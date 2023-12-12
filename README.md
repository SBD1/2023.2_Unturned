# 2023.2_Unturned

<p align="center">
  <img src="assets/unturned.jpg" alt="Unturned">
</p>

## Sobre o Projeto

Este repositório é dedicado ao desenvolvimento de trabalhos para a disciplina de Sistemas de Banco de Dados 1. O jogo base escolhido para aplicação dos conceitos é o _Unturned_, um jogo de sobrevivência em mundo aberto com temática de apocalipse zumbi. O objetivo é explorar como os sistemas de banco de dados podem ser integrados e utilizados em um ambiente de jogo.

# Pré-requisitos

* psycopg2
* docker compose
* python3

## Como executar ?

* Fazer o build o docker compose (somente a primeira vez)
```shell
docker compose up --build
```

* Se já fez o build uma vez, basta executar
```shell
docker compose up 
```

* Pegue o ip do localhost do container e nos arquivos ./src/game.py e ./src/adventures/russia.py cole no host do psycopg2
```shell
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' 20232_unturned-postgres-1
```

* Agora no diretório de ./src
```shell
python3 game.py
```

## Integrantes do Grupo

| **Matrícula** | **Nome**                        | **Foto**                                                                                                   |
| ------------- | ------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| 200057421     | Delziron Braz de Lima           | <img src="https://avatars.githubusercontent.com/DelzironBraz" width="75px;" alt="Foto Delziron"/>          |
| 200017519     | Eurico Menezes de Abreu Neto    | <img src="https://avatars.githubusercontent.com/EuricoAbreu" width="75px;" alt="Foto Eurico"/>             |
| 200067923     | João Henrique Marques Calzavara | <img src="https://avatars.githubusercontent.com/u/71076129?v=4" width="75px;" alt="Foto João Henrique"/>   |
| 200062379     | Marcos Vinícius de Deus         | <img src="https://avatars.githubusercontent.com/u/87666623?v=4" width="75px;" alt="Foto Marcos Vinicius"/> |

## Apresentações

- [**Módulo 1:** Apresentação no SharePoint](https://unbbr.sharepoint.com/:v:/s/Bancos1/EYwxobRqXIZKoffKm-LGR9QBVNREMPZuQ3zBR8UXwwaQcg?e=eVV8i8&nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJTdHJlYW1XZWJBcHAiLCJyZWZlcnJhbFZpZXciOiJTaGFyZURpYWxvZyIsInJlZmVycmFsQXBwUGxhdGZvcm0iOiJXZWIiLCJyZWZlcnJhbE1vZGUiOiJ2aWV3In19) ou [Vídeo no Diretório](docs/apresentacoes)
- [**Módulo 2:** Vídeo no YouTube](https://youtu.be/djW7gptqLoQ)
- [**Módulo 3:** Vídeo no YouTube](https://youtu.be/L42dy9sB3yw)

## Entregas por Módulo

### Módulo 1

- [Diagrama Entidade-Relacionamento (DER)](docs/DER.md)
- [Modelo Relacional (MR)](docs/MR.md)
- [Dicionário de Dados](docs/DicionarioDeDados.md)

### Módulo 2

- [Linguagem de Definição de Dados (DDL)](sql/DDL.sql)
- [Linguagem de Manipulação de Dados (DML)](sql/DML.sql)
- [Linguagem de Consulta de Dados (DQL)](sql/DQL.sql)

### Módulo 3

- [Triggers e Procedures](sql/Trigger_Storage_Procedure.sql)
- [Implementação Parcial do Jogo](src/adventures/russia.py)
