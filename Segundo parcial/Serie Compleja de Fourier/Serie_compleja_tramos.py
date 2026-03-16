import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

def resolver_serie_compleja_tramos():
    t = sp.Symbol('t', real=True)
    n = sp.Symbol('n', integer=True)
    
    # === 1. CONFIGURA TU PERÍODO Y FRECUENCIA ===
    T = 2           # Ejemplo: Período total de 2
    w0 = 2 * sp.pi / T
    
    # === 2. CONFIGURA TUS TRAMOS AQUÍ ===
    # Formato: (Función, Límite Inferior, Límite Superior)
    # Puedes agregar tantos renglones como tramos tenga el problema.
    # Ejemplo: f(t)=5 de 0 a 1, y f(t)=-3 de 1 a 2
    tramos = [
        (5, 0, 1),
        (-3, 1, 2)
    ]
    # ============================================

    print("\n" + "="*65)
    print(" SERIE COMPLEJA DE FOURIER (MÚLTIPLES TRAMOS) ")
    print("="*65 + "\n")

    # --- PASO 1: Calcular c_0 ---
    print("[ PASO 1: Calcular c_0 (Suma de integrales) ]")
    suma_c0 = 0
    for i, (f_val, lim_inf, lim_sup) in enumerate(tramos):
        integral_tramo = sp.integrate(f_val, (t, lim_inf, lim_sup))
        print(f"  Integral tramo {i+1}: {integral_tramo}")
        suma_c0 += integral_tramo
        
    c0 = (1/T) * suma_c0
    print(f"\nResultado c_0 = {c0}\n")

    # --- PASO 2: Calcular c_n ---
    print("[ PASO 2: Plantear y resolver c_n ]")
    exponencial = sp.exp(-sp.I * n * w0 * t)
    
    suma_cn = 0
    for i, (f_val, lim_inf, lim_sup) in enumerate(tramos):
        integral_tramo_cn = sp.integrate(f_val * exponencial, (t, lim_inf, lim_sup))
        suma_cn += integral_tramo_cn
        
    cn = (1/T) * suma_cn
    
    # Simplificamos y convertimos exponenciales complejas a senos/cosenos si es posible
    cn_simp = sp.simplify(cn).rewrite(sp.sin)
    
    print("Resultado c_n (Sumatoria de todos los tramos) =")
    sp.pprint(cn_simp)
    print("="*65 + "\n")

    # --- PASO 3: GRAFICAR EL ESPECTRO ---
    print("Generando la gráfica del espectro de frecuencias...")
    n_vals = np.arange(-10, 11)
    cn_mags = []

    for val in n_vals:
        if val == 0:
            cn_mags.append(float(sp.Abs(c0)))
        else:
            # Sustituimos n y aplicamos sp.Abs de forma segura
            cn_eval = cn_simp.subs(n, val)
            cn_mags.append(float(sp.Abs(cn_eval)))

    plt.figure(figsize=(10, 5))
    plt.stem(n_vals, cn_mags, basefmt="black", linefmt="r-", markerfmt="ro")
    plt.title("Espectro de Amplitud Discreto |c_n| (Función por Tramos)")
    plt.xlabel("Armónico (n)")
    plt.ylabel("Magnitud |c_n|")
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.xticks(n_vals)
    plt.show()

if __name__ == "__main__":
    resolver_serie_compleja_tramos()