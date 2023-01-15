let health = {
    fetchRules: async () => {
        let url = '/api/health/rule/'
        let method = 'GET'
        let response = await getResponse(url, method)

        return response
    },
    buildRules: async () => {
        let response = await health.fetchRules()
        log.toasts("success", "Rules fetched")
        let idRules = document.getElementById("idRules")
        idRules.innerHTML = ""
        idRules.appendChild(jsonPrettyHTML(response))
    }
}

window.addEventListener('DOMContentLoaded', async () => {

    document.getElementById("loader").style.display = "block";
    await health.buildRules()
    document.getElementById("loader").style.display = "none";
    document.getElementById("idHealthHomeContainer").classList.remove("no-display")

    console.log('DOM fully loaded and parsed. health.html');
});
