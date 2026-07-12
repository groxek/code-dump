package main

import (
	"fmt"
	"math/rand/v2"
)

type account struct {
	login    string
	password string
	url      string
}

var letterRunes = []rune("abcdefghkjklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")

func main() {
	fmt.Println(rand.IntN(10))
	str := []rune("Hello")
	for _, ch := range string(str) {
		fmt.Println(ch, string(ch))
	}


	login := promptData("Введите логин")
	password := promptData("Введите пароль")
	url := promptData("Введите URL")
	

	acc := account{
		login: login,
		password: password,
		url: url,
	}

	outputPassword(&acc)
}

func promptData(prompt string) string {
	fmt.Print(prompt + ": ")
	var res string
	fmt.Scan(&res)
	return res
}

func outputPassword(acc *account) {
	fmt.Println(acc)
	return st
}



func generatePassword(n int) string {
	res := make([]rune, n)
}