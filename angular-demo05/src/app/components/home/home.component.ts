import { Component, OnInit } from '@angular/core';
import { RequestService } from '../../service/request.service'
import {filter, map} from "rxjs/operators";
@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {

  constructor(public request: RequestService) { }

  ngOnInit(): void {

    console.log(this.request)

    console.log(this.request.getData())


    this.request.getDataCallBack((msg)=>{
        console.log(msg)
    })


    let promis = this.request.getDataByPromise()

    promis.then((msg)=>{
      console.log(msg)
    })


    // let ob = this.request.getDataByRxjs()
    //
    // ob.subscribe((data)=>{
    //   console.log(data)
    // })


    // this.request.getDataIntervalByPromis().then((msg)=>{
    //   console.log(msg)
    // })
    //
    //
    // this.request.getDataIntervalByRxjs().subscribe((data)=>{
    //   console.log(data)
    // })
    //
    //
    // let stream = this.request.getDataIntervalByRxjss()

    // stream.pipe(
    //   filter((value:any)=>{
    //     if(value%2==0){
    //       return true
    //     }
    //   }),
    //  map((value:any)=>{
    //   return (value * value)
    //  })
    // ).subscribe((data)=>{
    //   console.log(data)
    // })


  }

}
