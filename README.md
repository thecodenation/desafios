# Criando desafios na Code:Nation

## O que?

Na Code:Nation acreditamos que a melhor forma de aprender uma nova tecnologia, linguagem ou mesmo uma nova carreira é através de desafios práticos. É o chamado _"challenge based learning"_, onde a pessoa é apresentada a desafios práticos que vão ajudá-la a aprender os principais tópicos necessários para a sua evolução.

## Por que contribuir criando desafios?

Lembra quando você iniciou na carreira que está atuando hoje? A angústia de não saber o que estudar primeiro? A lista interminável e assustadora de links, livros, siglas, tudo isso para começar a entender o básico? O quão frustrante isso pode ser? É esse sentimento que queremos mudar com a Code:Nation e você, já passou por isso, pode nos ajudar a mudar esse cenário. 


## Como criar um desafio?

Uma boa forma de iniciar o processo de criação é pensar nos conteúdos que o desafio vai ensinar para o desenvolvedor. Exemplo: Ao completar este desafio a pessoa terá aprendido o básico de Python, manipulação de listas e dicionários, como ler um arquivo CSV.

### O título

Tudo começa com um bom título. Algo que vai chamar a atenção do desenvolvedor(a) e convencer a clicar no desafio. Exemplos:  "Média do ENEM", "Melhor nota de matemática do ENEM"

### A descrição

Aqui é onde descrevemos o desafio em si, qual seus objetivos, quais resultados são esperados. Exemplo:

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

### O teste

Um dos tópicos mais importantes que o desenvolvedor precisa internalizar é o conceito de TDD (Test Driven Development) e a abordagem da Code:Nation é fortemente baseada nesta crença. 
Quando o desenvolvedor inicia o desafio ele, usando o codenation-cli (link para o video explicando como usar) ele recebe, na sua máquina um diretório com uma estrutura similar a:

```
README.md: detalhes sobre o desafio e o que você precisa instalar na sua máquina para o desenvolvimento
main.go: é neste arquivo que você deve resolver o desafio
main_test.go: testes unitários para auxiliá-lo no desenvolvimento. Você não deve alterar este arquivo!
```

O exemplo acima mostra os arquivos de um desafio na linguagem Go, mas o mesmo conceito é aplicado a qualquer ambiente: uma suite de testes que o desenvolvedor vai usar para guiar seu desenvolvimento. Neste caso, o main.go é um "esqueleto" que o desenvolvedor vai usar para desenvolver. 

Exemplo do esqueleto main.go:

```
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

Exemplo do conteúdo do arquivo de testes:

```
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

Quando o desenvolvedor entender que sua solução está pronta ele pode submetê-la para avaliação. Para isso ele executa o comando  do codenation-cli (link para o video) e um arquivo de testes especial é executado para que a nota seja calculada. A ideia é que o desenvolvedor não possa ver este arquivo, ele é executado apenas no momento da submissão e possui testes mais avançados, para validarmos o conhecimento. Exemplo de um arquivo de testes para este fim, o submit_test.go:

```
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
    
Enquanto o primeiro teste possui asserts mais simples (por exemplo: o resultado deve ser uma lista de strings de tamanho 10) neste caso temos asserts mais complexas (por exemplo: o resultado deve ser uma lista de strings cujo primeiro item tenha o valor Amazonas).

### Os conteúdos

Um dos maiores desafios de um iniciante é conseguir fazer o filtro da enorme quantidade de conteúdo existente e identificar o que é relevante. Para resolvermos este problema sempre elencamos uma lista de posts, livros, documentações, videos, etc, que vão ajudar o desenvolvedor a resolver o desafio. Exemplos:

```
Introduction to Linux
https://www.edx.org/course/introduction-linux-linuxfoundationx-lfs101x-1
Develop a good working knowledge of Linux using both the graphical interface and command line, covering the major Linux distribution families

An Introduction to API’s
https://restful.io/an-introduction-to-api-s-cee90581ca1b
An Introduction to API’s

```

### O template

Para facilitar o processo de criação de desafios nós criamos um [repositório no Github](https://github.com/thecodenation/desafios/tree/master/templates) com templates para as principais linguagens de programação. O repositório é open source por isso você pode colaborar com novos templates.

## Como começar?  

Se você tem interesse em nos ajudar com a criação de templates basta abrir uma issue/pull request no [repositório de templates](https://github.com/thecodenation/desafios/tree/master/templates).

E caso queira criar um desafio por favor entre em contato conosco pelo e-mail (link) ou Twitter/Facebook/Linkedin



