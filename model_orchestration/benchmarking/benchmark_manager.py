from datetime import datetime


class BenchmarkManager:
    benchmarks = []

    @classmethod
    def record(cls, task_name, provider, model, success=True, latency_ms=0):

        cls.benchmarks.append(
            {
                "timestamp": datetime.now().isoformat(),
                "task": task_name,
                "provider": provider,
                "model": model,
                "success": success,
                "latency_ms": latency_ms,
            }
        )

    @classmethod
    def get_all(cls):

        return cls.benchmarks
