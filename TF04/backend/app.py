from flask import Flask, jsonify, request
import os
import time
import random
import logging
import json

app = Flask(__name__)
INSTANCE_ID = os.getenv("INSTANCE_ID", "unknown")
START_TIME = time.time()

metrics = {
    "instance_id": INSTANCE_ID,
    "requests_total": 0,
    "success_total": 0,
    "error_total": 0,
    "total_latency_seconds": 0.0,
    "last_request": None,
}

logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger("backend")

@app.before_request
def before_request():
    request.start_time = time.time()

@app.after_request
def after_request(response):
    duration = time.time() - getattr(request, "start_time", time.time())
    metrics["requests_total"] += 1
    if response.status_code < 500:
        metrics["success_total"] += 1
    else:
        metrics["error_total"] += 1
    metrics["total_latency_seconds"] += duration
    metrics["last_request"] = {
        "path": request.path,
        "method": request.method,
        "status": response.status_code,
        "duration_seconds": round(duration, 3),
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
    }

    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "GET,POST,OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type,Authorization"

    logger.info(json.dumps({
        "instance_id": INSTANCE_ID,
        "path": request.path,
        "method": request.method,
        "status": response.status_code,
        "duration_seconds": round(duration, 3),
        "remote_addr": request.remote_addr,
    }))
    return response

@app.route("/api/info")
def info():
    return simulate_workload("standard")

@app.route("/api/workload/<level>")
def workload(level):
    return simulate_workload(level)

def simulate_workload(level):
    workload_map = {
        "light": (0.1, 0.3),
        "medium": (0.4, 0.7),
        "heavy": (0.8, 1.5),
        "standard": (0.2, 0.8),
    }
    low, high = workload_map.get(level, workload_map["standard"])
    delay = random.uniform(low, high)
    time.sleep(delay)
    payload = {
        "instance_id": INSTANCE_ID,
        "workload": level,
        "response_time_seconds": round(delay, 3),
    }
    if level == "heavy":
        payload["alert"] = "High simulated workload"
    return jsonify(payload)

@app.route("/health")
def health():
    return jsonify({
        "status": "ok",
        "instance": INSTANCE_ID,
        "uptime_seconds": round(time.time() - START_TIME, 2),
    })

@app.route("/status")
def status():
    uptime_seconds = round(time.time() - START_TIME, 2)
    average_latency = (
        metrics["total_latency_seconds"] / metrics["requests_total"]
        if metrics["requests_total"] else 0.0
    )
    return jsonify({
        "instance_id": INSTANCE_ID,
        "uptime_seconds": uptime_seconds,
        "requests_total": metrics["requests_total"],
        "success_total": metrics["success_total"],
        "error_total": metrics["error_total"],
        "average_latency_seconds": round(average_latency, 3),
        "last_request": metrics["last_request"],
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)