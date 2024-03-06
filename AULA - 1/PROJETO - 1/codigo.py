# Passo a Passo do projeto (Hashtage é comentário no Phyton)

# Passo 1: Entrar no sistema da empresa:
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login
#biblioteca: pyautogui - pip install pyautogui
import pyautogui
import time # Biblioteca TIME.

pyautogui.PAUSE = 0.8 # Tempo de pausa para o phyton conseguir abrir cada operação do phyton. No caso aqui, usamos para dar tempo do navegador abrir tranquilamente e continuar o processo.

# pyautogui.click -> clicar em algum lugar da tela.
# pyautogui.write -> escrever um texto.
# pyautogui.press -> pressionar 1 tecla do teclado.
# pip install pandaspyautogui.hotkey("ctrl", "v")

# abrir o navegador (O que eu escolher)
pyautogui.press("win")
pyautogui.write("Navegador Opera GX")
pyautogui.press("enter")


link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter") # Escreve o link na busca do navegador e aperta enter.

# Dar uma pausa um pouco maior (3 segundos)
pyautogui.sleep(3)


# Passo 2: Fazer login.
pyautogui.click(x=446, y=384)
pyautogui.write("emaildeteste@gmail.com") # Preencher o campo de email (to usando email ficticio)
pyautogui.press("tab") # Para ele pular para o campo da senha.
pyautogui.write('colocara a senha aqui') # Escrever a senha do usuário.
# Clicar em logar
pyautogui.click(x=697, y=543)
time.sleep(3)

# Passo 3: Importar a base de dados. (Ferramenta: Pandas - pip install pandas numpy openpyx1)
import pandas as pd


tabela = pd.read_csv("produtos.csv")

print(tabela)

# Passo 4: Cadastrar 1 produto.
# para cada linha da minha tabela
for linha in tabela.index:
    # clicar no 1º campo
    pyautogui.click(X=414, y=276)
    # Código do Produto
    codigo = tabela.loc[linha, "codigo"]
    # preencher o campo
    pyautogui.write(str(codigo))
     # passar para o proximo campo
    pyautogui.press("tab")
    # Marca do Produto
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    # Tipo de Produto
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    # Categoria do Produto
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    # Preço Unitário do Produto
    pyautogui.write(str(tabela.loc [linha, "preco_unitario"]))
    pyautogui.press("tab")
    # Custo do Produto
    pyautogui.write(str(tabela.loc [linha, "custo"]))
    pyautogui.press("tab")
    # OBS
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")

    # Enviar
    pyautogui.press("enter")
    pyautogui.scroll(5000) # Sobe a tela pro inicio para cadastrar o proximo produto.

# Passo 5: Repetir o processo de cadastro até acabar a lista.