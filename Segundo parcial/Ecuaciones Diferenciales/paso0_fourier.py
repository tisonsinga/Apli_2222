import sympy as sp

def calcular_paso_0_fourier():
    t = sp.Symbol('t', real=True)
    # Declaramos 'n' como entero y positivo para que SymPy pueda simplificar los senos y cosenos
    n = sp.Symbol('n', integer=True, positive=True)

    # === 1. CONFIGURA TU PERÍODO AQUÍ ===
    T = 2 * sp.pi    # Período completo
    L = T / 2        # Semi-período
    
    # Frecuencia fundamental
    w0 = sp.pi / L

    # === 2. CONFIGURA TU FUNCIÓN f(t) AQUÍ ===
    # Usamos sp.Piecewise para funciones seccionadas: (valor, condicion)
    # Ejemplo: f(t) = 1 de 0 a pi, y f(t) = 0 de pi a 2pi
    f_t = sp.Piecewise(
        (1, (t >= 0) & (t < sp.pi)), 
        (0, (t >= sp.pi) & (t <= 2*sp.pi))
    )
    # =========================================

    print("\n" + "="*65)
    print(" PASO 0: CÁLCULO DE COEFICIENTES DE FOURIER (a_0, a_n, b_n) ")
    print("="*65 + "\n")

    # [ 1. Cálculo de a_0 ]
    print("[ 1. Coeficiente a_0 ]")
    print("Fórmula: (1/L) * integral_0^T f(t) dt")
    a0 = (1/L) * sp.integrate(f_t, (t, 0, T))
    a0_simp = sp.simplify(a0)
    print("Resultado a_0 =")
    sp.pprint(a0_simp)
    print("\n")

    # [ 2. Cálculo de a_n ]
    print("[ 2. Coeficiente a_n ]")
    print("Fórmula: (1/L) * integral_0^T f(t)*cos(n*w0*t) dt")
    an = (1/L) * sp.integrate(f_t * sp.cos(n * w0 * t), (t, 0, T))
    an_simp = sp.simplify(an)
    print("Resultado a_n =")
    sp.pprint(an_simp)
    print("\n")

    # [ 3. Cálculo de b_n ]
    print("[ 3. Coeficiente b_n ]")
    print("Fórmula: (1/L) * integral_0^T f(t)*sin(n*w0*t) dt")
    bn = (1/L) * sp.integrate(f_t * sp.sin(n * w0 * t), (t, 0, T))
    bn_simp = sp.simplify(bn)
    print("Resultado b_n =")
    sp.pprint(bn_simp)
    print("\n")
    
    print("="*65)
    print("NOTA PARA TU CÓDIGO DE EDOs:")
    print("Copia estos resultados y pégalos en las variables a_0_in, a_n_in y b_n_in")
    print("del script 'edo_paso_a_paso.py'.")
    print("="*65 + "\n")

if __name__ == "__main__":
    calcular_paso_0_fourier()