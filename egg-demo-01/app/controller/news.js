'use strict'

const Controller = require('egg').Controller

class NewsController extends Controller {
    async index() {
        const { ctx } = this;
       let msg ="hello "
        let list = await  this.service.news.getNewsList()
       await ctx.render('index',{
           msg,
           list
       })
    }
}

module.exports = NewsController;
