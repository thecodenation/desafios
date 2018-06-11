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
Para este desafio você precisará de python 3.6 (ou superior) e a biblioteca pandas. Para instalar as dependências, você pode utilizar o arquivo requirements.txt presente neste diretório.

Utilizando a função pd.read_csv, carregue o arquivo train.csv para um DataFrame do pandas mantendo os valores como str (dica: argumento dtype em pd.read_csv). A saída da sua função deverá ser um pd.DataFrame de tamanho (2,2) cujas linhas são as duas primeiras de train.csv e as colunas "NU_INSCRICAO", "NU_IDADE".

Calcule a média da idade dos alunos (dica: utilze .astype para converter o tipo da coluna)

Normalize a coluna "NU_IDADE" removendo a média e dividindo todos os valores pelo desvio padrão da mesma.

Calcule a média das notas de matemática (coluna "NU_NOTA_MT") para cada valor em "NO_MUNICIPIO_ESC". Garanta que o resultado final tenha apenas os 10 municipios com maior média (dica: .groupby e .nlargest)

Converta o tipo das colunas "NU_NOTA_CN", "NU_NOTA_CH", "NU_NOTA_LC", "NU_NOTA_MT" e "NU_NOTA_REDACAO" para float. Crie uma coluna nova "NU_NOTA_MEDIA" no dataframe cujos valores são a média das colunas anteriores. Caso exista valores faltantes (NaN) preencha com zeros utilizando a função .fillna.

Utilize a função "groupby" para contar a quantidade de alunos por idade.
```

### O teste

Um dos tópicos mais importantes que o desenvolvedor precisa internalizar é o conceito de TDD (Test Driven Development) e a abordagem da Code:Nation é fortemente baseada nesta crença. 
Quando o desenvolvedor inicia o desafio ele, usando o codenation-cli (link para o video explicando como usar) ele recebe, na sua máquina um diretório com uma estrutura similar a:

```
README.md: detalhes sobre o desafio e o que você precisa instalar na sua máquina para o desenvolvimento
main.py: é neste arquivo que você deve resolver o desafio
main_test.py: testes unitários para auxiliá-lo no desenvolvimento. Você não deve alterar este arquivo!
```

O exemplo acima mostra os arquivos de um desafio na linguagem Python, mas o mesmo conceito é aplicado a qualquer ambiente: uma suite de testes que o desenvolvedor vai usar para guiar seu desenvolvimento. Neste caso, o main.py é um "esqueleto" que o desenvolvedor vai usar para desenvolver. 

Exemplo do conteúdo do arquivo de testes:

```
import pandas as pd
from main import (
    part_1,
    part_2,
    part_3,
    part_4,
    part_5,
    part_6,
    part_7,
    part_8,
    part_9,
    part_10,
)


def test_part_1():
    df = part_1()
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (2,2)
    assert set(df.columns) == set(["NU_INSCRICAO", "NU_IDADE"])

def test_part_2():
    assert isinstance(part_2(), float)

def test_part_3():
    s = part_3()
    assert isinstance(s, pd.Series)
    assert s.name == "NU_IDADE"
    assert s.dtype == float

def test_part_4():
    s = part_4()
    assert isinstance(s, pd.Series)
    assert s.name == "NU_NOTA_MT"
    assert s.size == 10

def test_part_5():
    columns = [
        'NU_NOTA_CN',
        'NU_NOTA_CH',
        'NU_NOTA_LC',
        'NU_NOTA_MT',
        'NU_NOTA_REDACAO',
        'NU_NOTA_MEDIA',
    ]

    df = part_5()
    assert (df[columns].dtypes == float).all()
    assert (~df[columns].isnull()).all().all()

def test_part_6():
    assert part_6().dtype == int
```

Exemplo do arquivo main.py:

```
def part_1():
    pass

def part_2():
    pass

def part_3():
    pass

def part_4():
    pass

def part_5():
    pass

def part_6():
    pass

def part_7():
    pass

def part_8():
    pass

def part_9():
    pass

def part_10():
    pass

```


### O cálculo da nota

Quando o desenvolvedor entender que sua solução está pronta ele pode submetê-la para avaliação. Para isso ele executa o comando  do codenation-cli (link para o video) e um arquivo de testes especial é executado para que a nota seja calculada. A ideia é que o desenvolvedor não possa ver este arquivo, ele é executado apenas no momento da submissão e possui testes mais avançados, para validarmos o conhecimento. Exemplo de um arquivo de testes para este fim:

```
import pandas as pd
from main import (
    part_1,
    part_2,
    part_3,
    part_4,
    part_5,
    part_6
)


eq = lambda x: lambda y: x == y

train = pd.read_csv("train.csv", dtype=str)

def test_part_1():
    assert (
        train
        .head(2)
        [["NU_INSCRICAO", "NU_IDADE"]]
        .pipe(eq(part_1()))
        .all()
        .all()
    )

def test_part_2():
    assert (
        train
        ["NU_IDADE"]
        .astype(int)
        .mean()
        == part_2()
    )

def test_part_3():
    assert (
        train
        ["NU_IDADE"]
        .astype(int)
        .pipe(lambda s: (s - s.mean())/s.std())
        .pipe(eq(part_3()))
        .all()
    )

def test_part_4():
    assert (
        train
        .astype({
            "NU_NOTA_MT": float
        })
        .groupby("NO_MUNICIPIO_ESC")
        ["NU_NOTA_MT"]
        .mean()
        .nlargest(10)
        .pipe(eq(part_4()))
        .all()
    )

def test_part_5():
    columns = [
        'NU_NOTA_CN',
        'NU_NOTA_CH',
        'NU_NOTA_LC',
        'NU_NOTA_MT',
        'NU_NOTA_REDACAO'
    ]

    assert (
        train
        .astype({c:float for c in columns})
        .fillna(0)
        .assign(NU_NOTA_MEDIA=lambda df: df[columns].mean(axis=1))
        .pipe(eq(part_5()))
        .all()
        .all()
    )

def test_part_6():
    assert (
        train
        .groupby("NU_IDADE")
        .size()
        .pipe(eq(part_6()))
        .all()
    )    
```
    
Enquanto o primeiro teste possui asserts mais simples (por exemplo: o resultado deve ser uma lista de strings) neste caso temos asserts mais complexas (por exemplo: o resultado deve ser uma lista de strings cujo primeiro item tenha o valor XYZ).

### Os conteúdos

Um dos maiores desafios de um iniciante é conseguir fazer o filtro da enorme quantidade de conteúdo existente e identificar o que é relevante. Para resolvermos este problema sempre elencamos uma lista de posts, livros, documentações, videos, etc, que vão ajudar o desenvolvedor a resolver o desafio. Exemplos:

```
Introduction to Linux
https://www.edx.org/course/introduction-linux-linuxfoundationx-lfs101x-1
Develop a good working knowledge of Linux using both the graphical interface and command line, covering the major Linux distribution families

An Introduction to API’s
https://restful.io/an-introduction-to-api-s-cee90581ca1b
An Introduction to API’s

Pandas From The Ground Up
https://github.com/brandon-rhodes/pycon-pandas-tutorial
The typical Pandas user learns one dataframe method at a time, slowly scraping features together through trial and error until they can solve the task in front of them. In this tutorial you will re-learn how to think about dataframes from the ground up, and discover how to select intelligently from their abilities to solve your data processing problems through direct and deliberately-chosen steps

```

### O template

Para facilitar o processo de criação de desafios nós criamos um [repositório no Github](https://github.com/thecodenation/desafios/tree/master/templates) com templates para as principais linguagens de programação. O repositório é open source por isso você pode colaborar com novos templates.

## Como começar?  

Se você tem interesse em nos ajudar com a criação de templates basta abrir uma issue/pull request no [repositório de templates](https://github.com/thecodenation/desafios/tree/master/templates).

E caso queira criar um desafio por favor entre em contato conosco pelo e-mail (link) ou Twitter/Facebook/Linkedin



