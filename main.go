package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
)

type (
	Config struct {
		Directory string `json:"directory"`
	}
)

func main() {
	config_file, _ := ioutil.ReadFile("config.json")

	var config Config
	json.Unmarshal(config_file, &config)

	fmt.Println(config)
}
