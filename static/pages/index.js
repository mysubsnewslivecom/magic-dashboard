function dataTablesJS(name) {
    console.log(`loading datatables ${name}!!!`)
    $(document).ready(function () {
        $(name).DataTable(
            {
                "paging": true,
                "destroy": true,
                "searching": true,
                "order": [[0, "desc"]],
                "pageLength": 10,
                // "processing": true,
                // "serverSide": true,
                // "resetPaging": true,
                // "cache": false,
                language: {
                    "processing": "Loading. Please wait..."
                },
            }
        );
    })
};


function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


async function getResponse(url, method) {

    let options = restMeta.options(method)
    const response = await fetch(url, options);

    if (!response.ok) {
        alert("Unable to fetch system details.");
        throw new Error(`HTTP error! Status: ${response.status}`);
    }
    const data = await response.json();
    return await data;
}

let restMeta = {
    headers: (method) => {
        var headers = new Headers();
        headers.append('Content-type', 'application/json');
        headers.append("Accept", "application/json")
        if (method.toUpperCase() != "GET") {
            headers.delete("X-CSRFToken")
            headers.append("X-CSRFToken", getCookie('csrftoken'))
        }
        return headers
    },
    options: (method, ...args) => {
        method = method.toUpperCase()
        let options = {
            mode: 'cors',
            cache: 'default',
            method: method,
            headers: restMeta.headers(method),
            body: (method === "PATCH" || method === "POST") ? args : null
        };
        return options
    }
}

let log = {
    toasts: (type, desc) => {

        var textColor = "text-dark"

        if (type.toLowerCase() === "success") {
            bg = "bg-success"
            textColor = "text-dark"
        }
        else if (type.toLowerCase() === "error") {
            bg = "bg-danger"
            textColor = "text-white"

        }
        else if (type.toLowerCase() === "warn") {
            bg = "bg-warning"
            textColor = "text-white"
        }
        else {
            bg = "bg-info"
        }

        let toastContainer = document.querySelector(".toast-container")

        let toast = document.createElement("div")
        toast.classList.add("toast")
        toast.setAttribute("role", "alert")
        toast.setAttribute("aria-live", "assertive")
        toast.setAttribute("aria-atomic", "true")
        toast.setAttribute("data-bs-autohide", true)
        toast.setAttribute("data-bs-delay", 5000)


        let toastHeader = document.createElement("div")
        toastHeader.classList.add("toast-header", bg, textColor)

        // let toastHImg = document.createElement("img")
        // toastHImg.src = "..."
        // toastHImg.alt = "..."
        // toastHImg.classList.add("rounded", "me-2")

        let toastHTitle = document.createElement("strong")
        toastHTitle.classList.add("me-auto", "textColor")
        toastHTitle.innerText = type.toUpperCase()

        var currentdate = new Date();
        var datetime = currentdate.getDate() + "/"
            + (currentdate.getMonth() + 1) + "/"
            + currentdate.getFullYear() + " @ "
            + currentdate.getHours() + ":"
            + currentdate.getMinutes() + ":"
            + currentdate.getSeconds();

        let toastHSmall = document.createElement("small")
        toastHSmall.classList.add(textColor)
        toastHSmall.innerText = `${new Date().toLocaleString()}`

        let toastHClose = document.createElement("button")
        toastHClose.type = "button"
        toastHClose.classList.add("btn-close")
        toastHClose.setAttribute("data-bs-dismiss", "toast")
        toastHClose.setAttribute("aria-label", "Close")

        // toastHeader.appendChild(toastHImg)
        toastHeader.appendChild(toastHTitle)
        toastHeader.appendChild(toastHSmall)
        toastHeader.appendChild(toastHClose)

        let toastBody = document.createElement("div")
        toastBody.classList.add("toast-body")
        toastBody.innerText = desc

        toast.appendChild(toastHeader)
        toast.appendChild(toastBody)

        toastContainer.appendChild(toast)

        if (toast) {
            const toaster = new bootstrap.Toast(toast)
            toaster.show()
        }
    }
}

async function createTable(...args) {

    let data = args[0]
    let exclusionList = args[1]
    let tableId = args[2]

    let table = document.createElement("table")
    table.classList.add("table", "table-striped", "table-hover")
    table.id = tableId

    let tableTHead = document.createElement("thead")
    let tableTHeadTR = document.createElement("tr")
    let tableBody = document.createElement("tbody")

    let headers = Object.keys(data[0])

    headers.forEach(el => {
        if (!exclusionList.includes(el)) {
            let th = document.createElement("th")
            th.innerText = el.toUpperCase().replaceAll("_", " ")
            tableTHeadTR.appendChild(th)
        }
    });

    for (const items of data) {
        const rowElement = document.createElement("tr");
        for ([key, val] of Object.entries(items)) {
            for (const header of headers) {
                if (!exclusionList.includes(header)) {
                    if (header == key) {
                        const cellElement = document.createElement("td");
                        cellElement.textContent = val;
                        rowElement.appendChild(cellElement);
                    }
                }
            }
            tableBody.appendChild(rowElement);
        }
    }
    tableTHead.appendChild(tableTHeadTR)

    table.appendChild(tableTHead)
    table.appendChild(tableBody)
    return table
}


async function buildTable(payload) {
    const { elementId, url, method, exclusionList, tableId, cardTitle, refreshCard } = payload
    let idElement = document.getElementById(elementId)
    if (idElement) {
        let response = await getResponse(url, method)
        let table = await createTable(response, exclusionList, tableId)
        idElement.innerHTML = ""
        let card = await createCard(table, cardTitle, refreshCard)
        idElement.appendChild(card)
        dataTablesJS(`#${tableId}`)
    }
    else {
        console.log(`div ${elementId} not found!`);
    }
}


async function createCard(element, ...args) {

    var title = args[0]
    var refreshTarget = args[1]

    let parentCardDiv = document.createElement("div")
    parentCardDiv.classList.add("col-lg-12", "col-12")

    let card = document.createElement("div")
    card.classList.add("card")

    let cardHeader = document.createElement("div")
    cardHeader.classList.add("card-header")

    let row = document.createElement("div")
    row.classList.add("row")

    let rowChild = document.createElement("div")
    rowChild.classList.add("col-md-12", "bg-light", "text-right")

    let collapseButton = document.createElement("button")
    collapseButton.type = "button"
    collapseButton.classList.add("btn", "btn-link", "float-end")
    collapseButton.setAttribute("data-bs-toggle", "collapse")
    collapseButton.setAttribute("data-bs-target", `#${refreshTarget}`)
    collapseButton.setAttribute("aria-expanded", "false")
    collapseButton.setAttribute("aria-controls", refreshTarget)
    collapseButton.style = "text-decoration: none; border: 1px dashed #61affe;"
    collapseButton.innerHTML = '<i class="bi bi-arrows-collapse"></i>'

    let refreshButton = document.createElement("button")
    refreshButton.type = "button"
    refreshButton.classList.add("btn", "btn-link", "float-end")
    refreshButton.setAttribute("data-bs-target", `#${refreshTarget}`)
    refreshButton.setAttribute("aria-expanded", "false")
    refreshButton.setAttribute("aria-controls", refreshTarget)
    refreshButton.style = "text-decoration: none; border: 1px dashed #61affe;"
    refreshButton.innerHTML= '<i class="bi bi-arrow-clockwise"></i>'

    let rowChildH3 = document.createElement("h3")
    rowChildH3.classList.add("float-start")
    rowChildH3.innerText = title

    rowChild.appendChild(rowChildH3)
    rowChild.appendChild(collapseButton)
    rowChild.appendChild(refreshButton)

    row.appendChild(rowChild)

    cardHeader.appendChild(row)

    let parentCardBodyDiv = document.createElement("div")
    parentCardBodyDiv.classList.add("collapse", "collapse-horizontal", "show")
    parentCardBodyDiv.id = refreshTarget

    let cardBody = document.createElement("div")
    cardBody.classList.add("card-body")

    let childCardBody = document.createElement("div")
    childCardBody.id = `id${refreshTarget}`
    childCardBody.appendChild(element)

    cardBody.appendChild(childCardBody)

    card.appendChild(cardHeader)
    parentCardBodyDiv.appendChild(cardBody)
    card.appendChild(parentCardBodyDiv)

    parentCardDiv.appendChild(card)

    return parentCardDiv

}
