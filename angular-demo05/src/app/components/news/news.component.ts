import { Component, OnInit } from '@angular/core';
import {HttpClient, HttpResponse} from "@angular/common/http";

@Component({
  selector: 'app-news',
  templateUrl: './news.component.html',
  styleUrls: ['./news.component.css']
})
export class NewsComponent implements OnInit {
  productList:any[]
  constructor(public http: HttpClient) { }

  ngOnInit(): void {
  }

  doGet() {
    let api = "http://a.itying.com/api/productlist"
    this.http.get(api).subscribe((response:any)=>{
      console.log(response)
      this.productList = response.result
    })
  }

  doSubmit() {
   console.log("执行")
  }
}
