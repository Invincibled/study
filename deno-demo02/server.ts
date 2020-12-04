// 引入

import {Application} from 'https://deno.land/x/oak/mod.ts'
import router from './routes.ts'

// 初始化
const app = new Application();

app.use(router.routes())

app.use(router.allowedMethods())


//监听端口


console.log(`服务器正在5000端口号运行....`)
await app.listen({ port : 5000})