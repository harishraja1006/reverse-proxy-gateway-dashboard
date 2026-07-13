from flask import Flask
import requests

app = Flask(__name__)

servers = [
    "http://localhost:5001",
    "http://localhost:5002",
    "http://localhost:5003"
]

connections = {
    "http://localhost:5001": 0,
    "http://localhost:5002": 0,
    "http://localhost:5003": 0
}

current = 0

@app.route('/')
def balance():
    global current

    server = servers[current]
    current = (current + 1) % len(servers)

    connections[server] += 1

    print("\nActive Connections")
    print(connections)

    response = requests.get(server)

    connections[server] -= 1

    return response.text

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
