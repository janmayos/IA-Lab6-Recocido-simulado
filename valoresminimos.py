import random
import math


def generaxy_rand(rango_inferior, rango_superior):
    x = random.uniform(rango_inferior, rango_superior)
    y = random.uniform(rango_inferior, rango_superior)
    return round(x, 5), round(y, 5)


def generar_vecino():
    nuevo_x, nuevo_y = generaxy_rand(-5, 5)
    return nuevo_x, nuevo_y


def part1(x, y):
    return (x**2 + y - 11)**2


def part2(x, y):
    return (x + y**2 - 7)**2


def eval_f_xy(x, y):
    return round(part1(x, y) + part2(x, y), 4)


def algoritmo_recocido_simulado(estado_inicial_x, estado_inicial_y):
    T = 10.0
    T_MIN = 0.001
    enfriamiento = 0.9  # Factor de enfriamiento
    max_iter = 10000  # Iteraciones por temperatura

    estado_actual_x = estado_inicial_x
    estado_actual_y = estado_inicial_y
    eval_actual = eval_f_xy(estado_actual_x, estado_actual_y)

    # Guardamos el mejor estado encontrado
    mejor_x = estado_actual_x
    mejor_y = estado_actual_y
    mejor_eval = eval_actual

    while T > T_MIN:
        for _ in range(max_iter):
            vecino_x, vecino_y = generar_vecino()
            eval_vecino = eval_f_xy(vecino_x, vecino_y)

            if eval_vecino < eval_actual:
                # Mejorar el estado
                estado_actual_x, estado_actual_y = vecino_x, vecino_y
                eval_actual = eval_vecino

                if eval_vecino < mejor_eval:
                    mejor_x, mejor_y = vecino_x, vecino_y
                    mejor_eval = eval_vecino
            else:
                # Aceptar con probabilidad
                prob = math.exp(-(eval_vecino - eval_actual) / T)
                if random.random() < prob:
                    estado_actual_x, estado_actual_y = vecino_x, vecino_y
                    eval_actual = eval_vecino

        # Enfriamiento
        T -= enfriamiento

    return mejor_x, mejor_y, mejor_eval


def run_algoritmo_recocido_simulado():

    x_inicial, y_inicial = generaxy_rand(-5, 5)
    x, y, valor = algoritmo_recocido_simulado(x_inicial, y_inicial)
    print(f"Valor mínimo encontrado: {valor} en X: {x} Y: {y}")


if __name__ == "__main__":
    run_algoritmo_recocido_simulado()
