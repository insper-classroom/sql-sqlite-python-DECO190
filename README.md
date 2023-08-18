# ProjÁgil - 2023

Material de apoio sobre SQL: https://www.devmedia.com.br/guia/guia-completo-de-sql/38314

### Exercício 1: SQL

Iremos utilizar a plataforma https://sqliteonline.com/ para treinar comandos SQL básicos. O arquivo que usaremos é "vgsales_pbi.csv" que pode ser baixado no link https://drive.google.com/file/d/1fhcUzrJau2w5zcQ1B3wpKhOv9mWet0xR/view?usp=sharing.

1. **Jogos da plataforma Xbox One**:
   - **Enunciado**: Liste todos os jogos disponíveis para a plataforma Xbox One. (copie e cole o comando e as 5 primeiras linhas do resultado aqui)
   - **Query**:
     ```sql
      
     ```
   - **Resultado**
    


2. **Jogos de Ação após 2010**:
   - **Enunciado**: Liste todos os jogos do gênero "Ação" que foram lançados após 2010.  (copie e cole o comando e as 5 primeiras linhas do resultado aqui)
   - **Query**:
     ```sql
      
     ```
   - **Resultado**
    


3. **Jogos mais recentes**:
   - **Enunciado**: Liste os 5 jogos mais recentes lançados.  (copie e cole o comando e as 5 primeiras linhas do resultado aqui)
   - **Query**:
     ```sql
      
     ```
   - **Resultado**
    


4. **Jogos mais antigos**:
   - **Enunciado**: Liste os 5 jogos mais antigos.  (copie e cole o comando e as 5 primeiras linhas do resultado aqui)
   - **Query**:
     ```sql
      
     ```
   - **Resultado**
    


5. **Jogos de Aventura com mais vendas na América do Norte**:
   - **Enunciado**: Quais são os 3 jogos do gênero "Aventura" com as maiores vendas na América do Norte?  (copie e cole o comando e as 5 primeiras linhas do resultado aqui)
   - **Query**:
     ```sql
      
     ```
   - **Resultado**
    


	 
6. **Jogos de RPG ou Estratégia lançados após 2005**:
   - **Enunciado**: Liste todos os jogos dos gêneros "RPG" ou "Strategy" lançados após 2005.  (copie e cole o comando e as 5 primeiras linhas do resultado aqui)
   - **Query**:
     ```sql
      
     ```
   - **Resultado**
    



### Exercício 2: Python - Sqlite

Objetivo: Familiarizar-se com os comandos básicos de SQL e aprender a filtrar registros usando o comando WHERE.

Crie uma tabela chamada "Estudantes" com os seguintes campos:

- **ID (chave primária)**
- **Nome**
- **Curso**
- **Ano de Ingresso**

Insira 5 registros de estudantes na tabela. Inclua os seguintes estudantes fictícios como parte desses registros:

- Ana Silva, Computação, Ano de Ingresso: 2019
- Pedro Mendes, Física, Ano de Ingresso: 2021
- Carla Souza, Computação, Ano de Ingresso: 2020
- João Alves, Matemática, Ano de Ingresso: 2018
- Maria Oliveira, Química, Ano de Ingresso: 2022
 
**Selecione e mostre todos os registros da tabela no console.**

- Filtre e mostre os estudantes que ingressaram entre 2019 e 2020 (inclusive) e exiba no console. Use o comando WHERE para realizar essa filtragem.

- Atualize o "Ano de Ingresso" de um estudante específico. Mostre por todos estudantes novamente.

- Delete um registro da tabela usando o ID do estudante. Mostre por todos estudantes novamente.

- Filtre e mostre os estudantes do Curso de Computação que ingressaram após 2019. Mostre o resultado.

- Imagine que alguém errou nos registros de ingresso de todos os alunos do curso de Computação, crie uma query que altere todos os registros dos alunos de Computação, campo ingresso para 2018. Mostre por todos estudantes novamente.




### Exercicio 3: Python - SQLite

**Exercício de Reaproveitamento e Organização de Código**

A medida que os sistemas crescem e se tornam mais complexos, a necessidade de manter o código organizado e reutilizável torna-se cada vez mais evidente. Manter funções comuns em módulos separados não apenas torna seu código mais legível, mas também permite que você reutilize funções sem duplicar o código. Isso reduz o risco de erros, facilita a manutenção e economiza tempo no longo prazo.

Considere o arquivo `main_1.py` que vocês trabalharam anteriormente. Nele, várias operações relacionadas ao banco de dados foram realizadas. Estas operações são comuns em muitas aplicações e podem ser reutilizadas em diversos contextos.

**Tarefa:** 

1. Crie um arquivo chamado `db_utils.py` dentro da pasta `db`.
2. Crie funções mais comuns relacionadas ao banco de dados para este novo arquivo. Por exemplo, funções para criar tabelas, inserir registros, consultar registros, atualizar e deletar.
3. No `main_2.py`, importe e utilize as funções do arquivo `db_utils.py` para realizar as operações do Exercício 2.

**Dica:** Ao organizar seu código desta maneira, você estará aplicando o princípio DRY (Don't Repeat Yourself) do desenvolvimento de software, que visa reduzir a repetição de informações de todos os tipos.