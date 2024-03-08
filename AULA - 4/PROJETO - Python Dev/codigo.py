# ----------------------ESCOPO DO PROJETO------------------------- #

# Titulo: Hashzap
# Botão de iniciar chat
    # Cliclou no botão: 
        # Poup / modal
            # Titulo: Bem vindo ao Hashzap.
            # Campo: Escreva seu nome no chat.
            # Botão: entrar no chat.

# Chat
# Embaixo do chat
    # campo de "Digite sua mensagem"
    # botão de enviar

# flet -> framework do Python (Django, flask, etc..), usaremos flet.
# Para instalar o framework, no terminal, digite: pip install flet

# --------------------------------------------------------------- #

# Colocando a mão na massa! #
import flet as ft # Importar

def main(pagina): # Criar a função principal/main.
    texto = ft.Text("Dougzap")

    chat = ft.Column()

    def enviar_mensagem_tunel(mensagem):
        print(mensagem)
        # adicione a mensagem no chat
        texto_mensagem = ft.Text(mensagem)
        chat.controls.append(texto_mensagem)
        pagina.update()

    pagina.pubsub.subscribe(enviar_mensagem_tunel)

    def enviar_mensagem(evento):
        print("Enviar mensagem")
        pagina.pubsub.send_all(f"{nome_usuario.value}: {campo_mensagem.value}")
        # limpar o campo mensagem
        campo_mensagem.value = ""
        pagina.update()

    

    campo_mensagem = ft.TextField(label="Digite sua mensagem", on_submit=enviar_mensagem)
    botao_enviar = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)
    linha_enviar = ft.Row([campo_mensagem, botao_enviar])

    def entrar_chat(evento):
        print("Entrar no chat")

        # fechar o popup
        popup.open = False
        # tirar o botao de iniciar chat
        pagina.remove(botao_iniciar)
        # tirar o titulo hashzap
        pagina.remove(texto)
        # criar o chat
        pagina.add(chat)
        pagina.pubsub.send_all(f"{nome_usuario.value} entrou no chat")
        # colocar o campo de digitar mensagem
        # criar o botão de enviar
        pagina.add(linha_enviar)
        pagina.update()

    def botao_entrar(evento): #botão para entrar
        entrar_chat(evento)

    titulo_popup = ft.Text("Bem vindo ao Hashzap")
    nome_usuario = ft.TextField(label="Escreva seu nome no chat")
    botao_entrar = ft.ElevatedButton("Entrar no chat", on_click=botao_entrar)
    popup = ft.AlertDialog(
        open=False,
        modal=True,
        title=titulo_popup,
        content=nome_usuario,
        actions=[botao_entrar]
    )

    def abrir_popup(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update() # Atualiza a modificação feia automaticamente.

    botao_iniciar = ft.ElevatedButton("Iniciar Chat", on_click=abrir_popup)   

    pagina.add(texto)
    pagina.add(botao_iniciar)

ft.app(target=main, view=ft.WEB_BROWSER) # Criar o app chamando a função principal.