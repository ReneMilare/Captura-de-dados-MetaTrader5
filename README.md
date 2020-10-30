# Captura-de-dados-MetaTrader5
Script em Python que faz a captura de dados dos pregões do MetaTrader5.

Para rodar o script no PowerShell por exemplo, basta digitar:

**> python captura_de_dados_metatrader5.py**

Em seguida é só informar o nome do ativo e quantidade de pregões que deseja, digite -1 para capturar o máximo de pregões possível.
Os dados são salvos em .csv

## DICA

No MetaTrader5, em Ferramentas depois Opções, ou utilizndo a tecla de atalho Ctrl+O.
Vá para a aba Gráficos e em: Máx. barras no gráfico, altere para **Unlimited**.
Com isso, quando você utilizar o parâmetro -1 para o máximo de pregões possível, o MetaTrader irá te devolver realmente o máximo.

Segue imagem com a alteração para Unlimited e dos dados capturados.

![image](https://user-images.githubusercontent.com/24875841/97712438-31a4be80-1a9d-11eb-919d-82309b7e3aaa.png)

![image](https://user-images.githubusercontent.com/24875841/97712850-c5768a80-1a9d-11eb-85a6-3780fe23bdae.png)

![image](https://user-images.githubusercontent.com/24875841/97712940-e63ee000-1a9d-11eb-9627-6d8816e0aa61.png)
