const { app, BrowserWindow, ipcMain } = require('electron')
const path = require("path")
/**
 * @type {BrowserWindow}
 */
var mainWindow;

const createWindow = () => {
  const win = new BrowserWindow({
    width: 800,
    height: 600,
    webPreferences: {
      preload: path.join(__dirname, "./preload.js"),
      nodeIntegration: false,
      contextIsolation: false,
    },
    fullscreen: true,
  })
  win.loadFile("./Shigure-Ui/index.html")
  return win
}

let config = {
  embed: process.argv[1]
}

ipcMain.handle("set-config", (_, conf, obj) => {
  Object.assign(config[conf], obj)
})

ipcMain.handle("get-config", (_) => {
  return config
})

ipcMain.handle("get-window", (_) => {
  const win = new BrowserWindow({
    width: 800,
    height: 600,
    parent: mainWindow,
    webPreferences: {
      preload: path.join(__dirname, 'preload.js'),
      nodeIntegration: false,
      contextIsolation: false,
    },
    fullscreen: true,
  })
  win.loadFile("./Shigure-Ui/index.html")
})

app.whenReady().then(() => {
  mainWindow = createWindow()
})

app.on('browser-window-created', (_, win) => {
  if(mainWindow){
    if (mainWindow.getChildWindows().length > 0){
      win.close()
    }
  }
})
