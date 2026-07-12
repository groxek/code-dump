package main

import (
	"fmt"
)

func main() {
    tr := make([]string, 0,2)
    tr = append(tr, "1")
    tr = append(tr, "2")
    tr = append(tr, "3")
    fmt.Println(tr)

    transactions := []float64{}
	for {
        transaction := get()
        if transaction == 0 {
            break
        }
        transactions = append(transactions, transaction)
	}
    fmt.Println(transactions)
    totalBalance := calculateBalance(transactions)
    fmt.Println(totalBalance)

}

func get() float64 {
	var num float64
	fmt.Println("Введите транзакцию: ")
	fmt.Scan(&num)
	return num
}


func calculateBalance(transacrions []float64) float64 {
    var summa float64
    for _, val := range transacrions {
        summa += val
    }
    return summa
}