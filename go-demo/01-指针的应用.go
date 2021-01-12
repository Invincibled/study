package main

import "fmt"

func main() {
	var a int = 10
	var b *int = &a
	fmt.Println(a)
	fmt.Println(b)
	fmt.Println(*b)

	*b = 250

	fmt.Println(a)
	fmt.Println(b)
	fmt.Println(*b)

}