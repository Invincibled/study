const {MongoClient} = require('mongodb')

const  url = "mongodb:/127.0.0.1:27017"
const  dbName = "itying"

let mongoClient = new MongoClient(url,{useUnifiedTopology : true})

mongoClient.connect((err)=>{
    if(err){
        console.log(err)
        return ;
    }
    console.log("数据库连接成功")

    let db = mongoClient.db(dbName)

    db.co

    // 操作数据库完毕后关闭
    mongoClient.close();
})