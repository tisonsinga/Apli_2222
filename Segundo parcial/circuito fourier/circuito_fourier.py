import sympy as sp

def resolver_circuito_ac_fourier():
    # Variables simbólicas
    n = sp.Symbol('n', positive=True, integer=True)
    t = sp.Symbol('t', real=True)
    
    # === 1. CONFIGURA TU CIRCUITO Y SEÑAL AQUÍ ===
    R = 2        # Resistencia en Ohmios (pon 0 si no hay)
    L = 1        # Inductancia en Henrios (pon 0 si no hay)
    C = 0        # Capacitancia en Faradios (pon 0 si no hay)
    
    w0 = 1       # Frecuencia fundamental (omega_0)
    
    # Amplitud del voltaje de entrada para el armónico n (En el Tema 1 era 1/n^2)
    V_n_amp = 1 / (n**2) 
    
    # Tipo de función trigonométrica de la entrada ('coseno' o 'seno')
    tipo_funcion = 'coseno'
    # ==============================================
    
    print("\n" + "="*65)
    print(" ANÁLISIS DE CIRCUITO CON SERIES DE FOURIER (FASORES) ")
    print("="*65 + "\n")
    
    # Frecuencia del armónico n
    w_n = n * w0
    
    # Impedancia Compleja Zn = R + j(wL - 1/wC)
    Reactancia_L = w_n * L if L != 0 else 0
    Reactancia_C = 1 / (w_n * C) if C != 0 else 0
    
    # sp.I es el número imaginario 'j' en Sympy
    Z_n = R + sp.I * (Reactancia_L - Reactancia_C)
    
    print("[ 1. IMPEDANCIA COMPLEJA Z_n ]")
    print(f"Z_n = {Z_n}\n")
    
    # Magnitud y Fase de Zn
    mag_Z_n = sp.sqrt(sp.re(Z_n)**2 + sp.im(Z_n)**2)
    fase_Z_n = sp.atan2(sp.im(Z_n), sp.re(Z_n))
    
    print("[ 2. MAGNITUD Y FASE DE LA IMPEDANCIA ]")
    print("Magnitud |Z_n| :")
    sp.pprint(mag_Z_n)
    print("\nÁngulo de desfase (fase) de Z_n :")
    sp.pprint(fase_Z_n)
    print("\n")
    
    # Cálculo de la Corriente In
    I_n_amp = V_n_amp / mag_Z_n
    
    print("[ 3. AMPLITUD DE LA CORRIENTE I_n ]")
    print("I_n = |V_n| / |Z_n| :")
    sp.pprint(I_n_amp)
    print("\n")
    
    # Respuesta final en el tiempo i(t)
    print("[ 4. RESPUESTA FINAL EN EL TIEMPO i_n(t) ]")
    if tipo_funcion == 'coseno':
        i_t = I_n_amp * sp.cos(w_n * t - fase_Z_n)
    else:
        i_t = I_n_amp * sp.sin(w_n * t - fase_Z_n)
        
    print("El término general de la corriente i(t) a meter en la sumatoria es:\n")
    sp.pprint(i_t)
    print("\n" + "="*65)

if __name__ == "__main__":
    resolver_circuito_ac_fourier()