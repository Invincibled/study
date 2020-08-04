import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {

  // let flag:boolean = true
  flat:boolean = true
  constructor() { }

  ngOnInit(): void {
    // 组件和指令初始化完成, 并不是真正的dom加载完成.
    let obox:any = document.getElementById("box")
    console.log(obox.innerHTML)
    obox.style.color="red"
  }

  // dom加载完成后触发的方法，
  ngAfterViewInit(){
    let obox:any = document.getElementById("box2")
    console.log(obox.innerHTML)
    obox.style.color="blue"
  }

}
