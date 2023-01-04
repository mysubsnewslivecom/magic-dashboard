let gitsvn = {
    load: async () => {
        var idGitProjectsStanding = document.getElementById("idGitProjectsStanding");

        const value = JSON.parse(document.getElementById('project-data').textContent);

        // var jsonPretty = JSON.stringify(value,null,4);
        // idGitProjectsStanding.innerHTML = "<pre><code>" + jsonPretty + "</code></pre>"

        let table = await createTable(value, "", "idGitProjectsStandingTable")
        idGitProjectsStanding.appendChild(table)
        document.getElementById('project-data').remove()
        dataTablesJS("#idGitProjectsStandingTable")
        idGitProjectsStanding.classList.remove("no-display")
    }
}

let issues = {
    getIssues: async (id) => {

        let url = `/api/git/issues/gitab/${id}/`
        let method = 'GET'
        let response = await getResponse(url, method)
        return response
    },
    buildList: async () => {

        document.getElementById("loader").style.display = "block";
        // var id = window.location.pathname.split('/').slice(-1);
        // console.log(`typeof ${typeof(id)}`);

        var id = document.getElementById("idIssueID").value;

        let data = await issues.getIssues(id)
        var idIssueDetail = document.getElementById("idIssueDetail")

        if (data.length === 0) {
            document.getElementById("loader").style.display = "none";
            idIssueDetail.innerHTML = ""
        }
        else {

            var issueDetailDiv = document.createElement("div")
            issueDetailDiv.classList.add("my-3")
            issueDetailDiv.style = "font-family: Roboto"

            var h3El = document.createElement("h3")
            h3El.classList.add("mb-3")
            h3El.innerText = "Issue Details"

            issueDetailDiv.appendChild(h3El)

            for ([key, val] of Object.entries(data)) {

                var divParent = document.createElement("div")
                divParent.classList.add("mb-3", "row", "border-bottom")

                var labelEl = document.createElement("label")
                labelEl.setAttribute("for", key)
                labelEl.classList.add("col-sm-2", "col-form-label")
                labelEl.innerText = key.toUpperCase()

                var divChildEl = document.createElement("div")
                divChildEl.classList.add("col-sm-7")

                var inputEl = document.createElement("input")
                inputEl.type = "text"
                inputEl.readOnly = true
                inputEl.classList.add("form-control-plaintext")
                inputEl.id = `id${key}`
                inputEl.value = val

                divChildEl.appendChild(inputEl)

                divParent.appendChild(labelEl)
                divParent.appendChild(divChildEl)

                issueDetailDiv.appendChild(divParent)

            }
            idIssueDetail.innerHTML = ""
            idIssueDetail.appendChild(issueDetailDiv)
            document.getElementById("loader").style.display = "none";

        }

    }
}

window.addEventListener('DOMContentLoaded', async () => {


    //    const id = window.location.pathname.split('/').slice(-1);

    //    id = document.getElementById("idIssueID").value;

    //    await issues.buildList(id)

    document.getElementById("loader").style.display = "none";
    document.getElementById("idIssueCreate").classList.remove("no-display")

    console.log('DOM fully loaded and parsed. base.html');
});


