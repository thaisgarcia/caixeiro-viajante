from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from itertools import permutations
import time

def obter_quilometragem(driver):
    quilometragem = None
    try:
        # Espera até que o elemento de quilometragem seja carregado
        quilometragem_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.ivN21e.tUEI8e.fontBodyMedium"))
        )
        quilometragem = quilometragem_element.text
    except Exception as e:
        print("Erro ao obter quilometragem:", e)
    return quilometragem


def obter_info_google_maps(driver, origem, destinos):
    driver.get("https://www.google.com/maps")

    # Clicar no botão de Rotas
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[@aria-label='Rotas']"))
    ).click()

    time.sleep(3)

    # Preencher o ponto de partida
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "input[aria-label='Escolher ponto de partida ou clicar no mapa...']"))
    ).send_keys(origem, Keys.ENTER)

    time.sleep(3)  # Esperar um pouco após inserir a origem

    for destino in destinos:
        # Preencher cada destino
        try:
            destino_input = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "input[aria-label='Informe o destino ou clique no mapa…']"))
            )
            destino_input.send_keys(destino, Keys.ENTER)

            time.sleep(3)  # Esperar um pouco após inserir cada destino

            # Clicar em "Adicionar destino" se não for o último destino
            if destino != destinos[-1]:
                WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, ".fC7rrc.xiw3Pd"))
                ).click()

            time.sleep(5)  # Esperar um pouco após clicar em "Adicionar destino"

        except Exception as e:
            print(f"Erro ao inserir destino {destino}: {e}")

    return obter_quilometragem(driver)


def caixeiro_viajante(origem, destinos):
    driver = webdriver.Edge()
    try:
        melhores_rotas = None
        menor_quilometragem = float('inf')

        for perm in permutations(destinos):
            perm_destinos = list(perm) + [origem]
            quilometragem = obter_info_google_maps(driver, origem, perm_destinos)

            if quilometragem:
                quilometragem_valor = float(quilometragem.replace(" km", "").replace(",", "."))

                if quilometragem_valor < menor_quilometragem:
                    menor_quilometragem = quilometragem_valor
                    melhores_rotas = perm_destinos

    except Exception as e:
        print("Erro:", e)

    finally:
        driver.quit()

    return melhores_rotas, menor_quilometragem

# Entrada dos dados
origem = input("Digite o endereço de origem: ")
quantidade_destinos = int(input("Informe a quantidade de destinos: "))
destinos = [input(f"Digite o {i+1}º endereço de destino: ") for i in range(quantidade_destinos)]

# Executar o caixeiro viajante
rota, quilometragem = caixeiro_viajante(origem, destinos)

# Saída dos resultados
if rota is not None:
    print(f"Melhor rota de {origem}: {origem} -> " + " -> ".join(rota))
    print("Menor quilometragem:", quilometragem, "km")
else:
    print(f"Não foi possível calcular a rota de {origem}.")
