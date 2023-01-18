let health = {
    fetchRules: async () => {
        let url = '/api/health/rule/'
        let method = 'GET'
        let response = await getResponse(url, method)

        return response
    },
    buildRules: async () => {
        let idRulesCardDiv = document.getElementById("idRulesCardDiv")
        let response = await health.fetchRules()
        let card = await createCard(jsonPrettyHTML(response), "Rules", "collapseIdRules", "javascript:health.buildRules()")
        idRulesCardDiv.innerHTML = ""
        idRulesCardDiv.appendChild(card)
        log.toasts("success", "Rules fetched")

    },
    addRules: async () => {

        var formEl = document.getElementById("idAddRuleForm")

        let rule = document.getElementById("idRuleInput")
        if (rule.value.length == 0 ) {
            log.toasts("error", "input is required")
            return
        }
        body = {
            "name": rule.value
        }
        let url = formEl.action
        let method = 'POST'
        let response = await getResponse(url, method, body)
        rule.value = ""
        health.buildRules()



    }
}

window.addEventListener('DOMContentLoaded', async () => {

    document.getElementById("loader").style.display = "block";
    await health.buildRules()
    document.getElementById("loader").style.display = "none";
    document.getElementById("idHealthHomeContainer").classList.remove("no-display")

    console.log('DOM fully loaded and parsed. health.html');
});
