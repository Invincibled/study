
import { Product } from '../types.ts';
import {v4} from 'https://deno.land/std/uuid/mod.ts';

let productList: Product[] =[
    {
        id:"1",
        name:"产品一",
        description:"我是产品一",
        price:29.99,
    },
    {
        id:"2",
        name:"产品二",
        description:"我是产品二",
        price:29.99,
    },
    {
        id:"3",
        name:"产品三",
        description:"我是产品三",
        price:29.99,
    }
]

// @desc 获取所有产品

// @route Get api/v1/products

const getProducts=({response}: {response:any})=>{
   response.body = {
       success:true,
       data: productList,

   }
}
// @desc 获取单个产品
// @route Get api/v1/product/:id
const getProduct=({response, params}:  {params:{id:string}; response:any})=>{
    const product:Product | undefined = productList.find((p)=>p.id == params.id);
    if (product){
        response.status =200;
        response.body={
            success:true,
            data:product
        }
    }else {
        response.status =404;
        response.body={
            success:false,
            msg:"抱歉，没有这个产品"
        }
    }

 }

 // @desc 添加单个产品
// @route POST api/v1/product/
const addProduct= async ({request, response}: {request:any, response:any})=>{
    const body = await request.body()

    if(!request.hasBody){
        response.status =400;
        response.body={
            success:false,
            msg:"没有数据"
        }
    }else{
        const product:Product = body.value
        product.id = v4.generate()
        response.status =201;
        response.body={
            success:true,
            data:product
        }
    }
}

// @desc 更新单个产品
// @route Get api/v1/product/:id
const updateProduct=({params,request, response}: {params:{id:string}; request:any, response:any})=>{
    const product:Product | undefined = productList.find((p)=>p.id == params.id);
    if (product){
        const body = request.body()
        const updateData :{name?:string, descritpion?:string, price?:number} = body.value;

        productList = productList.map(p=>p.id === params.id ? {...p, ...updateData}: p);
        response.status =200;
        response.body={
            success:true,
            data:productList
        }
    }else {
        response.status =404;
        response.body={
            success:false,
            msg:"抱歉，没有这个产品"
        }
    }

}

// @desc 删除单个产品
// @route Delete api/v1/product/:id
const deleteProduct=({params, response}: {params:{id:string}; response:any})=>{
    productList = productList.filter(p => p.id !== params.id)
    response.status = 200;
    response.body={
        success:true,
        data:"产品已删除"
    }
}

export {getProducts, addProduct, updateProduct, deleteProduct, getProduct}