import sympy as sp

def serie_fourier_completa():
    t = sp.Symbol('t')
    n = sp.Symbol('n', integer=True, positive=True)
    
    # === 1. CONFIGURA TU PROBLEMA AQUÍ ===
    f = 2-t          # Problema 2
    L = 2              # Semi-periodo
    tipo_serie = 'seno'   # 'seno' o 'coseno'
    terminos_a_mostrar = 5  # Cuántos términos expandidos quieres ver
    # =====================================
    
    print("=" * 50)
    print(f"Calculando Serie de Medio Rango en {tipo_serie.upper()}")
    print(f"f(t) = {f}    |    L = {L}")
    print("=" * 50 + "\n")
    
    terminos_expandidos = []
    
    if tipo_serie == 'coseno':
        # 1. Calcular a_0
        a0 = (2/L) * sp.integrate(f, (t, 0, L))
        a0_simp = sp.simplify(a0)
        print(f"[ FÓRMULAS GENERALES ]\na_0 = {a0_simp}")
        if a0_simp != 0:
            terminos_expandidos.append(a0_simp / 2)
            
        # 2. Calcular a_n general
        an_general = (2/L) * sp.integrate(f * sp.cos(n * sp.pi * t / L), (t, 0, L))
        print(f"a_n = {sp.simplify(an_general)}\n")
        
        # 3. Evaluar término por término para evitar divisiones por cero
        print("[ EVALUACIÓN TÉRMINO POR TÉRMINO ]")
        for i in range(1, terminos_a_mostrar + 1):
            # Integramos directamente con el número exacto, sin usar 'n'
            an_val = (2/L) * sp.integrate(f * sp.cos(i * sp.pi * t / L), (t, 0, L))
            an_val = sp.simplify(an_val)
            print(f"Para n={i}:  a_{i} = {an_val}")
            
            if an_val != 0:
                termino_real = an_val * sp.cos(i * sp.pi * t / L)
                terminos_expandidos.append(termino_real)
                
    elif tipo_serie == 'seno':
        # 1. Calcular b_n general
        bn_general = (2/L) * sp.integrate(f * sp.sin(n * sp.pi * t / L), (t, 0, L))
        print(f"[ FÓRMULA GENERAL ]\nb_n = {sp.simplify(bn_general)}\n")
        
        # 2. Evaluar término por término
        print("[ EVALUACIÓN TÉRMINO POR TÉRMINO ]")
        for i in range(1, terminos_a_mostrar + 1):
            bn_val = (2/L) * sp.integrate(f * sp.sin(i * sp.pi * t / L), (t, 0, L))
            bn_val = sp.simplify(bn_val)
            print(f"Para n={i}:  b_{i} = {bn_val}")
            
            if bn_val != 0:
                termino_real = bn_val * sp.sin(i * sp.pi * t / L)
                terminos_expandidos.append(termino_real)

    # 4. Mostrar la respuesta final expandida
    print("\n" + "=" * 50)
    print("[ RESPUESTA FINAL EXPANDIDA ]")
    # Sumamos visualmente todos los términos válidos que encontramos
    suma_final = sum(terminos_expandidos)
    print(f"f(t) ≈ {suma_final} ...")
    print("=" * 50)

if __name__ == "__main__":
    serie_fourier_completa()