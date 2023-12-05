from sympy import symbols, diff, pprint

# Definir los símbolos
from sympy import symbols

# Todas las letras del abecedario como variables simbólicas
a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z = symbols('a b c d e f g h i j k l m n o p q r s t u v w x y z')


# Definir la función con múltiples símbolos
f = 3*x**2 + 5*x*y - 7*y**2 + 1



# Definir el símbolo a derivar
variable_a_derivar = x

# Calcular la derivada de la función con respecto a la variable_a_derivar
derivada = diff(f, variable_a_derivar)

# Obtener el objeto Derivative para mostrar el procedimiento
derivada_objeto = diff(f, x, evaluate=False)

# Mostrar el procedimiento paso a paso
print("Procedimiento:")
pprint(derivada_objeto, use_unicode=True)

# Mostrar el resultado final
print("\nResultado final:")
pprint(derivada)