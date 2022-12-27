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
