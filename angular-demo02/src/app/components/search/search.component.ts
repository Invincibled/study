import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-search',
  templateUrl: './search.component.html',
  styleUrls: ['./search.component.css']
})
export class SearchComponent implements OnInit {

  public keyword:String = ""
  public list = new Set()
  constructor() { }

  ngOnInit(): void {
  }

  doSearch(){
    this.list.add(this.keyword)
    this.keyword = ""

  }

  delSearch(item){
    this.list.delete(item)
  }

}
