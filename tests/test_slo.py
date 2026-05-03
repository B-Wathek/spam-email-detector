import time

def test_latency_slo():
    start = time.time()

    # simulate model inference
    time.sleep(0.1)

    latency = time.time() - start

    assert latency < 0.3  # 300ms SLO
