import { Component, OnInit, ViewChild } from '@angular/core';

/**
 *
 */
@Component({
  selector: 'app-news',
  templateUrl: './news.component.html',
  styleUrls: ['./news.component.css']
})
export class NewsComponent implements OnInit {

  @ViewChild("myBox") mybox:any

  @ViewChild("header") header:any

  constructor() { }

  ngOnInit(): void {
  }

  ngAfterViewInit():void{
     console.log(this.mybox.nativeElement)
     this.mybox.nativeElement.style.color='red'
     this.mybox.nativeElement.style.width='200px'
     this.mybox.nativeElement.style.height='200px'
     this.mybox.nativeElement.style.border='1px solid pink'

    this.header.run()
  }

}
