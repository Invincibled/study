import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { UserComponent } from './user.component';
import { OrderComponent } from './order/order.component';
import { AddressComponent } from './address/address.component';



@NgModule({
  declarations: [UserComponent, OrderComponent, AddressComponent],
  exports:[UserComponent],
  imports: [
    CommonModule
  ]
})
export class UserModule { }
