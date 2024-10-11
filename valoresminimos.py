import random
import math

def generaxy_rand(rango_inferior, rango_superior):

    x = random.uniform(rango_inferior, rango_superior)
    y = random.uniform(rango_inferior, rango_superior)
    return round(x, 5), round(y, 5)


def part1(x, y):
    return pow(pow(x, 2)+y-11, 2)


def part2(x, y):
    return pow(x+pow(y, 2)-7, 2)


def eval_f_xy(x, y):
    return round(part1(x, y)+part2(x, y), 4)

def algorito_recocido_simulado(estado_actual_x,estado_actual_y):
    T = 10
    T_MIN = 1
    v_enfriamiento = 100
    while T > T_MIN:
        for i in range(v_enfriamiento):
            estado_nuevo_x,estado_nuevo_y = generaxy_rand(-5, 5)
            eval_nuevo = eval_f_xy(estado_nuevo_x,estado_nuevo_y) 
            eval_actual = eval_f_xy(estado_actual_x,estado_actual_y)
            #print(estado_actual_x,estado_actual_y)
            if eval_nuevo <= eval_actual:
                estado_actual_x = estado_nuevo_x
                estado_actual_y = estado_nuevo_y
            else:
                randomval = random.random()
                #print(eval_actual,eval_nuevo,T)
                expr = math.exp(((-1*(eval_actual-eval_nuevo))/T))
                
                #print(randomval,expr)

                if randomval < expr:
                    estado_actual_x = estado_nuevo_x
                    estado_actual_y = estado_nuevo_y
        T-=0.005
    return estado_actual_x,estado_actual_y


def run_minimos():
    valorminimo = 0
    xaux = 0
    yaux = 0
    iaux = 0
    for i in range(0, 1000000):
        x, y = generaxy_rand(-5, 5)
        res = eval_f_xy(x, y)
        # print(i)
        # print(x,y,res)
        if valorminimo > res or i == 0:
            valorminimo = res
            xaux = x
            yaux = y
            iaux = i
        if valorminimo == 0:
            print(valorminimo)
            break
    print("Valor minimo es:"+str(valorminimo)+" X:" +
          str(xaux) + " Y:"+str(yaux)+" Iteración: "+str(iaux))

def run_algorito_recocido_simulado():
    x, y = generaxy_rand(-5, 5)
    x,y = algorito_recocido_simulado(x,y)
    print("Valor minimo es:"+str(eval_f_xy(x,y))+" X:" +
          str(x) + " Y:"+str(y))


# X:3 Y:2
# X:2.99885 Y:2.00055
if __name__ == "__main__":
    run_algorito_recocido_simulado()
