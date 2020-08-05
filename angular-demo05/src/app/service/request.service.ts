import { Injectable } from '@angular/core';
import {Observable} from "rxjs";

@Injectable({
  providedIn: 'root'
})
export class RequestService {

  constructor() {

  }

  getData(){
    return "this is msg"
  }

  getDataCallBack(cb){
    setTimeout(function () {
        var name = "李四"
        cb(name)
    }, 1000)
  }

  getDataByPromise(){
    return new Promise(function (resolve) {
         setTimeout(function () {
           var name = "李四--promise"
                resolve(name)
         }, 2000)
    })
  }

  getDataByRxjs(){
    return new Observable((observer)=>{
      setTimeout(function () {
        var name = "李四--rxjs"
        observer.next(name)

      }, 2000)
    })
  }

  getDataIntervalByPromis(){
    return new Promise(function (resolve) {
      setInterval(function () {
        var name = "李四--promise Interval"
        resolve(name)
      }, 2000)
    })
  }

  getDataIntervalByRxjs(){
    var count = 0
    return new Observable((observer)=>{
      setInterval(function () {
        count++
        var name = "李四--rxjs Interval " + count
        observer.next(name)

      }, 2000)
    })
  }

  getDataIntervalByRxjss(){
    var count = 1
    return new Observable((observer)=>{
      setInterval(function () {
        count++
        observer.next(count)

      }, 1000)
    })
  }
}
