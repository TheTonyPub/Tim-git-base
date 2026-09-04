package main

import "fmt"

func fib(n int) int {
	if n < 0 {
		return -1
	}

	if n < 2 {
		return n
	}

	a, b := 0, 1
	for i := 2; i <= n; i++ {
		a, b = b, a+b
	}

	return b
}

func main() {
	fmt.Println(fib(12))
	fmt.Println(fib(15))
}
