const express = require('express')
const ejs = require('ejs')

const  app = express()
app.set("view engine", "ejs")

app.get(
    '/',
    (req, res)=>{
        let title = "你好ejs"
        res.render('index',{title:title})
    }
)

app.listen(3000)