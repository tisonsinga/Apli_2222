import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

def resolver_serie_compleja():
    # Variables simbólicas. 'n' puede ser negativo en la serie compleja, así que no limitamos.
    t = sp.Symbol('t', real=True)
    n = sp.Symbol('n', integer=True)
    
    # === 1. CONFIGURA TU PERÍODO Y FRECUENCIA ===
    # En el Tema 2, la gráfica iba de -1/2 a 1/2, así que el período total es 1
    T = 1           
    w0 = 2 * sp.pi / T
    
    # === 2. CONFIGURA TU FUNCIÓN Y LÍMITES DE INTEGRACIÓN ===
    # TRUCO DE EXAMEN: Para no confundir a Python con funciones seccionadas (Piecewise)
    # y números imaginarios, simplemente pon el valor de la función donde NO es cero,
    # y pon los límites donde empieza y termina esa parte de la función.
    # En el Tema 2, vale 1 solo desde -1/4 hasta 1/4.
    f_t = 1
    limite_inf = -1/4
    limite_sup = 1/4
    # ==========================================================

    print("\n" + "="*65)
    print(" SERIE EXPONENCIAL COMPLEJA DE FOURIER (Paso a Paso) ")
    print("="*65 + "\n")

    print("[ PASO 1: Calcular c_0 (Componente DC) ]")
    print(f"Fórmula: (1/T) * integral_{limite_inf}^{limite_sup} f(t) dt")
    c0 = (1/T) * sp.integrate(f_t, (t, limite_inf, limite_sup))
    print("Resultado c_0 =")
    sp.pprint(c0)
    print("\n")

    print("[ PASO 2: Plantear la integral para c_n ]")
    print(f"Fórmula: c_n = (1/{T}) * integral f(t) * e^(-j*n*w0*t) dt")
    
    # sp.I es la letra 'j' imaginaria
    exponencial = sp.exp(-sp.I * n * w0 * t)
    
    print("Integral a resolver:")
    sp.pprint(sp.Integral(f_t * exponencial, (t, limite_inf, limite_sup)))
    print("\n")

    print("[ PASO 3: Resolver y simplificar c_n ]")
    cn = (1/T) * sp.integrate(f_t * exponencial, (t, limite_inf, limite_sup))
    
    # Usamos rewrite(sp.sin) para convertir las exponenciales raras en senos (función sinc)
    cn_simp = sp.simplify(cn).rewrite(sp.sin)
    
    print("Resultado c_n =")
    sp.pprint(cn_simp)
    print("\n(Nota: Si ves 'sinc', recuerda que sinc(x) = sin(x)/x)")
    print("="*65 + "\n")

    # === SECCIÓN DE GRÁFICA (ESPECTRO DE FRECUENCIAS) ===
    print("Generando la gráfica del espectro de frecuencias...")
    
    # Rango de n que pide el problema (-10 a 10)
    n_vals = np.arange(-10, 11)
    cn_mags = []

    # Evaluamos la magnitud |c_n| para cada palito
    for val in n_vals:
        if val == 0:
            cn_mags.append(abs(float(c0)))
        else:
            # Sustituimos n, sacamos valor absoluto (módulo) y lo pasamos a float
            cn_eval = cn_simp.subs(n, val)
            cn_mags.append(float(sp.Abs(cn_eval)))

    # Dibujamos los palitos (stem plot)
    plt.figure(figsize=(10, 5))
    plt.stem(n_vals, cn_mags, basefmt="black", linefmt="b-", markerfmt="bo")
    plt.title("Espectro de Amplitud Discreto |c_n|")
    plt.xlabel("Armónico (n)")
    plt.ylabel("Magnitud |c_n|")
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.xticks(n_vals) # Mostrar todos los números en el eje X
    plt.show()

if __name__ == "__main__":
    resolver_serie_compleja()