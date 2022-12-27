let dashboard = {
    ISSNow: async () => {
        let response = await getResponse("/api/iss/", "GET")
    }
}

let home = {
    start: async () => {
        await dashboard.ISSNow()
    }
}

window.addEventListener('DOMContentLoaded', async (event) => {

    home.start()

});

