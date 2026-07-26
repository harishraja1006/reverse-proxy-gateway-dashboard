from flask import Flask

from .proxy import forward_request
from .health import start_health_monitor
from dashboard.routes import dashboard

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
# Health Status of Backend Servers
# ==========================================================

@app.route("/health-status")
def health_status():
    from .health import server_health
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
# Run Application
# ==========================================================

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=8000
    )
