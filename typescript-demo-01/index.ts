let str:string = "111"
let str1:string ="2222"
let str3:string = "333"

let  str4="fadfa"

enum Flag {success = 1 , error = -1}


var num:number|null|undefined;

console.log(num)


function remainParm(a:number, b:number, ...result:number[]):number {
    let sum = 0
    for ( let i = 0; i< result.length; i++){
        sum += result[i]
    }
    return sum
}

remainParm(1,2,3, 4, 5)


function f1(){
    return function (target:any) {
        console.log(target)
        console.log("装饰器1")
    }
}

function f2() {

    return function (target:any) {
       console.log(target)
        console.log("装饰器2")
    }
}



@f1()
@f2()
class Decrator{

    var api:string | undefined;





}

var d = Decrator()
console.log(d)