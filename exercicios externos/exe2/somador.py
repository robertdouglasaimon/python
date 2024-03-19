from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            num1 = float(request.form['num1'])
            num2 = float(request.form['num2'])
            resultado = num1 + num2
            return f"A soma de {num1} e {num2} é igual a {resultado}."
        except ValueError:
            return "Por favor, insira números válidos."
    return '''
    <form method="post">
        <label for="num1">Digite o primeiro número:</label>
        <input type="text" id="num1" name="num1">
        <br>
        <label for="num2">Digite o segundo número:</label>
        <input type="text" id="num2" name="num2">
        <br>
        <button type="submit">Calcular Soma</button>
    </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)




    """

    1 - O processo passo a passo, começando com a instalação das dependências necessárias e seguindo com a explicação detalhada do código:

    Instalação das dependências:

    Antes de executar o código, é necessário instalar o Flask. Você pode fazer isso usando o comando abaixo no terminal:
     pip install Flask 

    2 - Código Python:
        Agora, vou explicar cada linha do código Python:

         from flask import Flask, render_template, request 

        Importamos as classes Flask, render_template e request do módulo flask. Isso nos permite criar uma aplicação web, renderizar templates HTML e acessar os dados enviados através das requisições HTTP.
    
    3 - Criamos uma instância da classe Flask, que é a nossa aplicação web. Passamos __name__ como argumento, que     é        uma     variável especial em Python que representa o nome do módulo ou do pacote.

         app = Flask(__name__) 

    4 - Definimos uma rota para a nossa aplicação. O decorador @app.route associa a função index() à rota raiz '/'. Especificamos também os métodos HTTP permitidos para esta rota, que são GET e POST.

         @app.route('/', methods=['GET', 'POST']) 

    5 - Definimos a função index(), que será chamada quando um usuário acessar a rota raiz ('/'). Esta função irá manipular tanto requisições GET quanto POST.

         def index(): 

    6 - Verificamos se a requisição feita à rota raiz é do tipo POST. Se for, significa que o formulário foi submetido.

         if request.method == 'POST': 

    7 - Tentamos converter os valores enviados pelo formulário em números de ponto flutuante (float). Se a conversão    for bem-sucedida, calculamos a soma dos números e retornamos uma mensagem com o resultado da soma. Se houver um erro durante a conversão (por exemplo, se o usuário inserir texto em vez de números), capturamos a exceção ValueError e retornamos uma mensagem de erro.

          try:
             num1 = float(request.form['num1'])
             num2 = float(request.form['num2'])
             resultado = num1 + num2
             return f"A soma de {num1} e {num2} é igual a {resultado}."
        except ValueError:
             return "Por favor, insira números válidos.

    8 - Se a requisição não for do tipo POST, isso significa que é uma requisição GET. Neste caso, retornamos um formulário HTML simples. Este formulário contém dois campos de entrada (input) para que o usuário insira os números a serem somados. O atributo method="post" indica que o formulário será submetido usando o método POST.

        return '''
        <form method="post">
            <label for="num1">Digite o primeiro número:</label>
            <input type="text" id="num1" name="num1">
            <br>
            <label for="num2">Digite o segundo número:</label>
            <input type="text" id="num2" name="num2">
            <br>
            <button type="submit">Calcular Soma</button>
        </form>                                                        

    9 - Verificamos se o script está sendo executado diretamente (não importado como um módulo). Se for o caso, iniciamos o servidor web embutido do Flask. O parâmetro debug=True ativa o modo de depuração, que é útil durante o desenvolvimento.

          if __name__ == '__main__':
          app.run(debug=True)       

'''


        """
