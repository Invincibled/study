import { Component, OnInit, ViewChild } from '@angular/core';

@Component({
  selector: 'app-news',
  templateUrl: './news.component.html',
  styleUrls: ['./news.component.css']
})
export class NewsComponent implements OnInit {
  @ViewChild("footer") footer:any

  constructor() { }

  ngOnInit(): void {
  }

  getChildMsg() {
    console.log(this.footer.msg)
  }

  getChildRun() {
    this.footer.run()
  }

  runParent($event: any) {
    alert($event)
  }
}
