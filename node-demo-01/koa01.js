const koa = require('koa')
const Router = require('koa-router')
const mongoose = require('mongoose')
const db = require("./config/keys").mongoURI
const passport = require('koa-passport')
const users = require("./routes/api/users")
const app = new koa()
const router = new Router()


router.get('/', async ctx=>{
    ctx.body = {msg:"hello koa interface"}
})

mongoose.connect(db,{useUnifiedTopology: true, useNewUrlParser: true}).then(
    ()=>{
        console.log("mongodb connected")
    }
).catch(err=>{
    console.log(err)
})

require('./config/passport')(passport)

// app.use(users)
// app.use('/api/users', users)


app.use(router.routes()).use(router.allowedMethods())

const port = process.env.PORT || 5000;

app.listen(port, ()=>{
    console.log(`server started on ${port}`)
})
