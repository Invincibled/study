import { Component, OnInit , Output,EventEmitter} from '@angular/core';

@Component({
  selector: 'app-footer',
  templateUrl: './footer.component.html',
  styleUrls: ['./footer.component.css']
})
export class FooterComponent implements OnInit {

  @Output("outer") outer: any = new EventEmitter()

  msg:string = "我是子组件信息"
  constructor() { }

  ngOnInit(): void {
  }

  run(){
    console.log("我是子组件方法")
  }
  sendParent(){
    this.outer.emit('msg is child')
  }

}
