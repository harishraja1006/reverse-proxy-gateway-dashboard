#!/bin/sh

echo "Starting service: $SERVICE"

case "$SERVICE" in
    proxy)
        exec python -m loadbalancer.app
        ;;

    server1)
        exec python backend/server1.py
        ;;

    server2)
        exec python backend/server2.py
        ;;

    server3)
        exec python backend/server3.py
        ;;

    *)
        echo "Unknown SERVICE: $SERVICE"
        exit 1
        ;;
esac

