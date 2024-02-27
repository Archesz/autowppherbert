import pyautogui
import pandas as pd
import time

df = pd.read_csv("alunos.csv", sep=";")
screenWidth, screenHeight = pyautogui.size()

pyautogui.hotkey('alt', 'tab')

# Abrir o Whatsapp Web
pyautogui.moveTo(22, 440)
pyautogui.click()

nomes = list(df["Nome"])

for i, tel in enumerate(list(df["Telefone"])):

    # Clicar em começar nova conversa
    pyautogui.moveTo(365, 77)
    pyautogui.click()
    telefone = tel
    nome = nomes[i]

    pyautogui.typewrite(f"{telefone}", interval=0.01)

    # Selecionando contato
    pyautogui.moveTo(186, 375)
    pyautogui.click()

    # Digitando mensagem
    time.sleep(1)
    mensagem = f"Bom dia {nome}! Somos do projeto Herbert de Souza, vimos que foi declarado interesse de sua parte pelo projeto, no entanto, nao foi efetuada a matricula. Gostariamos de saber se pretende efetuar! Caso sim, fique a vontade para tirar duvidas."
    pyautogui.typewrite(mensagem, interval=0.01)

    pyautogui.hotkey("enter")

    print(i, nome, telefone)
