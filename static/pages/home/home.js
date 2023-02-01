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

        let taskDiv = document.getElementById("tasks")
        taskDiv.innerHTML = ""

        response.forEach(el => {
            task.buildList(el)
        });
    },
    createTodo: async () => {
        var taskId = document.getElementById("new-task-input")

        if (taskId.value.length == 0) {
            log.toasts("error", "Task input is required!!!")
            return
        }
        body = { "name": taskId.value, "status": false }
        let url = '/api/task/todo/'
        let method = 'POST'
        let response = await getResponse(url, method, body)
        if (Object.keys(response)[0] == "error") {
            return
        }
        task.buildList(response)
        taskId.value = ""
        log.toasts("success", "Task added!")
        return await response
    },
    deleteTodo: async (id) => {

        body = { "is_active": false }
        let url = `/api/task/todo/${id}/`
        let method = 'PATCH'
        let response = await getResponse(url, method, body)
        log.toasts("success", "Task removed!")
        return await response

    },
    updateTodo: async (data) => {
        body = data
        let url = `/api/task/todo/${data.id}/`
        let method = 'PATCH'
        let response = await getResponse(url, method, body)
        log.toasts("success", "Task updated!")
        return await response

    },
    buildList: async (data) => {

        let taskDiv = document.getElementById("tasks")

        var divEl = document.createElement("div")
        divEl.classList.add("list-group", "w-auto", "mb-1")

        var labelEl = document.createElement("label")
        labelEl.classList.add("list-group-item", "d-flex", "gap-3")

        var inputCheckEl = document.createElement("input")
        inputCheckEl.classList.add("form-check-input", "flex-shrink-0")
        inputCheckEl.type = "checkbox"
        inputCheckEl.style = "font-size: 1.375em;"
        inputCheckEl.checked = data.status
        inputCheckEl.id = `data-chk-${data.id}`
        inputCheckEl.maxLength = 150

        var spanTitle = document.createElement("span")
        spanTitle.classList.add("pt-1", "form-checked-content")

        var inputEl = document.createElement("input")
        inputEl.classList.add("form-control-plaintext")
        inputEl.setAttribute("data-id", data.id)
        inputEl.setAttribute('data-status', data.status)
        inputEl.setAttribute('data-name', data.name)
        inputEl.type = "text"
        inputEl.readOnly = true
        inputEl.value = data.name

        spanTitle.appendChild(inputEl)

        labelEl.appendChild(inputCheckEl)
        labelEl.appendChild(spanTitle)

        const task_actions_el = document.createElement('div');
        task_actions_el.classList.add('actions');

        const task_edit_el = document.createElement('button');
        task_edit_el.id = `data-edit-${data.id}`
        task_edit_el.classList.add('edit');
        task_edit_el.innerText = 'Edit';

        const task_delete_el = document.createElement('button');
        task_delete_el.classList.add('delete');
        task_delete_el.id = `data-delete-${data.id}`
        task_delete_el.innerText = 'Delete';

        task_actions_el.appendChild(task_edit_el);
        task_actions_el.appendChild(task_delete_el);

        labelEl.appendChild(task_actions_el);

        divEl.appendChild(labelEl);

        taskDiv.appendChild(divEl)

        var task_edit_el_btn = document.getElementById(`data-edit-${data.id}`);
        task_edit_el_btn.addEventListener('click', (e) => {
            if (task_edit_el_btn.innerText.toLowerCase() == "edit") {
                task_edit_el_btn.innerText = "Save";
                inputEl.removeAttribute("readonly");
                inputEl.focus();
            } else {
                task_edit_el_btn.innerText = "Edit";
                inputEl.setAttribute("readonly", "readonly");
                inputEl.dataset.name = inputEl.value;
                inputEl.dataset.id = data.id;
                task.updateTodo(inputEl.dataset)
            }
        });

        var task_delete_el_btn = document.getElementById(`data-delete-${data.id}`);
        task_delete_el_btn.addEventListener('click', (e) => {
            var dataset = {
                "id": data.id,
                "is_active": false
            }
            taskDiv.removeChild(divEl);
            task.updateTodo(dataset)
        });

        var task_chk_el_btn = document.getElementById(`data-chk-${data.id}`);
        task_chk_el_btn.addEventListener('click', (e) => {
            var dataset = {
                "id": data.id,
                "status": !data.status
            }
            task.updateTodo(dataset)
        });
    }
}

let health = {
    generateHealth: async () => {
        let steps_arr = Array()
        let distance_arr = Array()
        let floor_arr = Array()
        let cal_arr = Array()
        let date_arr = Array()

        let resp = await getResponse('/api/health/fitbit/', 'GET')

        resp.forEach(el => {
            cal_arr.push(el["calories_burned"])
            steps_arr.push(el["steps"])
            distance_arr.push(el["distance"] * 1000)
            floor_arr.push(el["floor"])
            date_arr.push(el["date"])
        })

        steps_avg = 0;
        distance_avg = 0;

        steps_arr.forEach(items => {
            steps_avg += items
        })

        distance_arr.forEach(items => {
            distance_avg += items
        })

        document.getElementById("idAverage").innerText = Math.round(steps_avg/steps_arr.length)
        document.getElementById("idAverageDistance").innerText = Math.round(distance_avg/distance_arr.length)

        const ctx = document.getElementById('myChart');

        let chartStatus = Chart.getChart("myChart"); // <canvas> id
        if (chartStatus != undefined) {
            chartStatus.destroy();
        }

        new Chart(ctx, {
            data: {
                labels: date_arr,
                datasets: [{
                    type: 'line',
                    label: '# of steps',
                    data: steps_arr,
                    borderWidth: 1
                },
                {
                    type: 'line',
                    label: '# of distance',
                    data: distance_arr,
                    borderWidth: 1
                },
                {
                    type: 'line',
                    label: '# of calories',
                    data: cal_arr,
                    borderWidth: 1
                }]
            },


            options: {
                animations: {
                    tension: {
                        duration: 1000,
                        easing: 'linear',
                        from: 1,
                        to: 0,
                        loop: true
                    }
                },
                scales: {
                    y: {
                        beginAtZero: true,
                        min: 0,
                        // max: 100
                    }
                },
                plugins: {
                    title: {
                        display: true,
                        text: 'Fitbit data',
                        align: 'center'
                    }
                }
            }


        });
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
            "id": idFifa.id,
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
            "id": idGitProjectsDiv.id,
            "url": "/api/git/projects/",
            "method": "GET",
            "exclusionList": "",
            "tableId": "idGitProjectsTable",
            "cardTitle": "Git projects",
            "refreshCard": "refreshGitProjects"
        }
        await buildTable(payload)

        task.getTodo()

        health.generateHealth()

    }
}

window.addEventListener('DOMContentLoaded', async (event) => {

    document.getElementById("loader").style.display = "block";
    await home.start()
    document.getElementById("loader").style.display = "none";
    document.getElementById("idHomeContainer").classList.remove("no-display")

    log.toasts("success", "DOM fully loaded and parsed")

    console.log('DOM fully loaded and parsed');

});
