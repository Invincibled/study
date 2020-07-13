import { Component, OnInit } from '@angular/core';
import {analyticsPackageSafelist} from "@angular/cli/models/analytics";
@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {

  public title = "home我是一个title"

  public picUrl = "https://www.baidu.com/img/PCfb_5bf082d29588c07f842ccde3f97243ea.png"
  public keyword:string="默认值"
  public list:any[] = [
    {"title":"我是title1"},
    {"title":"我是title2"},
    {"title":"我是title3"},
    {"title":"我是title4"}

  ]

  public flag: boolean = true;

  public orderStatus:number = 2;

  public attr:string = "red"

  public today: any = new Date()
  constructor() { }

  ngOnInit(): void {
  }

  run(){
    console.log("自定义事件")
  }

  runEvent(e){
    console.log(e)
    let dom:any = e.target
    dom.style.color='red'
  }

  getData(){
    alert(this.orderStatus)
  }

  setData(){
    this.orderStatus = 5
  }
  keyDown(e){
    console.log(e)
    console.log(e.target.value)
  }

  keyUp(e){
    console.log(e)
  }

  changeData(){
    this.keyword="这是改变后的值"
  }
  changeGetData(){
    console.log(this.keyword)
  }
}
