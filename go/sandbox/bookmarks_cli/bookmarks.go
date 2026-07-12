package main

import (
	"fmt"
)

type bookmarkMap = map[string]string


func iw() {

	a := []string{"1"}
	fmt.Println(a)


	bookmarks := bookmarkMap{}

	Menu:
		for {
			variant := getMenu()
			switch variant {

			case 1:
				printBookmarks(bookmarks)

			case 2:
				addBookmarks(bookmarks)

			case 3:
				deleteBookmark(bookmarks)

			case 4:
				fmt.Println("bye bye")
				break Menu
			}
		}
}

func getMenu() int {
	var variant int
	fmt.Println(`1 посмотреть закладки
2 добавть закладку
3 удалить закладку
4 выход`)
	fmt.Scan(&variant)
	return variant

}

func printBookmarks(bookmarks bookmarkMap) {
	if len(bookmarks) == 0 {
		fmt.Println("Закладок нет")
	}

	for key, value := range bookmarks {
		fmt.Println(key, ": ", value)
	}
} 

func addBookmarks(bookmarks bookmarkMap){
	var newBookmarksKey, newBoolmarksValue string
	fmt.Print("Введите название: ")
	fmt.Scan(&newBookmarksKey)
	fmt.Print("Введите ссылку: ")
	fmt.Scan(&newBoolmarksValue)
	bookmarks[newBookmarksKey] = newBoolmarksValue
}

func deleteBookmark(bookmarks bookmarkMap) {
	var bookmarkToDelete string
	fmt.Println("Введите название: ")
	fmt.Scan(&bookmarkToDelete)
	delete(bookmarks,bookmarkToDelete)
}
