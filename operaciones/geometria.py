import math

def area_circulo(radio):
    """
    Devuelve el área de un círculo dado su radio.

    Parameters:
    radio (float): Radio del círculo.

    Returns:
    float: Área del círculo.
    """
    return math.pi * radio ** 2

def perimetro_circulo(radio):
    """
    Devuelve el perímetro (circunferencia) de un círculo dado su radio.

    Parameters:
    radio (float): Radio del círculo.

    Returns:
    float: Perímetro del círculo.
    """
    return 2 * math.pi * radio

def area_rectangulo(base, altura):
    """
    Devuelve el área de un rectángulo dado su base y altura.

    Parameters:
    base (float): Longitud de la base del rectángulo.
    altura (float): Longitud de la altura del rectángulo.

    Returns:
    float: Área del rectángulo.
    """
    return base * altura

def perimetro_rectangulo(base, altura):
    """
    Devuelve el perímetro de un rectángulo dado su base y altura.

    Parameters:
    base (float): Longitud de la base del rectángulo.
    altura (float): Longitud de la altura del rectángulo.

    Returns:
    float: Perímetro del rectángulo.
    """
    return 2 * (base + altura)

