import logging
import os

os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename="logs/access.log",
    level=logging.INFO,
    format="%(asctime)s | %(message)s"
)

logger = logging.getLogger("reverse-proxy")
