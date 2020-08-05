import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {

  public title:string="我是home的title"
  msg:string = "我是一条信息"
  constructor() { }

  ngOnInit(): void {
  }


  run(){
    console.log("父组件方法")
  }
}
