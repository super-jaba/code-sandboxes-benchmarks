import asyncio
import time
import random
import os

from daytona import AsyncDaytona, DaytonaConfig, AsyncSandbox

from programs import PROGRAMS


# Fix SSL certificate verification on macOS
# This ensures Python can verify SSL certificates by using certifi's certificate bundle
try:
    import certifi
    os.environ['SSL_CERT_FILE'] = certifi.where()
except ImportError:
    pass  # certifi not available, will use system defaults


class SandboxPool:
    def __init__(self, daytona: AsyncDaytona, num_sandboxes: int):
        self._daytona = daytona
        self._num_sandboxes = num_sandboxes

    async def init_sandboxes(self):
        self.sandboxes = await asyncio.gather(*[self._daytona.create() for _ in range(self._num_sandboxes)])

    async def run_program(self, program: str) -> tuple[AsyncSandbox, str, float]:
        start_time = time.perf_counter()

        sandbox = random.choice(self.sandboxes)
        response = await sandbox.process.code_run(program)
        if response.exit_code != 0:
            print(f"Error: {response.exit_code} {response.result}")
        
        elapsed_ms = (time.perf_counter() - start_time) * 1000
        return sandbox, response.result, elapsed_ms

    async def clear_sandboxes(self):
        await asyncio.gather(*[self._daytona.delete(sandbox) for sandbox in self.sandboxes])


async def main() -> None:
    config = DaytonaConfig(
        # api_key="dtn_bafa691545d140b4b6cdae09cd228d017edac63f68c21cba3537f99e30aab8c4",  # production key
        api_key="dtn_e686a90966de9489d3a4ede98d963dc364296be06ead308a3c3b1c249a1da663",  # local key
        api_url="http://localhost:3000/api"
    )
    daytona = AsyncDaytona(config)
    sandbox_pool = SandboxPool(daytona, 1)
    await sandbox_pool.init_sandboxes()

    results = await asyncio.gather(*[sandbox_pool.run_program(program) for program, _expected in PROGRAMS[:1]])
    for sandbox, result, elapsed_ms in results:
        print(f"Sandbox {sandbox.id}: {elapsed_ms:.2f} ms")

    # await sandbox_pool.clear_sandboxes()
    await daytona.close()


if __name__ == "__main__":
    asyncio.run(main())