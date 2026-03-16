import sympy as sp

def serie_fourier_visual():
    t = sp.Symbol('t')
    n = sp.Symbol('n', integer=True, positive=True)
    
    # === 1. CONFIGURA TU PROBLEMA AQUÍ ===
    f = 2-t          # Problema 2
    L = 2            # Semi-periodo
    tipo_serie = 'seno'   # 'seno' o 'coseno'
    # =====================================
    
    print("\n" + "=" * 55)
    print(" [ FÓRMULA FINAL VISUAL PARA EL EXAMEN ] ")
    print("=" * 55 + "\n")
    
    # Función auxiliar para detectar si la sumatoria debe empezar en 2
    def procesar_termino(termino):
        inicio = 1
        termino_limpio = sp.simplify(termino)
        
        # Si Sympy creó un "Piecewise" (por división entre cero en n=1)
        if isinstance(termino_limpio, sp.Piecewise):
            # Extraemos solo la fórmula general limpia
            termino_limpio = termino_limpio.args[0][0]
            inicio = 2 # Forzamos a que la sumatoria visual empiece en 2
            
        return termino_limpio, inicio

    if tipo_serie == 'coseno':
        # Cálculos de integrales
        a0 = (2/L) * sp.integrate(f, (t, 0, L))
        an = (2/L) * sp.integrate(f * sp.cos(n * sp.pi * t / L), (t, 0, L))
        
        # Procesamiento
        termino_constante = sp.simplify(a0) / 2
        an_limpio, inicio_n = procesar_termino(an)
        termino_sum = an_limpio * sp.cos(n * sp.pi * t / L)
        
        # sp.oo significa infinito en Sympy
        sumatoria = sp.Sum(termino_sum, (n, inicio_n, sp.oo))
        
        print("x(t) = \n")
        if termino_constante != 0:
            sp.pprint(termino_constante)
            print("\n  + \n")
            
        # Imprime el dibujo de la sumatoria
        sp.pprint(sumatoria)
        
    elif tipo_serie == 'seno':
        # Cálculos de integrales
        bn = (2/L) * sp.integrate(f * sp.sin(n * sp.pi * t / L), (t, 0, L))
        
        # Procesamiento
        bn_limpio, inicio_n = procesar_termino(bn)
        termino_sum = bn_limpio * sp.sin(n * sp.pi * t / L)
        
        sumatoria = sp.Sum(termino_sum, (n, inicio_n, sp.oo))
        
        print("f(t) = \n")
        # Imprime el dibujo de la sumatoria
        sp.pprint(sumatoria)

    print("\n" + "=" * 55)

if __name__ == "__main__":
    serie_fourier_visual()