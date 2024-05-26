# Problema do Caixeiro Viajante (PCV)

Como parte da disciplina de Estrutura de Dados no meu curso da faculdade, desenvolvi um projeto que combina automação web com algoritmos de otimização de rotas para resolver o problema do caixeiro viajante. Utilizei Python, Selenium e Google Maps para encontrar a rota mais eficiente entre vários destinos.
<br>

## Descrição do Projeto

O objetivo deste projeto é encontrar a rota mais eficiente entre vários destinos, começando de uma origem especificada. O algoritmo de permutações é utilizado para testar todas as combinações possíveis de destinos, garantindo a rota mais curta.
<br><br>

![image](https://github.com/thaisgarcia/caixeiro-viajante/assets/95317220/3db3640f-4c28-4a9f-a9b6-a6e6e656d7b8)

## Requisitos
- Python 3.12 ou superior
- Selenium
- WebDriver para o navegador utilizado (Edge, Chrome, Firefox, etc.)
- Conexão estável com a internet

## Instalação

1. Clone o repositório para o seu computador:
    ```bash
    git clone https://github.com/seu-usuario/nome-do-repositorio.git
    cd nome-do-repositorio
    ```

2. Instale as dependências necessárias:
    ```bash
    pip install selenium
    ```

3. Baixe o WebDriver compatível com a versão do seu navegador e adicione-o ao PATH do seu sistema. Por exemplo, se estiver usando o Edge, baixe o Microsoft Edge WebDriver [aqui](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/).

## Uso

1. Execute o script Python:
    ```bash
    python seu_script.py
    ```

2. Siga as instruções para inserir a origem e os destinos:
    ```text
    Digite o endereço de origem:
    Informe a quantidade de destinos:
    Digite o 1º endereço de destino:
    Digite o 2º endereço de destino:
    ...
    ```

3. O script calculará a rota mais curta e exibirá os resultados:
    ```text
    Melhor rota: Origem -> Destino 1 -> Destino 2 -> ... -> Origem
    Menor quilometragem: X km
    ```
