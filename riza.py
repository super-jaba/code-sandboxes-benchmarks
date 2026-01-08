import asyncio
import time
from rizaio import Riza

from programs import PROGRAMS

client = Riza(
    base_url="http://localhost:3004",
    api_key="riza_self_hosted",
)

async def run_program(program: str, expected: str) -> tuple[str, str, str, float]:
    """Run a program using Riza and return (program, result, expected, elapsed_ms)"""
    start_time = time.perf_counter()
    result = None
    try:
        # Run the synchronous Riza call in a thread pool to enable concurrency
        resp = await asyncio.to_thread(
            client.command.exec,
            language="python",
            code=program
        )
        # Extract result from response - adjust based on actual Riza response structure
        # Common patterns: resp.stdout, resp.output, resp.result, or dict(resp)['output']
        if hasattr(resp, 'stdout'):
            result = resp.stdout.strip()
        elif hasattr(resp, 'output'):
            result = resp.output.strip()
        elif hasattr(resp, 'result'):
            result = str(resp.result).strip()
        else:
            # Try converting to dict and look for common fields
            resp_dict = dict(resp) if hasattr(resp, '__dict__') or hasattr(resp, 'keys') else {}
            result = resp_dict.get('stdout', resp_dict.get('output', resp_dict.get('result', str(resp)))).strip()
    except Exception as e:
        print(f"Error: {e}")
        result = f"Error: {e}"
    
    elapsed_ms = (time.perf_counter() - start_time) * 1000
    return program, result, expected, elapsed_ms

async def main():
    # Run programs concurrently (first 15 like singlesandbox.py)
    results = await asyncio.gather(*[
        run_program(program, expected) 
        for program, expected in PROGRAMS[:15]
    ])
    
    # Check results and report errors
    for program, result, expected, _elapsed_ms in results:
        if result != expected:
            print("Error!")
            print(f"Program: {program}")
            print(f"Result: {result}")
            print(f"Expected: {expected}")
            print("--------------------------------")
    
    # Print benchmarking statistics
    elapsed_times = [elapsed_ms for _, _, _, elapsed_ms in results]
    print(f"Average execution time: {sum(elapsed_times) / len(elapsed_times):.2f} ms")
    for elapsed in sorted(elapsed_times):
        print(f"Execution time: {elapsed:.2f} ms")

if __name__ == "__main__":
    start_time = time.perf_counter()
    asyncio.run(main())
    end_time = time.perf_counter()
    total_time = end_time - start_time
    print(f"\nTotal execution time: {total_time:.2f} seconds")