const express    = require("express")
const app        = express()
const { execFile } = require("child_process")
require("dotenv").config()

const API_KEY = process.env.API_KEY
const DB_PASS = process.env.DB_PASS

// Xavfli eval funksiyasi butunlay olib tashlandi
app.get("/safe", (req, res) => {
    res.json({ message: "Xavfsiz xizmat" })
})

// execFile (shell injection xavfi yo'q) va faqat ruxsat berilgan buyruqlar filtri
const ALLOWED = ["ls", "pwd", "date"]
app.get("/cmd", (req, res) => {
    const cmd = req.query.q
    if (!ALLOWED.includes(cmd)) return res.status(400).send("Ruxsat yo'q")
    execFile(cmd, [], (err, out) => {
        if (err) return res.status(500).send(err.message)
        res.send(out)
    })
})

app.listen(process.env.PORT || 3000)
