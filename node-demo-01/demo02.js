// const  fs = require('fs')
//
// fs.stat('./' , function (err, data) {
//       if (err){
//           console.log(err)
//           return
//       }
//       console.log(`是文件:${data.isFile()}`)
//       console.log(`是目录:${data.isDirectory()}`)
//
// })

let app = function () {
  console.log("这是一个方法")
}

app.get = function () {
  console.log("这是第二个方法")
}
app()
app.get()
console.log(typeof  app)