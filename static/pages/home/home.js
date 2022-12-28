let dashboard = {
    ISSNow: async () => {
        let response = await getResponse("/api/iss/", "GET")
    }
}

let home = {
    start: async () => {
        await dashboard.ISSNow()
        await buildTable("idFifaStanding", "/api/epl-standing/", "GET", "", "idFifaStandingTable")
    }
}

window.addEventListener('DOMContentLoaded', async (event) => {

    document.getElementById("loader").style.display = "block";
    await home.start()
    document.getElementById("loader").style.display = "none";

    log.toasts("success", "DOM fully loaded and parsed")

    console.log('DOM fully loaded and parsed');

});

