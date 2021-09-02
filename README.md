# TrabalhoInformaticaIndustrial
Trabalho de conclusao de periodo
# Etapas:

* Interface Grafica:
  * Representacao da planta;
  * Capacidade de ligar e desligar o motor/esteira principal;
  * Capacidade de alterar frequencia do motor;
  * Capacidade de configurar os filtros do classificador;
  * Visualizacao dos objetos em cada esteira;
  * Grafico em tempo real;
  * Menu de Configuracoes;
  * Acesso a dados historicos.

* Loop:
  * Leitura dos dados;
  * Atualizacao da GUI;
  * Armazenamento de dados Historicos;
  * Sleep;

# Requisitos:
* Monitoramento em tempo real das grandezas do processo (20 pontos):
  * (8 pontos) Comunicação MODBUS com o CLP da planta; (CONEXAO REALIZADA)
  * (5 pontos) Tensão da rede, corrente RMS, potência de entrada, velocidade da esteira, rotação do motor, frequência do inversor, temperatura do estator; (FAZER A LEITURA DOS DADOS)
  * (7 pontos) Gráficos: Cores (RGB) e Peso do objeto.

* Capacidade de atuação no sistema (12 pontos):
  * (2 pontos) Ligar/desligar o processo;
  * (1 pontos) Ligar/desligar o atuador da esteira principal (inserção de novos objetos);
  * (1 pontos) Mudança na frequência de operação do motor;
  * (8 pontos) Mudança nos filtros do Classificador.

* Interface gráfica que represente de forma fidedigna o processo (28 pontos):
  * (8 pontos) Imagem representativa da planta;
  * (7 pontos) Pelo menos uma animação no supervisório (deslocamento do objeto na esteira, classificação, etc);
  * (2 pontos) Menu de configurações;
  * (2 pontos) Mecanismos para atuação no processo (ver item 2);
  * (2 pontos) Separação de telas (monitoramento em tempo real e busca de dados históricos);
  * (7 pontos) Deverá utilizar o framework kivyMD.

* Módulo de busca de dados históricos (15 pontos):
  * (6 pontos) Armazenamento das principais informações do processo;
  * (6 pontos) Permitir a busca de dados históricos das informações do processo;
  * (3 pontos) Deverá ser implementado utilizando a técnica ORM com o SQLAlchemy.
