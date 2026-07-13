/*
==========================================================
Reverse Proxy Gateway Dashboard
Version 4
==========================================================
*/

const API_URL = "/api/dashboard";

let dashboardData = {};

/*
==========================================================
REQUESTS CHART
==========================================================
*/

let requestsChart;

let requestHistory = [];

let labels = [];

let previousRequestCount = 0;

let connectionsChart;

let connectionHistory = [];

let distributionChart;

let responseChart;

let responseHistory = [];
let eventHistory = [];
/*
==========================================================
LIVE CLOCK
==========================================================
*/

function updateClock() {

    document.getElementById("clock").textContent =
        new Date().toLocaleTimeString();

}

/*
==========================================================
FETCH DATA
==========================================================
*/

async function fetchDashboardData() {

    try {

        const response = await fetch(API_URL);

        dashboardData = await response.json();

        updateDashboard();

    }

    catch (error) {

        console.error(error);

    }

}

/*
==========================================================
UPDATE DASHBOARD
==========================================================
*/

function updateDashboard() {

    //-----------------------------
    // Top Cards
    //-----------------------------

    document.getElementById("algorithm").textContent =
        dashboardData.algorithm
            .replaceAll("_", " ")
            .replace(/\b\w/g, c => c.toUpperCase());

    document.getElementById("totalRequests").textContent =
        dashboardData.total_requests;

    document.getElementById("failedRequests").textContent =
        dashboardData.failed_requests;

    document.getElementById("healthyServers").textContent =
        dashboardData.healthy_servers;

/*
==========================================================
AVERAGE RESPONSE
==========================================================
*/

const s1 =
    dashboardData.server_stats["http://localhost:5001"].response_time;

const s2 =
    dashboardData.server_stats["http://localhost:5002"].response_time;

const s3 =
    dashboardData.server_stats["http://localhost:5003"].response_time;

const avgResponse =
    ((s1 + s2 + s3) / 3).toFixed(2);

document.getElementById("avgResponse").textContent =
    `${avgResponse} ms`;
    document.getElementById("clusterStatus").textContent =
        `${dashboardData.healthy_servers} / 3 ONLINE`;
/*
==========================================================
SCHEDULER
==========================================================
*/

document.getElementById("scheduler").textContent =
    dashboardData.algorithm
        .replaceAll("_"," ")
        .replace(/\b\w/g,c=>c.toUpperCase());
    //-----------------------------
    // Backend Servers
    //-----------------------------

    updateServer(
        1,
        "http://localhost:5001"
    );

    updateServer(
        2,
        "http://localhost:5002"
    );

    updateServer(
        3,
        "http://localhost:5003"
    );
    updateRequestChart();
    updateConnectionsChart();
    updateDistributionChart();
    updateResponseChart();
    updateEventLog();
}
/*
==========================================================
UPDATE REQUEST CHART
==========================================================
*/

function updateRequestChart() {

    const now = new Date();

    labels.push(
        labels.length + 1
    );

    const currentRequests =
        dashboardData.total_requests;

if (previousRequestCount === 0) {

    previousRequestCount = currentRequests;

}

const requestsPerSecond =
    currentRequests - previousRequestCount;

previousRequestCount =
    currentRequests;
    requestHistory.push(
        requestsPerSecond
    );

    if (labels.length > 20) {

        labels.shift();
        requestHistory.shift();

    }

    requestsChart.update();

}
function updateConnectionsChart() {

    let totalConnections = 0;

    for (const server in dashboardData.active_connections) {

        totalConnections +=
            dashboardData.active_connections[server];

    }

    connectionHistory.push(totalConnections);

    if (connectionHistory.length > 20) {

        connectionHistory.shift();

    }

    connectionsChart.update();

}

/*
==========================================================
UPDATE DISTRIBUTION CHART
==========================================================
*/

function updateDistributionChart() {

    distributionChart.data.datasets[0].data = [

        dashboardData.server_stats["http://localhost:5001"].requests,

        dashboardData.server_stats["http://localhost:5002"].requests,

        dashboardData.server_stats["http://localhost:5003"].requests

    ];

    distributionChart.update();

}

/*
==========================================================
UPDATE RESPONSE CHART
==========================================================
*/

function updateResponseChart() {

    const s1 =
        dashboardData.server_stats["http://localhost:5001"].response_time;

    const s2 =
        dashboardData.server_stats["http://localhost:5002"].response_time;

    const s3 =
        dashboardData.server_stats["http://localhost:5003"].response_time;

    const average =
        (s1 + s2 + s3) / 3;

    responseHistory.push(average);

    if (responseHistory.length > 20) {

        responseHistory.shift();

    }

    responseChart.update();

}
/*
==========================================================
UPDATE SERVER CARD
==========================================================
*/

function updateServer(number, url){

    const health =
        dashboardData.server_health[url];

    const active =
        dashboardData.active_connections[url];

    const stats =
        dashboardData.server_stats[url];

    document.getElementById(
        `server${number}-status`
    ).textContent =
        health ? "🟢 UP" : "🔴 DOWN";

    document.getElementById(
        `server${number}-connections`
    ).textContent =
        active;

    document.getElementById(
        `server${number}-response`
    ).textContent =
        `${stats.response_time} ms`;

    document.getElementById(
        `server${number}-requests`
    ).textContent =
        stats.requests;

}


/*
==========================================================
INITIALIZE CHARTS
==========================================================
*/

function initializeCharts() {

    const ctx =
        document.getElementById("requestsChart");

    requestsChart = new Chart(ctx, {

        type: "line",

        data: {

            labels: labels,

            datasets: [

                {

                    label: "Requests",

                    data: requestHistory,

                    borderColor: "#38bdf8",

                    backgroundColor: "rgba(56,189,248,.2)",

                    borderWidth: 3,

                    fill: true,

                    tension: .35

                }

            ]

        },

        options: {

            responsive: true,

            maintainAspectRatio: false,

            animation: true,

            scales: {

                y: {

                    beginAtZero: true

                }

            }

        }

    });
const ctx2 =
    document.getElementById("connectionsChart");

connectionsChart = new Chart(ctx2, {

    type: "line",

    data: {

        labels: labels,

        datasets: [

            {

                label: "Connections",

                data: connectionHistory,

                borderColor: "#22c55e",

                backgroundColor: "rgba(34,197,94,.2)",

                borderWidth: 3,

                fill: true,

                tension: .35

            }

        ]

    },

    options: {

        responsive: true,

        maintainAspectRatio: false,

        animation: true,

        scales: {

            y: {

                beginAtZero: true

            }

        }

    }

});
const ctx3 =
    document.getElementById("distributionChart");

distributionChart = new Chart(ctx3, {

    type: "pie",

    data: {

        labels: [

            "Server 1",

            "Server 2",

            "Server 3"

        ],

        datasets: [

            {

                data: [0,0,0],

                backgroundColor: [

                    "#38bdf8",

                    "#22c55e",

                    "#f59e0b"

                ]

            }

        ]

    },

    options: {

        responsive:true,

        maintainAspectRatio:false

    }

});
const ctx4 =
    document.getElementById("responseChart");

responseChart = new Chart(ctx4, {

    type: "line",

    data: {

        labels: labels,

        datasets: [

            {

                label: "Response Time",

                data: responseHistory,

                borderColor: "#f59e0b",

                backgroundColor: "rgba(245,158,11,.2)",

                borderWidth: 3,

                fill: true,

                tension: .35

            }

        ]

    },

    options: {

        responsive: true,

        maintainAspectRatio: false,

        scales: {

            y: {

                beginAtZero: true

            }

        }

    }

});
}
/*
==========================================================
EVENT LOG
==========================================================
*/

function updateEventLog() {

    const log = document.getElementById("eventLog");

    const now = new Date().toLocaleTimeString();

    const latest =
        `[${now}] Requests: ${dashboardData.total_requests} | Healthy: ${dashboardData.healthy_servers}/3`;

    eventHistory.unshift(latest);

    if (eventHistory.length > 10) {

        eventHistory.pop();

    }

    log.innerHTML = eventHistory.join("<br>");

}
/*
==========================================================
AUTO REFRESH
==========================================================
*/

function startAutoRefresh(){

    fetchDashboardData();

    setInterval(fetchDashboardData,1000);

}

/*
==========================================================
INITIALIZATION
==========================================================
*/

document.addEventListener("DOMContentLoaded",()=>{

     updateClock();

     initializeCharts();

     setInterval(updateClock,1000);

     startAutoRefresh();
});
