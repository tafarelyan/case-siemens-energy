Para rodar a aplicação, execute o comando abaixo
``` bash
docker-compose up --build
```

Obs: Existe a possibilidade do serviço consumidor não funcionar devido ao tempo de inicialização do kafka, então caso o serviço não iniciar, execute o seguinte comando
```bash
docker-compose run consumer
```