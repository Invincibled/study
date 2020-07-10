import { Component, OnInit } from '@angular/core';
import {consoleTestResultsHandler} from "tslint/lib/test";

@Component({
  selector: 'app-news',
  templateUrl: './news.component.html',
  styleUrls: ['./news.component.css']
})
export class NewsComponent implements OnInit {
  title ="news我是一个title";

  msg:string = " 我是新闻组件msg"
  userinfo={
    name:"张三",
    age: 18
  }


  content="<h2>我是一个html标签</h2>"


  cars:any[] =[
    {
      name:"奥迪",
      list:[
        {
          title:"奥迪1",
          price:"20万"
        },
        {
          title:"奥迪2",
          price:"30万"
        },
        {
          title:"奥迪3",
          price:"40万"
        }
      ]
    },
    {
      name:"宝马",
      list:[
        {
          title:"宝马1",
          price:"20万"
        },
        {
          title:"宝马2",
          price:"30万"
        },
        {
          title:"宝马3",
          price:"40万"
        }
      ]
    }
  ]
  constructor() {
    console.log(this.msg)

    this.msg = "我是改变后的值"
  }

  ngOnInit(): void {
  }
}
