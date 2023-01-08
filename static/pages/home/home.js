let dashboard = {
    ISSNow: async () => {
        let url = '/api/iss/'
        let method = 'GET'
        let response = await getResponse(url, method)

        let idISSLocation = document.getElementById("idISSLocation")
        if (idISSLocation) {
            const { iss_position } = response
            const { longitude, latitude } = iss_position
            idISSLocation.innerText = `${longitude}, ${latitude}`
        }
    },
    getIP: async () => {
        let url = '/api/ip/'
        let method = 'GET'
        let response = await getResponse(url, method)
        let idIP = document.getElementById("idIP")
        if (idIP) {
            const { ip } = response
            idIP.innerText = ip
        }

    }
}

let task = {
    getTodo: async () => {

        let url = '/api/task/todo/'
        let method = 'GET'
        let response = await getResponse(url, method)

        response.forEach(el => {
            console.log(el);
            task.buildList(response)
        });

        // return await response
    },
    createTodo: async () => {
        var taskId = document.getElementById("new-task-input")
        body = { "name": taskId.value, "status": false }
        let url = '/api/task/todo/'
        let method = 'POST'
        let response = await getResponse(url, method, body)
        console.log(response);
        return await response

    },
    deleteTodo: async () => {

        let url = `/api/task/todo/${id}`
        let method = 'POST'
        let response = await getResponse(url, method)
        return await response

    },
    updateTodo: async () => {

    },
    buildList: async (data) => {

        console.log(data);

        let taskDiv = document.getElementById("tasks")
        taskDiv.innerHTML = ""
        // let response = await task.getTodo()

            var divEl = document.createElement("div")
            divEl.classList.add("list-group", "w-auto", "mb-1")

            var labelEl = document.createElement("label")
            labelEl.classList.add("list-group-item", "d-flex", "gap-3")

            var inputCheckEl = document.createElement("input")
            inputCheckEl.classList.add("form-check-input", "flex-shrink-0")
            inputCheckEl.type = "checkbox"
            inputCheckEl.style = "font-size: 1.375em;"
            // inputCheckEl.checked = data["status"]
            // inputCheckEl.value = data["status"]

            var spanTitle = document.createElement("span")
            spanTitle.classList.add("pt-1", "form-checked-content")

            var inputEl = document.createElement("input")
            inputEl.setAttribute("data-id", data["id"])
            inputEl.type = "text"
            inputEl.readOnly = true
            inputEl.classList.add("form-control-plaintext")
            inputEl.value = data["name"]

            spanTitle.appendChild(inputEl)

            labelEl.appendChild(inputCheckEl)
            labelEl.appendChild(spanTitle)

            divEl.appendChild(labelEl)

            taskDiv.appendChild(divEl)

    }
}


let home = {
    start: async () => {
        var idGitProjectsDiv = document.createElement("div")
        idGitProjectsDiv.id = "idGitProjectsDiv"

        var idFifa = document.getElementById("idFifaStanding")

        dashboard.ISSNow()
        dashboard.getIP()

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

        task.buildList()

    }
}

window.addEventListener('DOMContentLoaded', async (event) => {

    document.getElementById("loader").style.display = "block";
    await home.start()
    document.getElementById("loader").style.display = "none";

    log.toasts("success", "DOM fully loaded and parsed")

    console.log('DOM fully loaded and parsed');

});
