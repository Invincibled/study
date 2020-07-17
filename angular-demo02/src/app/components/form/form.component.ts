import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-form',
  templateUrl: './form.component.html',
  styleUrls: ['./form.component.css']
})
export class FormComponent implements OnInit {

  constructor() { }


  public  peopleInfo:any={
    username:"111",
    sex:'1',
    citys:['北京','上海','深圳'],
    city:'上海',
    hobby:[{
      title:"吃饭",
      check:false
    },
      {
        title:"睡觉",
        check:false
      },
      {
        title:"打豆豆",
        check:true
      }],
    remark:"备注信息"
  }

  ngOnInit(): void {
  }

  doSubmit(e){
     console.log(e)
  }

}
