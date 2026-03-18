"""Basic usage example for gpu-cluster-scheduler."""
from src.core import GpuClusterScheduler

def main():
    instance = GpuClusterScheduler(config={"verbose": True})

    print("=== gpu-cluster-scheduler Example ===\n")

    # Run primary operation
    result = instance.learn(input="example data", mode="demo")
    print(f"Result: {result}")

    # Run multiple operations
    ops = ["learn", "assess", "recommend]
    for op in ops:
        r = getattr(instance, op)(source="example")
        print(f"  {op}: {"✓" if r.get("ok") else "✗"}")

    # Check stats
    print(f"\nStats: {instance.get_stats()}")

if __name__ == "__main__":
    main()
