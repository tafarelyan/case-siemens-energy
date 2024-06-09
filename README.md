## Execução da aplicação
Para rodar a aplicação, execute o comando abaixo
``` bash
docker-compose up --build
```

Obs: Existe a possibilidade do serviço consumidor não funcionar devido ao tempo de inicialização do kafka, então caso o serviço não iniciar, execute o seguinte comando
```bash
docker-compose run consumer
```

### E se eu quiser ter múltiplas partições no meu tópico?
Para ter múltiplas partições no tópico específico, só pode ser criado o tópico pelo Kafka, não há possibilidades de criar o tópico com múltiplas partições no produtor ou no consumidor, podemos utilizar o seguinte comando
```bash
docker-compose exec kafka kafka-topics --create --topic siemens_energy --partitions 3 --bootstrap-server kafka:9092
```