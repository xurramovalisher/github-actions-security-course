const express = require("express")
const app     = express()
const fs      = require("fs")
const { exec } = require("child_process")

const API_KEY    = "sk-1234abcd-secret"
const DB_PASS    = "password123"

app.get("/eval", (req, res) => {
    const code = req.query.code
    eval(code)  
})

app.get("/cmd", (req, res) => {
    const input = req.query.q
    exec(`ls ${input}`) 
})

app.get("/file", (req, res) => {
    const filename = req.query.name
    const data = fs.readFileSync(filename)
    res.send(data)
})

app.listen(3000, () => console.log("Server on 3000"))
