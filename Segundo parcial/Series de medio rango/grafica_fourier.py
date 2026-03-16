import numpy as np
import matplotlib.pyplot as plt

def graficar_fourier():
    # === 1. CONFIGURA TU PROBLEMA AQUÍ ===
    L = 2                  # Semi-periodo
    tipo_extension = 'impar' # Escribe 'par' o 'impar'
    
    # Define tu función f(t) para el intervalo original [0, L]
    def funcion_original(t):
        return 2 - t       # Problema 3
    # =====================================

    # 2. CREAR EL PERIODO BASE (-L a L)
    # Rango original de 0 a L
    t_derecha = np.linspace(0.0001, L, 500) 
    y_derecha = funcion_original(t_derecha)
    
    # Reflejar hacia la izquierda (-L a 0)
    t_izquierda = -np.flip(t_derecha) 
    
    if tipo_extension == 'par':
        y_izquierda = np.flip(y_derecha)  # Reflejo tipo espejo (eje Y)
    elif tipo_extension == 'impar':
        y_izquierda = -np.flip(y_derecha) # Reflejo invertido (origen)
    else:
        print("Error: El tipo de extensión debe ser 'par' o 'impar'.")
        return

    # Unir ambas partes para tener un periodo completo
    t_periodo = np.concatenate((t_izquierda, t_derecha))
    y_periodo = np.concatenate((y_izquierda, y_derecha))

    # 3. REPETIR LA GRÁFICA (Hacerla periódica)
    plt.figure(figsize=(10, 5))
    
    # Dibujamos 3 periodos: uno en el centro, uno a la izq, uno a la der
    for i in [-1, 0, 1]:
        desplazamiento = i * 2 * L
        plt.plot(t_periodo + desplazamiento, y_periodo, color='blue', linewidth=2)

    # Resaltar la función original en rojo
    plt.plot(t_derecha, y_derecha, color='red', linewidth=4, label='Función original f(t)')

    # 4. DISEÑO VISUAL
    plt.title(f'Extensión Periódica {tipo_extension.capitalize()} de f(t)')
    plt.xlabel('t')
    plt.ylabel('f(t)')
    plt.axhline(0, color='black', linewidth=1.5)
    plt.axvline(0, color='black', linewidth=1.5)
    
    # Marcas en el eje X basadas en L
    marcas_x = [i * L for i in range(-3, 4)]
    etiquetas_x = [f'{i}L' if i not in [0, 1, -1] else ('0' if i==0 else ('L' if i==1 else '-L')) for i in range(-3, 4)]
    # Si L es un número entero como en el problema 3, mostramos el número real
    if isinstance(L, (int, float)): 
        etiquetas_x = [str(round(i * L, 2)) for i in range(-3, 4)]
        
    plt.xticks(marcas_x, etiquetas_x)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()
    
    plt.show()

if __name__ == "__main__":
    graficar_fourier()