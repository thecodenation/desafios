# Readme

Teste básico de Golang

Listas os dez maiores estados brasileiros em extensão territorial

## Suite de testes para aprendizado

Arquivo: main_test.go

Comando: go get -u github.com/golang/dep/cmd/dep; dep ensure; go test

## Suite de testes para avaliação

Arquivo: submit_test.go

Comando: go get -u github.com/golang/dep/cmd/dep; dep ensure; go get -u github.com/jstemmer/go-junit-report ; go test -v | go-junit-report > output.xml

OBS: é necessário a geração do arquivo output.xml pois este será analisado durante o processo de avaliação