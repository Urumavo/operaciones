import operaciones.matematica as mat
import operaciones.geometria as geo

def main():
    # Usando las funciones del módulo matematica
    print("Multiplicación de 10 y 5:", mat.multiplicacion(10, 5))
    print("División de 10 y 5:", mat.division(10, 5))

    # Usando las funciones del módulo geometria
    print("Área del rectángulo (base=10, altura=5):", geo.area_rectangulo(10, 5))
    print("Perímetro del rectángulo (base=10, altura=5):", geo.perimetro_rectangulo(10, 5))

if __name__ == "__main__":
    main()
