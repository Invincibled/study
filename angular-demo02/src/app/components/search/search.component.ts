import { Component, OnInit } from '@angular/core';
import {StorageService} from "../../services/storage.service";

@Component({
  selector: 'app-search',
  templateUrl: './search.component.html',
  styleUrls: ['./search.component.css']
})
export class SearchComponent implements OnInit {

  public keyword:String = ""
  public list = new Set()

  constructor(public storage: StorageService) {

  }

  ngOnInit(): void {
    let local = this.storage.get("searchList")
    if (local) {
      this.list = new Set(local)
    }
  }

  doSearch(){
    this.list.add(this.keyword)
    console.log(this.list)
    this.storage.set("searchList", this.list)
    this.keyword = ""

  }

  delSearch(item){
    this.list.delete(item)
    this.storage.set("searchList", this.list)
  }

}
