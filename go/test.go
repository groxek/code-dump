package main

import (
	"fmt"
	"math"
)

var sad bool

    func main() {
	height := 1.8
	var wight float64 = 100
	var IMT = wight / math.Pow(height, 2)
	fmt.Print(IMT)
}

func getUserInput() (float64, float64) {
    var userHeight float64
    var userKg float64
    fmt.Scan(&userHeight)
    fmt.Scan(&userKg)
    return userHeight, userKg
    
}

