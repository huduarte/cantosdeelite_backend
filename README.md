1-  virtualenv -p python3  vm
2- cd project && pip install -r requirements.txt

*obs: para gerar pip freeze --local
*obs2: antes do push em nova instância no heroku: heroku config:set DISABLE_COLLECTSTATIC=1
*obs3: rodar heroku run fab dev

ex: 

**list:
http://192.168.1.13:8000/api/pessoa/

**update: 
http://192.168.1.13:8000/api/pessoa/4ed5b488-6d0c-4beb-af68-d15d6f08c67b/


## Utilizando Docker

### Dependências

1) Docker (v17.12.0+)
2) Docker Compose (v1.18.0+)

### Instalação

Faça uma cópia do arquivo `.env.example` para `.env` e altere os dados que achar pertinente, como os dados do banco de dados, endereços de domínio, porta de execução, Django secret_key, entre outras configurações.

Após isso, rode o comando:

```bash
docker-compose build
```

> NOTA: Sempre que houver alterações no requirements.txt ou algum arquivo estrutural como o Dockerfile ou docker-compose.yml, execute novamente o comando build.


### Utilização

Sempre que quiser rodar o projeto, basta executar:

```bash
docker-compose up
```

> NOTA: A primeira vez que o comando é executado pode levar um pouco mais de tempo para a criação dos containers.

Caso queira rodar comandos, como os do `manage.py` do Django, acesse primeiro o shell dentro do container docker, com ajuda do script:

```bash
./docker-shell.sh
```

Dentro do shell, então pode executar os comandos desejados, como `fab dev`, `./manage.py makemigrations`, etc.
