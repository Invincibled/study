const  koa = require('koa')


let app = new koa()

app.use(async  ctx=>{
    console.log("ctx")
    ctx.body = "你好,koa2.x"
})

app.listen(3000)