/**
 * webpack的配置文件.
 * 作用: 只是webpack干哪些活，（当你运行webpack指令时,会加载里面的配置）
 *     所有的构建工具都是基于nodejs的，commonjs是nodejs模块的默认方式.
 * @type {{}}
 */
const { resolve }  = require('path')
const HtmlWebPackPlugin = require('html-webpack-plugin')
module.exports={
   entry:'./src/index.js',
   output:{
      filename: 'built.js',
      path: resolve(__dirname, 'build')
   },
   module:{
      rules:[
          // 不同类型的文件，使用不同的loader
          // 详细的loader配置
         {
            // test 匹配什么样的文件
            test: /\.css$/,
            use:[
                // use 数组中的loader执行顺序，从右到左，从下到上
                // 创建style标签，将js中的样式资源插入处理，添加到head中生效.
                'style-loader',
                // 将css文件变成commonjs模块加载js中，里面内容是样式字符串
                'css-loader'
            ]
         },
         {
            test:/\.less$/,
            use:[
               // use 数组中的loader执行顺序，从右到左，从下到上
               // 创建style标签，将js中的样式资源插入处理，添加到head中生效.
               'style-loader',
               // 将css文件变成commonjs模块加载js中，里面内容是样式字符串
               'css-loader',
                // 将less文件编译成css文件
               'less-loader'
            ]
         },
         {
            test:/\.(jpg|png|gif)$/,
            // 下载url-loader file-loader
            loader:'url-loader',
            options:{
               // 图片小于8kb，就会被base64处理
               // 优点，减少网络请求（减轻服务器压力）
               // 缺点, 图片体积变大
               limit: 8 * 1024,
               // 问题，因为url-loader使用es6模块进行解析，而html-loader使用commonjs模块解析
               //  解析时会出现[Object Module]
               // 解决： 关闭url-loader 的es6模块，使用commonjs模块解析(这个东西，新版本貌似解决了，不用加这个参数了)
               esModule: false,
               name:'[hash:10].[ext]'
            }
         },
         {
            test:/\.html$/,
            // 处理html中的img图片的.
            loader: 'html-loader'
         },
         {
            // 排除js/html/css/less其他的资源.
            exclude: /\.(js|html|css|less)$/,
            loader: 'file-loader'
         }
      ]
   },
   plugins:[
       // 详细的插件配置
       new HtmlWebPackPlugin({
          template: './src/index.html'
       })
   ],
   mode: 'development',
   // mode:'production'
   devServer:{
      contentBase: resolve(__dirname, 'build'),
      compress: true,
      port:3000,
      open:true
   }
}