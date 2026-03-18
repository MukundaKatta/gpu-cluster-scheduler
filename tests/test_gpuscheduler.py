"""Tests for GPUScheduler."""
import pytest
from src.gpuscheduler import GPUScheduler

def test_init():
    obj = GPUScheduler()
    stats = obj.get_stats()
    assert stats["total_ops"] == 0

def test_operation():
    obj = GPUScheduler()
    result = obj.submit_job(input="test")
    assert result["processed"] is True
    assert result["operation"] == "submit_job"

def test_multiple_ops():
    obj = GPUScheduler()
    for m in ['submit_job', 'schedule', 'preempt']:
        getattr(obj, m)(data="test")
    assert obj.get_stats()["total_ops"] == 3

def test_caching():
    obj = GPUScheduler()
    r1 = obj.submit_job(key="same")
    r2 = obj.submit_job(key="same")
    assert r2.get("cached") is True

def test_reset():
    obj = GPUScheduler()
    obj.submit_job()
    obj.reset()
    assert obj.get_stats()["total_ops"] == 0

def test_stats():
    obj = GPUScheduler()
    obj.submit_job(x=1)
    obj.schedule(y=2)
    stats = obj.get_stats()
    assert stats["total_ops"] == 2
    assert "ops_by_type" in stats
