import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-lifecycle-component',
  templateUrl: './lifecycle-component.component.html',
  styleUrls: ['./lifecycle-component.component.css']
})
export class LifecycleComponentComponent implements OnInit {

  constructor() {
    console.log("00构造函数")
  }


  onChanges(){
    console.log("01ngChange执行了----当被绑定的输入属性")
  }

  ngOnInit(): void {
    console.log("02oninit 执行了---请求数据一般放在这里")
  }

  ngDoCheck(){
    console.log("03ngDocheck 执行了检测")
  }

  ngAfterContentInit(){
    console.log("04 ngAfterContentInit 执行了-当把内容")
  }

  ngAfterContentChecked(){
    console.log("05 ngAfterContentChecked 执行了-每次完成被投影组件内容的变更检测之后调用")
  }

  ngAfterViewInit(){
    console.log("06 ngAfterViewInit 执行了---初始化完成组件视图及其子视图之后调用")
  }

  ngAfterViewChecked(){
    console.log("07 ngAfterViewChecked 执行了--每次做完组件视图的变更检测之后调用")
  }
  ngOnDestroy(){
    console.log("08 ngOnDestroy 执行了销毁。。。。")
  }

}
