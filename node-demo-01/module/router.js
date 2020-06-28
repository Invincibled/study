const url = require('url')
const fs = require('fs')
const path = require('path')

function changeRes(res){
    res.send=(data)=>{
        res.writeHead(200,{'Content-Type':'text/html;charset=utf-8'})
        res.end(data)
    }
}
let getFileMime = function(extname){
    let data = fs.readFileSync('./data/mime.json')
    let mimeObj = JSON.parse(data.toString())
    return mimeObj[extname]
}

function initStatic(req, res, staticPath){
    let pathname = url.parse(req.url).pathname
    pathname = pathname == '/'?'index.html':pathname
    let extname = path.extname(pathname)

    if (pathname != '/favicon.ico'){
        try{
            let data = fs.readFileSync('./' + staticPath + pathname)
            if (data){
                let mime = getFileMime(extname)
                res.writeHead(200, {'Content-Type':''+mime + ";charset=UTF-8"})
                res.end(data)
            }
        }catch (error) {

        }
    }
}

let server = ()=>{

    let G = {
        _get: {},
        _post: {},
        staticPath:'static'
    }

    let app = function (req, res) {
        changeRes(res)
        initStatic(req, res, G.staticPath)
        let pathname = url.parse(req.url).pathname
        let method = req.method.toLowerCase()
        if (G._get[pathname]){
            G._get[pathname](req, res)
        }else if(G._post[pathname]){
            let postData = ''
            req.on('data',(chunk)=>{
                postData += chunk
            })
            req.on('end', ()=>{
                req.body = postData
                G._post[pathname](req, res)
            })

        } else{
            res.writeHead(404,{'Content-Type':'text/html;charset=utf-8'})
            res.end('不存在')
        }
    }

    app.get = function (str, cb) {
        G._get[str] = cb;
    }

    app.post = function (str, cb) {
        G._post[str] = cb
    }
    app.static = function (staticPath) {
         G.staticPath = staticPath
    }
    return app
}


module.exports = server()