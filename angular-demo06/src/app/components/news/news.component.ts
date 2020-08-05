import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-news',
  templateUrl: './news.component.html',
  styleUrls: ['./news.component.css']
})
export class NewsComponent implements OnInit {

  public newsList:any[] = new Array()
  constructor() {
    // var list:any[]
    // for (let i =0;i<10;i++){
    //   // console.log(this.newsList)
    //   // this.newsList.push("111")
    //   console.log(111)
    //   console.log(this.newsList)
    //   list.push("1111")
    // }
    // this.newsList = list
  }

  ngOnInit(): void {
    for (let i =0;i<10;i++){
      console.log(this.newsList)
      this.newsList.push(`我是第${i}条数据`)
    }

  }
  // ngAfterViewInit(){
  //   for (let i =0;i<10;i++){
  //     // console.log(this.newsList)
  //     // this.newsList.push("111")
  //     console.log(111)
  //     console.log(this.newsList)
  //   }
  // }

}
