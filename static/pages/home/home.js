let dashboard = {
    ISSNow: async () => {
        let response = await getResponse("/api/iss/", "GET")
    }
}

let home = {
    start: async () => {
        var idGitProjectsDiv = document.createElement("div")
        idGitProjectsDiv.id = "idGitProjectsDiv"

        var idFifa = document.getElementById("idFifaStanding")

        await dashboard.ISSNow()

        let payload = {
            "elementId": idFifa.id,
            "url": "/api/epl-standing/",
            "method": "GET",
            "exclusionList": "",
            "tableId": "idFifaStandingTable",
            "cardTitle": "Fifa Standing",
            "refreshCard": "refreshFifaStanding"
        }
        await buildTable(payload)

        let bDivider = document.createElement("div")
        bDivider.classList.add("b-divider")

        if (idFifa.nextSibling) {
            idFifa.parentNode.insertBefore(bDivider, idFifa.nextSibling);
            bDivider.parentNode.insertBefore(idGitProjectsDiv, bDivider.nextSibling);
        } else {
            idFifa.parentNode.appendChild(bDivider);
            bDivider.parentNode.appendChild(idGitProjectsDiv);
        }

        // if (bDivider.nextSibling) {
        //     bDivider.parentNode.insertBefore(idGitProjectsDiv, bDivider.nextSibling);
        // } else {
        //     bDivider.parentNode.appendChild(idGitProjectsDiv);
        // }

        payload = {
            "elementId": idGitProjectsDiv.id,
            "url": "/api/git/projects/",
            "method": "GET",
            "exclusionList": "",
            "tableId": "idGitProjectsTable",
            "cardTitle": "Git projects",
            "refreshCard": "refreshGitProjects"
        }
        await buildTable(payload)
    }
}

window.addEventListener('DOMContentLoaded', async (event) => {

    document.getElementById("loader").style.display = "block";
    await home.start()
    document.getElementById("loader").style.display = "none";

    log.toasts("success", "DOM fully loaded and parsed")

    console.log('DOM fully loaded and parsed');

});



