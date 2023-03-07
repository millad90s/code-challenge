package main

import (
    "fmt"
)

func main() {
    var input float64
    fmt.Println("Enter a number:")
    fmt.Scanln(&input)
    result := input * 2
    fmt.Println("The result is:", result)
}