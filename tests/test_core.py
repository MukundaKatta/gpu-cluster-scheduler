"""Tests for GpuClusterScheduler."""
from src.core import GpuClusterScheduler
def test_init(): assert GpuClusterScheduler().get_stats()["ops"] == 0
def test_op(): c = GpuClusterScheduler(); c.learn(x=1); assert c.get_stats()["ops"] == 1
def test_multi(): c = GpuClusterScheduler(); [c.learn() for _ in range(5)]; assert c.get_stats()["ops"] == 5
def test_reset(): c = GpuClusterScheduler(); c.learn(); c.reset(); assert c.get_stats()["ops"] == 0
def test_service_name(): c = GpuClusterScheduler(); r = c.learn(); assert r["service"] == "gpu-cluster-scheduler"
