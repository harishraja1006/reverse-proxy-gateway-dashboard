/*
==========================================================
API MODULE
==========================================================
*/

const API_URL = "/api/dashboard";

/*
==========================================================
FETCH DASHBOARD DATA
==========================================================
*/

async function fetchDashboardData() {

    try {

        const response = await fetch(API_URL);

        return await response.json();

    }

    catch (error) {

        console.error("API Error:", error);

        return null;

    }

}
