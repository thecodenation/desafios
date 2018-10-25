# Criando desafios na Code:Nation

## O que?

Na Code:Nation acreditamos que a melhor forma de aprender uma nova tecnologia, linguagem ou mesmo uma nova carreira é através de desafios práticos. É o chamado *challenge based learning*, onde a pessoa é apresentada a desafios práticos que vão ajudá-la a aprender os principais tópicos necessários para a sua evolução.

## Por que contribuir criando desafios?

Lembra quando você iniciou na carreira que está atuando hoje? A angústia de não saber o que estudar primeiro? A lista interminável e assustadora de links, livros, siglas... Tudo isso para começar a entender o básico? O quão frustrante isso pode ser? É esse sentimento que queremos mudar com a Code:Nation e você, que já passou por isso, pode nos ajudar a mudar esse cenário.

## Como criar um desafio?

Uma boa forma de iniciar o processo de criação é pensando nos conteúdos que o desafio vai ensinar ao(a) desenvolvedor(a). Por exemplo:

> Ao completar este desafio a pessoa terá aprendido o básico de Go, manipulação de slices e como ler um arquivo CSV.

### O título

Tudo começa com um bom título. Algo que vai chamar a atenção do(a) desenvolvedor(a) e o(a) convencer a clicar no desafio. Exemplos:  *Média do ENEM* , *Melhor nota de matemática do ENEM*, *Os dez maiores estados do Brasil*

### A descrição

Aqui é onde descrevemos o desafio em si - quais são seus objetivos e resultados esperados. Exemplo:

```
# Teste básico de Golang

## Objetivo

Listar os dez maiores estados brasileiros em extensão territorial

## Tópicos

Neste desafio você vai aprender:

- Go
- Testes unitários

## Requisitos
​
Para este desafio você precisará do Go versão 1.9 (ou superior). Para realizar os testes locais basta executar os comandos abaixo:
​

    cd ~/codenation/go-0
    codenation test -c go-0


```

OBS: este conteúdo vai ser salvo no arquivo *test_files/README.md*, então é possível usar markdown.

### O teste

Um dos tópicos mais importantes que o(a) desenvolvedor(a) precisa internalizar é o conceito de  *TDD* (*Test Driven Development*) - a abordagem da Code:Nation é fortemente baseada nesta crença.

Quando o(a) desenvolvedor(a) inicia o desafio utilizando o [codenation-cli](https://www.youtube.com/watch?v=Bmwpq8cjXso), recebe na sua máquina um diretório com uma estrutura similar a:

```
README.md: detalhes sobre o desafio e o que você precisa instalar na sua máquina para o desenvolvimento
main.go: é neste arquivo que você deve ser resolvido o desafio
main_test.go: testes unitários para auxiliá-lo no desenvolvimento. Este arquivo não deve ser alterado!
```

O exemplo acima mostra os arquivos de um desafio na linguagem *Go*, mas o mesmo conceito é aplicado a qualquer ambiente: uma suite de testes que o desenvolvedor usará para guiar seu desenvolvimento. Neste caso, o *test_files/main.go* é um "esqueleto" que o desenvolvedor usará para desenvolver.

Exemplo do esqueleto *test_files/main.go*:

```go
package main

import (
	"fmt"
)

func main() {

}

func os10maioresEstadosDoBrasil() ([]string, error) {
	var data []string
	return data, fmt.Errorf("Not implemented")
}

```

Exemplo do conteúdo do arquivo de testes, o *test_files/main_test.go*:

```go
package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func Test10MaioresEstadosDoBrasil(t *testing.T) {
	estados, err := os10maioresEstadosDoBrasil()
	assert.Nil(t, err)
	assert.Equal(t, 10, len(estados))
}

```

### O cálculo da nota

Quando o(a) desenvolvedor(a) entender que sua solução está pronta poderá submetê-la para avaliação. Para isso, executará o comando do [codenation-cli](https://www.youtube.com/watch?v=Bmwpq8cjXso) e um arquivo de testes especial é executado para que a nota seja calculada. A ideia é que o(a) desenvolvedor(a) não possa ver este arquivo - ele é executado apenas no momento da submissão e possui testes mais avançados para validarmos seu conhecimento. Exemplo de um arquivo de testes para este fim, o *submission_files/submit_test.go*:

```go
package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestSubmit10MaioresEstadosDoBrasil(t *testing.T) {
	estados, err := os10maioresEstadosDoBrasil()
	assert.Nil(t, err)
	assert.Equal(t, 10, len(estados))
	expected := []string{"Amazonas", "Pará", "Mato Grosso", "Minas Gerais", "Bahia", "Mato Grosso do Sul", "Goiás", "Maranhão", "Rio Grande do Sul", "Tocantins"}
	assert.Equal(t, expected, estados)
}
   
```
    
Enquanto o primeiro teste possui *asserts* mais simples (por exemplo: o resultado deve ser uma lista de strings de tamanho 10) neste caso temos *asserts* mais complexos (por exemplo: o resultado deve ser uma lista de strings cujo primeiro item tenha o valor Amazonas).

Caso o cálculo da nota precise ser realizado de uma maneira mais complexa do que testes unitários, como no exemplo acima, basta que o arquivo faça o processamento e imprima na saída padrão a nota no formato:

```json
{"score": 99.5}
```

O valor do _score_ deve ser entre 0 e 100

### Os conteúdos

Um dos maiores desafios de um iniciante é conseguir fazer o filtro da enorme quantidade de conteúdo existente e identificar o que é relevante. Para resolvermos este problema sempre elencamos uma lista de posts, livros, documentações, videos, entre outros materiais, que ajudarão o(a) desenvolvedor(a) a resolver o desafio.

### O template

Para facilitar o processo de criação de desafios nós criamos um [repositório no Github](https://github.com/thecodenation/desafios/tree/master/templates) com templates para as principais linguagens de programação. O repositório é *open source*, por isso você pode colaborar com novos templates.

#### O arquivo challenge.json

No arquivo _challenge.json_ constam os metadados do desafio. Nele estão os detalhes como os comandos que serão executados, os arquivos que serão enviados para a API no momento da submissão e os conteúdos indicados. Exemplo:

```json
{
    "name": "Teste básico de Golang",
    "description": "Listar os dez maiores estados brasileiros em extensão territorial",
    "topic":["Go", "Testes unitários"],
    "slug": "go-0",
    "test_cmd": [
        "go get -u github.com/stretchr/testify/assert",
        "go test"
    ],
    "test_results_files": ["output.xml"],
    "submission_files":[
        "main.go",
        "main_test.go",
        "submit_test.go",
        "output.xml"
    ],
    "private_files": [
        "submit_test.go"
    ],
    "submission_cmd": [
        "go get -u github.com/jstemmer/go-junit-report",
        "go test -v | go-junit-report > output.xml"
    ],
    "created_by": [
        {
            "name": "Code:Nation",
            "picture": "https://www.codenation.com.br/image/ta-cn-symbol@3x.png",
            "email": "atendimento@codenation.com.br",
            "linkedin": "https://www.linkedin.com/company/code-nation/",
            "github": "http://github.com/thecodenation",
            "site": "https://www.codenation.com.br"
        }
    ],
    "content": [
        {
            "name": "The Go Programming Language",
            "description": "Documentation - The Go Programming Language",
            "url": "https://golang.org/doc/"
        },
        {
            "name": "A Tour of Go",
            "description": "A Tour of Go",
            "url": "https://tour.golang.org/welcome/1"
        },
        {
            "name": "Go by Example",
            "description": "Go by Example is a hands-on introduction to Go using annotated example programs",
            "url": "https://gobyexample.com/"
        },
        {
            "name": "stretchr/testify",
            "description": "A toolkit with common assertions and mocks that plays nicely with the standard library",
            "url": "https://github.com/stretchr/testify"
        },
        {
            "name": "A Linguagem de Programação Go - Novatec Editora",
            "description": "Este livro é uma referência definitiva para programadores que queiram conhecer a linguagem Go",
            "url": "https://novatec.com.br/livros/linguagem-de-programacao-go/"
        }
    ]
}
```

**OBS:** 

- no campo *test_cmd* indicamos o comando que será executado na máquina do desenvolvedor para que ele possa validar o seu código com os testes unitários fornecidos

- no campo *submission_cmd* é necessário que o comando gere o arquivo _output.xml_, conforme indicado no campo *test_results_files*, pois este será analisado durante o processo de avaliação, caso a nota seja calculada de acordo com os testes unitários.

- no campo *private_files* é necessário indicar quais arquivos serão excluídos da máquina do desenvolvedor após a correção e submissão para a API. Estes arquivos geralmente são usados apenas para o cálculo da nota e depois apagados, para garantir a lisura do processo.

- no campo *test_results_files* indicamos qual é o nome dos arquivos que armazenam o resultado dos testes, a serem processados para o cálculo da nota. Caso a nota seja calculada por outro algoritmo este campo não é necessário

- no campo *content* indicamos os conteúdos relacionados ao desafio.

## Como começar?  

Se você tem interesse em nos ajudar com a criação de templates basta abrir uma *issue/pull request* no [repositório de templates](https://github.com/thecodenation/desafios/tree/master/templates).

E, caso queira criar um desafio entre em contato conosco pelo e-mail _elton.minetto@codenation.com.br_ ou [Twitter](http://twitter.com/CodeNationBr)/[Facebook](https://www.facebook.com/CodenationFL)/[Linkedin](https://www.linkedin.com/company/code-nation).



