const electron = require("electron")
async function createNoteFrame(html, time) {
    const note = document.createElement("iframe")
    note.frameBorder = false
    note.height = "250px"
    note.srcdoc = "<dialog id='dialog'>" + html + "</dialog>"
    note.sandbox = 'allow-same-origin'
    note.onload = (ev) => {
        const dialog = new Proxy(ev.target.contentWindow.dialog, {
            get: (target, prop) => {
                const res = target[prop];
                return typeof res === "function" ? res.bind(target) : res;
            },
        })
        setInterval(dialog.close, time / 2);
        setInterval(dialog.showModal, time);
    }
    return note
}

class api {
    getConfig(){
        return electron.ipcRenderer.invoke("get-config")
    }
    setConfig(conf, obj){
        electron.ipcRenderer.invoke("set-config", conf, obj)
    }
    window(){
        electron.ipcRenderer.invoke("get-window")
    }
}

window.api = new api()

document.addEventListener("DOMContentLoaded", async () => {
    if (document.location.origin !== "file://") {
        document.write(`<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8" />
    <title>Hati Hati!</title>
    <style>
        body {
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            background-color: skyblue;
        }

        h1 {
            text-align: center;
            color: white;
        }
    </style>
</head>

<body>
</body>

</html>`)
        const header = document.createElement("h1")
        header.setHTML("Palang Darurat")
        document.body.appendChild(header)
        const mynote = await createNoteFrame("<h1>Hati Hati!</h1><p>Website " + decodeURIComponent(document.location) + " Kemungkinan Berbahaya!</p>", 1000)
        document.body.appendChild(mynote)
    } else {
        const embed = (await window.api.getConfig()).embed
        document.getElementById("embed").setHTML("<h1>"+embed+"</h1>")
    }
})
