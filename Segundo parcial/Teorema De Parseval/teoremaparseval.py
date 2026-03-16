import sympy as sp

def resolver_parseval():
    t = sp.Symbol('t')
    n = sp.Symbol('n', integer=True, positive=True)

    # === 1. CONFIGURA TU PROBLEMA AQUÍ ===
    # Escribe tu función f(t) o v(t)
    # (El ejemplo actual es el Problema 3 de tu hoja)
    v_t = sp.cos(t) - (1/3)*sp.sin(3*t) + (2/5)*sp.cos(2*t)
    
    T = 2 * sp.pi  # Período de la señal
    R = 1          # Valor de la resistencia en Ohmios
    armonicos = 4  # Cuántos armónicos n quieres evaluar en Parseval
    # =====================================

    omega = 2 * sp.pi / T

    print("\n" + "=" * 60)
    print(" ANÁLISIS DE PARSEVAL, VALOR R.M.S. Y POTENCIA ")
    print("=" * 60 + "\n")

    # --- MÉTODO 1: POR DEFINICIÓN (INTEGRAL) ---
    print("[ 1. CÁLCULO POR DEFINICIÓN (INTEGRAL DIRECTA) ]")
    print("Fórmula: V_rms^2 = (1/T) * int_0^T (v(t))^2 dt\n")
    
    # Sympy puede tardar unos segundos si la función es muy larga
    v_rms_sq = (1/T) * sp.integrate(v_t**2, (t, 0, T))
    v_rms_sq = sp.simplify(v_rms_sq)

    print(f"V_rms^2 exacto = {v_rms_sq}")
    print(f"V_rms   exacto = {sp.simplify(sp.sqrt(v_rms_sq))}")
    print(f"V_rms decimal  = {sp.sqrt(v_rms_sq).evalf(5)} V\n")

    # --- MÉTODO 2: POR TEOREMA DE PARSEVAL ---
    print("-" * 60)
    print("[ 2. CÁLCULO POR COEFICIENTES (PARSEVAL) ]")
    print("Fórmula: V_rms^2 = (a_0^2)/4 + (1/2) * Sumatoria(a_n^2 + b_n^2)\n")

    # Cálculo de la componente DC (a0)
    a0 = (2/T) * sp.integrate(v_t, (t, 0, T))
    a0_simp = sp.simplify(a0)
    termino_dc = (a0_simp**2) / 4

    print(f"Componente DC (a_0) = {a0_simp}")
    print(f"Energía DC (a_0^2 / 4) = {termino_dc}\n")

    suma_parseval = termino_dc

    print(f"Evaluando los primeros {armonicos} armónicos:")
    for i in range(1, armonicos + 1):
        # Integrales para cada coeficiente
        an = (2/T) * sp.integrate(v_t * sp.cos(i * omega * t), (t, 0, T))
        bn = (2/T) * sp.integrate(v_t * sp.sin(i * omega * t), (t, 0, T))

        an_simp = sp.simplify(an)
        bn_simp = sp.simplify(bn)

        # Si el coeficiente existe (no es cero), lo sumamos
        if an_simp != 0 or bn_simp != 0:
            potencia_armonico = (an_simp**2 + bn_simp**2) / 2
            suma_parseval += potencia_armonico
            print(f"  n={i} | a_{i} = {an_simp:5} | b_{i} = {bn_simp:5} | Aporte de energía: {potencia_armonico}")

    print(f"\nSuma total de Parseval exacta = {sp.simplify(suma_parseval)}")
    
    # --- POTENCIA EN LA CARGA ---
    print("-" * 60)
    print(f"[ 3. POTENCIA PROMEDIO EN EL RESISTOR (R = {R} Ohm) ]")
    print("Fórmula: P = V_rms^2 / R\n")
    
    potencia_promedio = v_rms_sq / R
    print(f"Potencia Promedio = {sp.simplify(potencia_promedio)} W")
    print(f"Potencia decimal  = {potencia_promedio.evalf(5)} W")
    print("=" * 60 + "\n")

if __name__ == "__main__":
    resolver_parseval()