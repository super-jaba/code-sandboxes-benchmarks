import asyncio
import os
import time

# Fix SSL certificate verification on macOS
# This ensures Python can verify SSL certificates by using certifi's certificate bundle
try:
    import certifi
    os.environ['SSL_CERT_FILE'] = certifi.where()
except ImportError:
    pass  # certifi not available, will use system defaults

from daytona import AsyncDaytona, AsyncSandbox, DaytonaConfig

from programs import PROGRAMS

# Define the configuration
config = DaytonaConfig(
    # api_key="dtn_bafa691545d140b4b6cdae09cd228d017edac63f68c21cba3537f99e30aab8c4",  # production key
    api_key="dtn_e686a90966de9489d3a4ede98d963dc364296be06ead308a3c3b1c249a1da663",  # local key
    api_url="http://localhost:3000/api"
)

daytona = AsyncDaytona(config)

async def run_program(sandbox: AsyncSandbox, program: str, expected: str) -> tuple[str, str, str]:
    start_time = time.perf_counter()
    try:
        ctx = await sandbox.code_interpreter.create_context()

        response = await sandbox.code_interpreter.run_code(program, context=ctx)
        if response.error is not None:
            print(f"Error: {response.error}")
        
        await sandbox.code_interpreter.delete_context(ctx)
    except Exception as e:
        print(f"Error: {e}")
    elapsed_ms = (time.perf_counter() - start_time) * 1000

    return program, response.stdout, expected, elapsed_ms

async def main():
    sandbox = await daytona.create()

    results = await asyncio.gather(*[run_program(sandbox, program, expected) for program, expected in PROGRAMS[:15]])
    for program, result, expected, _elapsed_ms in results:
        if result != expected:
            print("Error!")
            print(f"Program: {program}")
            print(f"Result: {result}")
            print(f"Expected: {expected}")
            print("--------------------------------")

    print(f"Average execution time: {sum([elapsed_ms for _, _, _, elapsed_ms in results]) / len(results):.2f} ms")
    for elapsed in sorted([elapsed_ms for _, _, _, elapsed_ms in results]):
        print(f"Execution time: {elapsed:.2f} ms")

    await daytona.delete(sandbox)
    await daytona.close()


if __name__ == "__main__":
    start_time = time.perf_counter()
    asyncio.run(main())
    end_time = time.perf_counter()
    total_time = end_time - start_time
    print(f"\nTotal execution time: {total_time:.2f} seconds")