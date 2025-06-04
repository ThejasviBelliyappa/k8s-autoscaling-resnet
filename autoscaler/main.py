import requests, time, subprocess

def get_latency():
    try:
        resp = requests.get("http://prometheus:9090/api/v1/query?query=http_request_duration_seconds{quantile=\"0.99\"}")
        return float(resp.json()["data"]["result"][0]["value"][1])
    except Exception as e:
        print("Error fetching latency:", e)
        return 0.0

def scale_up():
    subprocess.run(["kubectl", "scale", "deployment", "inference", "--replicas=3"])

def scale_down():
    subprocess.run(["kubectl", "scale", "deployment", "inference", "--replicas=1"])

while True:
    latency = get_latency()
    if latency > 0.5:
        scale_up()
    elif latency < 0.3:
        scale_down()
    time.sleep(10)
