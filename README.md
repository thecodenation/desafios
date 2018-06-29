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

## Requisitos

Para este desafio você precisará do Go versão 1.9 (ou superior) e o gerenciador de dependências dep. Para instalar as dependências, você pode utilizar os comandos abaixo:

    go get -u github.com/golang/dep/cmd/dep
    cd ~/codenation/golang-1
    dep ensure


```

OBS: este conteúdo vai ser salvo no arquivo _README.md_, então é possível usar markdown.

### O teste

Um dos tópicos mais importantes que o(a) desenvolvedor(a) precisa internalizar é o conceito de  *TDD* (*Test Driven Development*) - a abordagem da Code:Nation é fortemente baseada nesta crença.

Quando o(a) desenvolvedor(a) inicia o desafio utilizando o [codenation-cli](https://www.youtube.com/watch?v=Bmwpq8cjXso), recebe na sua máquina um diretório com uma estrutura similar a:

```
README.md: detalhes sobre o desafio e o que você precisa instalar na sua máquina para o desenvolvimento
main.go: é neste arquivo que você deve ser resolvido o desafio
main_test.go: testes unitários para auxiliá-lo no desenvolvimento. Este arquivo não deve ser alterado!
```

O exemplo acima mostra os arquivos de um desafio na linguagem *Go*, mas o mesmo conceito é aplicado a qualquer ambiente: uma suite de testes que o desenvolvedor usará para guiar seu desenvolvimento. Neste caso, o _main.go_ é um "esqueleto" que o desenvolvedor usará para desenvolver.

Exemplo do esqueleto *main.go*:

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

Exemplo do conteúdo do arquivo de testes, o *main_test.go*:

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

Quando o(a) desenvolvedor(a) entender que sua solução está pronta poderá submetê-la para avaliação. Para isso, executará o comando do [codenation-cli](https://www.youtube.com/watch?v=Bmwpq8cjXso) e um arquivo de testes especial é executado para que a nota seja calculada. A ideia é que o(a) desenvolvedor(a) não possa ver este arquivo - ele é executado apenas no momento da submissão e possui testes mais avançados para validarmos seu conhecimento. Exemplo de um arquivo de testes para este fim, o *submit_test.go*:

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

Um dos maiores desafios de um iniciante é conseguir fazer o filtro da enorme quantidade de conteúdo existente e identificar o que é relevante. Para resolvermos este problema sempre elencamos uma lista de posts, livros, documentações, videos, entre outros materiais, que ajudarão o(a) desenvolvedor(a) a resolver o desafio. Exemplos:

```
Introduction to Linux
https://www.edx.org/course/introduction-linux-linuxfoundationx-lfs101x-1
Develop a good working knowledge of Linux using both the graphical interface and command line, covering the major Linux distribution families

An Introduction to API’s
https://restful.io/an-introduction-to-api-s-cee90581ca1b
An Introduction to API’s

```

### O template

Para facilitar o processo de criação de desafios nós criamos um [repositório no Github](https://github.com/thecodenation/desafios/tree/master/templates) com templates para as principais linguagens de programação. O repositório é *open source*, por isso você pode colaborar com novos templates.

## Como começar?  

Se você tem interesse em nos ajudar com a criação de templates basta abrir uma *issue/pull request* no [repositório de templates](https://github.com/thecodenation/desafios/tree/master/templates).

E, caso queira criar um desafio entre em contato conosco pelo e-mail _elton.minetto@codenation.com.br_ ou [Twitter](http://twitter.com/CodeNationBr)/[Facebook](https://www.facebook.com/CodenationFL)/[Linkedin](https://www.linkedin.com/company/code-nation).



