# import pyautogui
# import time

# time.sleep(7)
# print (pyautogui.position())

import pandas as pd
tabela = pd.read_csv("C:\Program Files\ARQUIVOS DO CURSO DE PROGRAMAÇÃO NUNCA APAGAR\ARQUIVOS DO CURSO DE  PHYTON HASHTAG\python\AULA - 1\PROJETO - 1\produtos.csv")

print(tabela.to_string(index=True))


