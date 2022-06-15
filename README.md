# HousesNear
Aprendendo Webscraping, DataScience, Deploy e gerenciamentod e projetos.

- [Sobre](#sobre)
- [Setup e Requisitos](#setup-e-requisitos)
- [WebScraping](#webscraping)
- [Dados](#dados)
- [Treinamento](#treinamento)
- [Deploy](#deploy)
- [Conclusão](#conclusao)

## Sobre
Esse projeto tem como principal objetivo o aprendizado e fixação de todos os items acima.
Sobre o projeto em sí, em um primeiro momento vamos usar dados adquiridos por meio de Webscraping de casas, como tamanho, número de quartos, vagas de garagem, preço, ...
Todos esses dados a principio serão armazenados no AWS S3, para um acesso mais facil por todos que participarão do projeto.
Com esses dados vamos treinar um modelo de machine learning para tentar prever e preço de casa com base em suas caracteristicas.
Por fim é feito o deploy do modelo em uma página web bem como em um aplicativo para celular.

Uma segunda parte do projeto é usar a API do Google Maps para que com base em um endereço escolhido pelo usuário juntamente com um raio de interesse consigamos mostrar todos os comercios ou pontos de interesse dentro desse raio.

## Setup e Requisitos
Linguagens:

* Python
* SQL
* HTML
* CSS
* JavaScript

Várias libs serão utilizadas:

* Pandas
* Numby
* Matplotlib
* SQLalchemy
* Scikit-learn
* Selenium
* Kivy

E ferramentas:

* Visual Studio Code
* PyCharm
* Anaconda

## WebScraping
Usaremos selenium para fazer webscraping dos dados e serão todos adquiridos através do site de imóvies Viva Real:

- [Viva Real](https://www.vivareal.com.br/venda/sp/sao-paulo/apartamento_residencial/)

Todos os dados serão da cidade de São Paulo e vamos considerar somente imóveis que estão a venda.
Todas as informações que estão presentes no anuncio serão adquiridas como preço, tamanho, númeto de quartos, número de banheiros, endereço, se tem elevador, .... .

## Dados
Após conseguirmos os dados iremos armazena los usando um serviço cloud.
A idéia de usar um serviço na cloud é para facilitar o acesso de todos que estão trabalhando no projeto.
Serão criadas tabelas dentro do Amazon AWS S3 onde cada uma terá dados cada vez mais limpos e prontos para serem utilizados.
Serão 4 tabelas ou 4 camadas:

* Camada RAW
* Camada BRONZE
* Camada SILVER
* Camada GOLD

Iniciando pela camada RAW onde os dados estão da maneira que foram adquiridos via webscraping até a camada GOLD onde eles estão prontos para serem consumidos.

## PEP 8
Vamos seguir o padrão PEP 8 para boas práticas de escrita de código:
- https://peps.python.org/pep-0008/

## Treinamento

## Deploy

## Conclusão
