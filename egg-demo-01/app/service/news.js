'use strict';

const Service = require('egg').Service;

class NewsService extends Service {
    async getNewsList() {
        let list = ['000000000',"22222","3333"]
        return list
    }
}

module.exports = NewsService;
