from flask import Flask, Response
from prometheus_client import Counter, generate_latest
from prometheus_client import CONTENT_TYPE_LATEST
import logging
import uuid
logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)

app = Flask(__name__)
request_count = Counter("requests_total", "How many requests this service handled")

@app.route("/health")
def health():
    correlation_id = str(uuid.uuid4())
    logger.info({"event": "health_check", "correlation_id": correlation_id})
    request_count.inc()
    return "I'm alive"

@app.route("/metrics")
def metrics():
    return Response(generate_latest(), mimetype= CONTENT_TYPE_LATEST)

if __name__ == "__main__":
    app.run(port=8000)