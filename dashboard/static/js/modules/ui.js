/*
==========================================================
UI MODULE
==========================================================
*/

function updateClock() {

    document.getElementById("clock").textContent =
        new Date().toLocaleTimeString();

}

function updateDashboard(data) {

    if (!data) return;

    //-------------------------
    // Top Cards
    //-------------------------

    document.getElementById("algorithm").textContent =
        data.algorithm
            .replaceAll("_", " ")
            .replace(/\b\w/g, c => c.toUpperCase());

    document.getElementById("totalRequests").textContent =
        data.total_requests;

    document.getElementById("failedRequests").textContent =
        data.failed_requests;

    document.getElementById("healthyServers").textContent =
        data.healthy_servers;

    document.getElementById("clusterStatus").textContent =
        `${data.healthy_servers} / 3 ONLINE`;

    //-------------------------
    // Backend Servers
    //-------------------------

    updateServer(1, "http://localhost:5001", data);
    updateServer(2, "http://localhost:5002", data);
    updateServer(3, "http://localhost:5003", data);

}

function updateServer(number, url, data) {

    const stats = data.server_stats[url];

    document.getElementById(`server${number}-status`).textContent =
        data.server_health[url] ? "🟢 UP" : "🔴 DOWN";

    document.getElementById(`server${number}-connections`).textContent =
        data.active_connections[url];

    document.getElementById(`server${number}-response`).textContent =
        `${stats.response_time.toFixed(2)} ms`;

    document.getElementById(`server${number}-requests`).textContent =
        stats.requests;

}
