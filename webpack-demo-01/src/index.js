/**
 * 入口文件,webpack 入口起点文件.
 * 开发环境:webpack ./src/index.js -o ./build/built.js --mode=development
 *    webpack 会以./src/index.js 为入口文件开始打包,打包输出到./build/built.js，整体打包环境是开发环境
 * 生产环境:webpack ./src/index.js -o ./build/built.js --mode=production
 *
 * 结论：
 *   1. webpack能处理js，json资源，不能处理css、img资源
 *   2. 生产环境会压缩
 *   3. 能够编译es6module
 */

// import data from './data.json'
// // import './style.css'
//
// console.log(data)
//
// function add(a,b){
//     return a+b
// }
//
// console.log(add(2,1))

import './style.css'
import './style.less'

