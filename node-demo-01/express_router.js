const http = require('http')
const app = require('./module/router')
const ejs = require('ejs')

http.createServer(app).listen(3000)

app.static('public')

app.get('/login', function (req, res) {
    // res.writeHead(200,{'Content-Type':'text/plain;charset=utf-8'})
    // res.end('执行登录操作')
    ejs.renderFile('./views/form.ejs',{}, (error, data)=>{
        res.send(data)
    })
})

app.post('/doLogin',function (req, res) {
    res.send(req.body)
})