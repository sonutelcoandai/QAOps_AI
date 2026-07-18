from pathlib import Path
import sys
from model_orchestration.benchmarking.benchmark_manager import BenchmarkManager

ROOT_DIR = Path(__file__).resolve().parent.parent.parent

sys.path.insert(0, str(ROOT_DIR))


BenchmarkManager.record(
    task_name="test_case_generation",
    provider="ollama",
    model="qwen3",
    success=True,
    latency_ms=150,
)

print(BenchmarkManager.get_all())
