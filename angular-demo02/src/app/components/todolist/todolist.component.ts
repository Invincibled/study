import { Component, OnInit } from '@angular/core';

import { StorageService } from '../../services/storage.service';


@Component({
  selector: 'app-todolist',
  templateUrl: './todolist.component.html',
  styleUrls: ['./todolist.component.css']
})
export class TodolistComponent implements OnInit {


  public keyword:string=""

  public todolist:any[] = []

  constructor(public storage: StorageService) {

  }

  ngOnInit(): void {
    let local = this.storage.get("todoList")
    if (local) {
      this.todolist = local
    }
  }

  doAdd(e){
    if(e.keyCode === 13){
      if(!this.todolistHasKeyword(this.todolist, this.keyword)){
        this.todolist.push({title:this.keyword, status:0})
        this.storage.setL("todoList", this.todolist)
        this.keyword = ""
      }
      else {
        alert("数据已经存在")
        this.keyword = ""
      }
    }
  }

  delSearch(index){

    this.todolist.splice(index,1)
    this.storage.setL("todoList", this.todolist)
  }

  todolistHasKeyword(todolist:any, keyword:any):boolean{
    // 异步，会存在问题.
    //   todolist.forEach(value=>{
    //     if (value.title == keyword){
    //       return true;
    //     }
    //   });
    //
    if (!keyword){
      return false;
    }
    for(let i=0; i<todolist.length;i++){
      if (todolist[i].title == keyword){
              return true;
       }
    }
    return false;
  }
  changeBox(){
    this.storage.setL("todoList", this.todolist)
  }
}
