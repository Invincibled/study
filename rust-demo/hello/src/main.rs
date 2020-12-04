// const MAX_POINT : u32 = 10000;

fn main() {
    // let a =1 ;
    // println!("a={}", a);

    // let mut b = 1;
    // println!("b={}", b);

    // b = 2;
    // println!("b={}",b);
    // println!("Hello, world!");

    // println!("{}",MAX_POINT);


    //bool
    // let is_true: bool = true;

    // let is_false = false;

    // println!("{} {}", is_true, is_false);

    // char 是32位的,可以是个字符，也可以是汉字.
    // let a = 'a';

    // let b ="你";

    // println!("{} {}", a, b)

    // 自适应类型，isize,usize.在不同的平台上，所支持的不一样，比如64位，32位等等

    // println!("{}", usize::max_value())

    // 数组.

    println!("{}", usize::max_value());

    let arr : [u32; 5] = [0,0,1,1,1];

    println!("{}", arr[3]);

    show(arr);

    println!("-----------------");

    let tup: (u32, f32, char) = (2, 34.33, '号');

    println!("{}",tup.0);

    other_println();
    other_println1(333);
}
fn other_println(){
    println!("没有人合法");
}
fn other_println1(u1:u32){
    println!("{}", u1);
}
fn show(arr:[u32;5]){

    println!("--------------");

    for i in &arr{
        println!("{}", i);
    }
    println!("------------------")
}
