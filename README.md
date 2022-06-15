# HousesNear
Aprendendo Webscraping, DataScience, Deploy e gerenciamentod e projetos.

- [Sobre](#sobre)
- [Setup e Requisitos](#setup-e-requisitos)
- [WebScraping](#webscraping)
- [Dados](#dados)
- [PEP8](#pep8)
- [Treinamento](#treinamento)
- [Deploy](#deploy)
- [Conclusão](#conclusao)

## Sobre
Esse projeto tem como principal objetivo o aprendizado e fixação de todos os items acima.<br />
Sobre o projeto em sí, em um primeiro momento vamos usar dados adquiridos por meio de Webscraping de casas, como tamanho, número de quartos, vagas de garagem, preço, ... <br />
Todos esses dados a principio serão armazenados localmente. Futuramente usaremos o AWS S3 para um acesso mais fácil e também para centralizar o acesso.
Com esses dados vamos treinar um modelo de machine learning para tentar prever e preço de casas com base em suas características. <br />
Por fim é feito o deploy do modelo em uma página web bem como em um aplicativo para celular.

Uma segunda parte do projeto é usar a API do Google Maps para que com base em um endereço escolhido pelo usuário juntamente com um raio de interesse consigamos mostrar todos os comércios ou pontos de interesse dentro desse raio.

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

Todos os dados serão da cidade de São Paulo e vamos considerar somente imóveis que estão a venda.<br />
Todas as informações que estão presentes no anuncio serão adquiridas como preço, tamanho, número de quartos, número de banheiros, endereço, se tem elevador, .... .

## Dados
Após conseguirmos os dados iremos armazena los localmente e futuramente migrar os dados para uma plataforma cloud.<br />
A idéia de usar um serviço em cloud é para facilitar e centralizar o acesso.<br />
Serão criadas tabelas dentro do Amazon AWS S3 onde cada uma terá dados cada vez mais limpos e prontos para serem utilizados.<br />
Serão 4 tabelas ou 4 camadas:

* Camada RAW
* Camada BRONZE
* Camada SILVER
* Camada GOLD

Iniciando pela camada RAW onde os dados estão da maneira que foram adquiridos via webscraping até a camada GOLD onde eles estão prontos para serem consumidos.

## PEP8
Vamos seguir o padrão PEP 8 para boas práticas de escrita de código:
- https://peps.python.org/pep-0008/

## Treinamento

## Deploy

## Conclusão
