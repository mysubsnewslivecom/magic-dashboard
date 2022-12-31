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

// gitsvn.load()
