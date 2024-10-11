import random
import math

def generaxy_rand(rango_inferior, rango_superior):
    x = random.uniform(rango_inferior, rango_superior)
    y = random.uniform(rango_inferior, rango_superior)
    return round(x, 5), round(y, 5)

def generar_vecino(x, y, paso=0.1):
    # Genera un vecino agregando una pequeña perturbación
    delta_x = random.uniform(-paso, paso)
    delta_y = random.uniform(-paso, paso)
    nuevo_x = x + delta_x
    nuevo_y = y + delta_y
    # Asegura que los nuevos valores estén dentro del rango permitido
    nuevo_x = max(-5, min(5, nuevo_x))
    nuevo_y = max(-5, min(5, nuevo_y))
    return round(nuevo_x, 5), round(nuevo_y, 5)

def part1(x, y):
    return (x**2 + y - 11)**2

def part2(x, y):
    return (x + y**2 - 7)**2

def eval_f_xy(x, y):
    return round(part1(x, y) + part2(x, y), 4)

def algoritmo_recocido_simulado(estado_inicial_x, estado_inicial_y):
    T = 10.0
    T_MIN = 0.001
    alpha = 0.9  # Factor de enfriamiento
    max_iter = 1000  # Iteraciones por temperatura

    estado_actual_x = estado_inicial_x
    estado_actual_y = estado_inicial_y
    eval_actual = eval_f_xy(estado_actual_x, estado_actual_y)

    # Inicializar el mejor estado encontrado
    mejor_x = estado_actual_x
    mejor_y = estado_actual_y
    mejor_eval = eval_actual

    while T > T_MIN:
        for _ in range(max_iter):
            vecino_x, vecino_y = generar_vecino(estado_actual_x, estado_actual_y, paso=0.5)
            eval_vecino = eval_f_xy(vecino_x, vecino_y)

            delta = eval_vecino - eval_actual

            if delta < 0:
                # Mejorar el estado
                estado_actual_x, estado_actual_y = vecino_x, vecino_y
                eval_actual = eval_vecino

                if eval_vecino < mejor_eval:
                    mejor_x, mejor_y = vecino_x, vecino_y
                    mejor_eval = eval_vecino
            else:
                # Aceptar con probabilidad
                prob = math.exp(-delta / T)
                if random.random() < prob:
                    estado_actual_x, estado_actual_y = vecino_x, vecino_y
                    eval_actual = eval_vecino

        # Enfriamiento
        T *= alpha

    return mejor_x, mejor_y, mejor_eval

def run_algoritmo_recocido_simulado():
    # Puedes probar con múltiples estados iniciales para obtener mejores resultados
    mejores_resultados = []
    for _ in range(1):
        x_inicial, y_inicial = generaxy_rand(-5, 5)
        x, y, valor = algoritmo_recocido_simulado(x_inicial, y_inicial)
        mejores_resultados.append((x, y, valor))
    
    # Seleccionar el mejor de todos
    mejores_resultados.sort(key=lambda tup: tup[2])
    mejor = mejores_resultados[0]
    print(f"Valor mínimo encontrado: {mejor[2]} en X: {mejor[0]} Y: {mejor[1]}")

# Ejecutar el algoritmo
if __name__ == "__main__":
    run_algoritmo_recocido_simulado()
