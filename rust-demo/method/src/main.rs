
fn other_fun2(a:i32, b:i32) -> i32{
    return a+b;
}

fn other_fun3()->i32{
   34343
}

fn scope(){

    {
        let y: u32 = 1;
        println!("{}", y);
    }

    {
        let mut s1 = String::from("hello");
        s1.push_str(" word");
        println!("{}", s1);
        let s2= s1;

        // s1 被赋值给s2后就无效了，相当于指针转移了
        let s3 = s2.clone();

        println!("{}", s3)
    }
}
fn main() {
    scope();
    println!("{}",other_fun2(1, 2));

    println!("{}",other_fun3());

//    // let x = (let y=1)
//    let y = {
//        let x = 1;
//        x+1
//    };

//    println!("{}", y);


//    if y==2 {
//        println!("{}", "打印y");
//    } else{
//        println!("{}", "不打印y")
//    }

//    loop {
//        println!("{}","")
//    }
   
}
