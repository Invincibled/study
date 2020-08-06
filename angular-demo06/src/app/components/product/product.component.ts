import { Component, OnInit } from '@angular/core';
import {Router,NavigationExtras} from "@angular/router";

@Component({
  selector: 'app-product',
  templateUrl: './product.component.html',
  styleUrls: ['./product.component.css']
})
export class ProductComponent implements OnInit {

  constructor(public  route:Router) { }

  ngOnInit(): void {
  }

  doget() {

    this.route.navigate(['/productcontent'])

  }

  dogetp() {
    this.route.navigate(['/productcontent','111'])
  }


  dogetparam() {
    let param : NavigationExtras={
      queryParams: { 'pid': 111}
    };
    this.route.navigate(['/prodctcontent'], param)
  }
}
