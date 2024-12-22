def suma(a, b):
    """
    Devuelve la suma de dos números.

    Parameters:
    a (int, float): Primer número.
    b (int, float): Segundo número.

    Returns:
    int, float: Resultado de la suma.
    """
    return a + b

def resta(a, b):
    """
    Devuelve la resta de dos números.

    Parameters:
    a (int, float): Primer número.
    b (int, float): Segundo número.

    Returns:
    int, float: Resultado de la resta.
    """
    return a - b

def multiplicacion(a, b):
    """
    Devuelve la multiplicación de dos números.

    Parameters:
    a (int, float): Primer número.
    b (int, float): Segundo número.

    Returns:
    int, float: Resultado de la multiplicación.
    """
    return a * b

def division(a, b):
    """
    Devuelve la división de dos números.

    Parameters:
    a (int, float): Numerador.
    b (int, float): Denominador.

    Returns:
    float: Resultado de la división.
    
    Raises:
    ValueError: Si el denominador es 0.
    """
    if b == 0:
        raise ValueError("El denominador no puede ser cero.")
    return a / b
