print('*** Dibujar triangulo simetrico ***')

numero_filas = int(input('Digite o numero de filas: '))

#Iterar sobre cada fila del triangulo
for fila in range(1, numero_filas + 1):
    espacios_blanco = ' ' * (numero_filas - fila)
    asteriscos = '*' * (2 * fila - 1)
    print(f'{espacios_blanco}{asteriscos}')

""" Mismo codigo pero en java """
"""
 int numeroFilas = 3; 

        for (int fila = 1; fila <= numeroFilas; fila++) {
            // Generar espacios en blanco
            String espaciosBlanco = " ".repeat(numeroFilas - fila);
            // Generar asteriscos
            String asteriscos = "*".repeat(2 * fila - 1);
            // Imprimir la fila
            System.out.println(espaciosBlanco + asteriscos);
        }
"""