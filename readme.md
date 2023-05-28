## Como rodar este projeto

1. Tenha o docker instalado [install Docker](https://www.docker.com/products/docker-desktop/)
2. Clone este repositório para sua máquina local
```
 git clone git@github.com:aloiziobsc/AerodromoScrapping.git
```
3. Navegue até o diretório do projeto e instale as dependências:
 ```
 cd AerodromoScrapping
```
4. Use o seguinte comando no terminal para criar a imagem do container:
 ```
docker build -t aerodromo-scraping-python .
```
5. Para rodar o container use o comando:
 ```
docker run -it aerodromo-scraping-python
```
6. Para remover a imagem do container use o comando:
 ```
docker run -it --rm aerodromo-scraping-python
```
