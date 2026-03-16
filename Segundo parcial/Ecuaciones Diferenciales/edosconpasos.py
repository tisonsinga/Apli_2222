import sympy as sp

def resolver_edo_fourier_pasos():
    n = sp.Symbol('n', integer=True, positive=True)
    A_n, B_n = sp.symbols('A_n B_n')

    # === 1. INGRESA LOS COEFICIENTES DE TU EDO AQUÍ ===
    # Forma estándar: c2*y'' + c1*y' + c0*y = f(t)
    # (Ejemplo actual: y' + y = f(t), por lo que c2=0, c1=1, c0=1)
    c2 = 0  
    c1 = 1  
    c0 = 1  

    # === 2. INGRESA LOS COEFICIENTES DE f(t) AQUÍ ===
    # (Reemplaza con los que calculaste en tu Paso 0)
    a_0_in = 1
    a_n_in = 0
    b_n_in = (1 - (-1)**n) / (n * sp.pi)
    # ===================================================

    print("\n" + "="*65)
    print(" RESOLUCIÓN DE EDO CON SERIES DE FOURIER (PASO A PASO) ")
    print("="*65 + "\n")

    print("[ PASO 1: Calcular A_0 ]")
    print("Igualando los términos constantes (n=0):")
    print(f"{c0} * (A_0 / 2) = {a_0_in} / 2")
    
    A_0_out = a_0_in / c0 if c0 != 0 else "Indefinido (c0=0)"
    print(f"Despejando A_0 => A_0 = {A_0_out}\n")

    print("[ PASO 2: Plantear el sistema de ecuaciones para A_n y B_n ]")
    print("Al sustituir y(t), y'(t) y y''(t), e igualar coeficientes, obtenemos:\n")
    
    # Ecuaciones teóricas que resultan de sustituir las derivadas
    # (c0 - c2*n^2)An + (c1*n)Bn = an
    # (-c1*n)An + (c0 - c2*n^2)Bn = bn
    
    eq_cos = sp.Eq((c0 - c2*n**2)*A_n + (c1*n)*B_n, a_n_in)
    eq_sin = sp.Eq((-c1*n)*A_n + (c0 - c2*n**2)*B_n, b_n_in)

    print("Para los cosenos (A_n):")
    sp.pprint(eq_cos)
    print("\nPara los senos (B_n):")
    sp.pprint(eq_sin)
    print("\n")

    print("[ PASO 3: Resolver el sistema (Tus fórmulas finales) ]")
    solucion = sp.solve((eq_cos, eq_sin), (A_n, B_n))
    
    A_n_final = sp.simplify(solucion[A_n])
    B_n_final = sp.simplify(solucion[B_n])

    print("=> Fórmula para A_n:")
    sp.pprint(A_n_final)
    print("\n=> Fórmula para B_n:")
    sp.pprint(B_n_final)
    print("\n")

    print("[ PASO 4: Escribir la sumatoria final en tu examen ]")
    print("y(t) = (A_0 / 2) + Sumatoria [ (A_n)*cos(nt) + (B_n)*sin(nt) ]")
    print("\nVerifica el denominador de tus fórmulas. Si para algún valor de 'n'")
    print("el denominador se hace cero (ej. n=1), ¡TIENES RESONANCIA ahí!")
    print("="*65 + "\n")

if __name__ == "__main__":
    resolver_edo_fourier_pasos()