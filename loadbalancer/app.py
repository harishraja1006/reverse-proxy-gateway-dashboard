from flask import Flask

from .proxy import forward_request
from .health import start_health_monitor, server_health
from .metrics import generate_metrics
from .telemetry import server_stats
from dashboard.routes import dashboard

import os

app = Flask(__name__)

# Register Dashboard Blueprint
app.register_blueprint(dashboard)

# Start Background Health Monitoring
start_health_monitor()


# ==========================================================
# Reverse Proxy
# ==========================================================

@app.route("/")
def home():
    return forward_request()


# ==========================================================
# Health Status
# ==========================================================

@app.route("/health-status")
def health_status():
    return server_health


# ==========================================================
# Docker Health Check
# ==========================================================

@app.route("/health")
def health():
    return {
        "status": "healthy"
    }, 200


# ==========================================================
# Prometheus Metrics
# ==========================================================

@app.route("/metrics")
def metrics():
    return (
        generate_metrics(
            server_stats,
            server_health
        ),
        200,
        {
            "Content-Type": "text/plain"
        }
    )


# ==========================================================
# Run Application
# ==========================================================

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.getenv("PORT", 8000))
    )
