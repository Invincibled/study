const  Router = require('koa-router');
const  router = new Router()
const  gravatar = require('gravatar')
const  bcrypt = require('bcryptjs');
const  jwt = require('jsonwebtoken');
const tools = require('../../config/tools')
const  User = require('../../model/User')
const  keys = require('../../config/keys')
const passport = require('koa-passport')
const validate = require('../../validation/register')

router.get('/test', async ctx=>{
    ctx.status=200
    sleep(5000)
    ctx.body = {msg:"hello koa interface1111"}
})
function sleep(sleepTime) {
    for(var start = new Date; new Date - start <= sleepTime;) {}
}
router.post('/register', async ctx=>{

    const  {errors, isValid} = validate(ctx.request.body)
    if (!isValid){
        ctx.status = 400;
        ctx.body = errors
    }
    let findResult = await User.find({email: ctx.request.body.email})

    if (findResult.length >0){
        ctx.status = 500;
        ctx.body = {msg:"邮箱已被占用"}

    } else{
        const  avatar = gravatar.url('897456653@qq.com',{s:'200',r:'pg',d:'mm'})
        let user = new User({
            name:ctx.request.body.name,
            email: ctx.request.body.email,
            password: tools(ctx.request.body.password),
            avatar
        });

        // await bcrypt.genSalt(10,(error, salt)=>{
        //    bcrypt.hash(user.password, salt, (error,hash)=>{
        //        if (error) throw  error
        //        user.password = hash
        //    })
        // });

       await user.save().then(user=>{
           console.log(user)
       }).catch(err=>{
           console.log(err)
       })
        ctx.body = user
    }

})

router.post('/login',async  ctx => {
    const  findResult = await User.find({ email: ctx.request.body.email })
    const  password = ctx.request.body.password;
    const  user = findResult[0]
    if(findResult.length == 0){
        ctx.status = 404;
        ctx.body = {email:"用户不存在"}
    } else {
        let result = await bcrypt.compareSync( password,findResult[0].password)
        if(result){
            const  payload = {id: user.id, name:user.name, avatar: user.avatar}
            const  token = jwt.sign(payload, keys.secureOrKey, {expiresIn: 3600})
            ctx.status =200;

            ctx.body = {success:true, token: "Bearer " + token}
        }else{
            ctx.status =200;
            ctx.body = {msg:"密码错误"}
        }
    }
})
router.get('/current', passport.authenticate('jwt', {session: false}) ,async  ctx=>{
    ctx.body = ctx.state.user;
})

module.exports = router.routes()