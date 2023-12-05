from flask import Flask, render_template, request
from sympy import symbols, diff, expand

app = Flask(__name__)

@app.route('/')
def formulario():
    return render_template('sitio/index.html')

@app.route('/documentos')
def documentos():
        return render_template('sitio/documento.html')

@app.route('/calculadora')
def calculadora():
        return render_template('sitio/calculadora.html')


@app.route('/calcular_derivada', methods=['POST'])
def calcular_derivada():
    # Obtener la función y la variable desde el formulario
    funcion = request.form['funcion']
    variable_a_derivar = request.form['variable']

    # Definir los símbolos
    x = symbols(variable_a_derivar)

    # Calcular la derivada de la función con respecto a la variable_a_derivar
    derivada = diff(funcion, x)

    # Expandir la expresión
    derivada_expandida = expand(derivada)

    # Convertir la derivada expandida a cadena y reemplazar el asterisco con espacio vacío
    resultado_sin_asterisco = str(derivada_expandida).replace('*', '')

    # Generar el contenido HTML con el resultado final
    contenido_html = """
    <h2>Resultado final:</h2>
    <pre>{}</pre>
    """.format(resultado_sin_asterisco)

    return render_template('sitio/calculadora.html', resultado_html=contenido_html)

    
  
if __name__ == '__main__':
    app.run(debug=True)
