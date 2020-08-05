import { Component, OnInit } from '@angular/core';
import {ActivatedRoute} from "@angular/router";

@Component({
  selector: 'app-newscontent',
  templateUrl: './newscontent.component.html',
  styleUrls: ['./newscontent.component.css']
})
export class NewscontentComponent implements OnInit {

  constructor(public route:ActivatedRoute) { }

  ngOnInit(): void {
    console.log(this.route.queryParams)
  }

}
