# Autores: Luca, Thiago, Nicolas e Carlos CC5P12 E CC5Q12 UNIP SWIFT

from queue import Queue
import time

# Tempo dos temporizadores
temporizador1 = 0.001
temporizador2 = 0.01
temporizador3 = 0.1
temporizador4 = 1

def main():
    # Iniciando o tempo
    initial_time = time.time()
    # Começo do temporizador 1
    print("Realizando o processo do temporizador 1:")
    process_initial_time = time.time()
    run_all_processes(temporizador1)
    ################################################
    execution_time = time.time() - process_initial_time
    print('Resultado do temporizador 1: ' + str(execution_time) + ' segundos\n')
    # Começo do temporizador 2
    print("Realizando o processo do temporizador 2:")
    process_initial_time = time.time()
    run_all_processes(temporizador2)
    ################################################
    execution_time = time.time() - process_initial_time
    print('Resultado do temporizador 2: ' + str(execution_time) + ' segundos\n')
    # Começo do temporizador 3
    print("Realizando o processo do temporizador 3")
    process_initial_time = time.time()
    run_all_processes(temporizador3)
    ################################################
    execution_time = time.time() - process_initial_time
    print('Resultado do temporizador 3: ' + str(execution_time) + ' segundos\n')
    # Começo do temporizador 4
    print("Realizando o processo do temporizador 4:")
    process_initial_time = time.time()
    run_all_processes(temporizador4)
    ################################################
    execution_time = time.time() - process_initial_time
    print('Resultado do temporizador 4: ' + str(execution_time) + ' segundos\n')
    # Total no todo
    final_time = time.time() - initial_time
    print('Total: ' + str(final_time) + ' segundos\n')

# Funções
def temp1(number = 1, potency = 1, temporizador = 1):
    process_initial_time = time.time()
    multiplier = 2
    while(time.time() - process_initial_time < temporizador) :
        if (potency <= 1000000):
            number *= multiplier
            potency += 1
    return [number, potency]
################################################
def temp2(number = 1, potency = 1, temporizador = 1):
    process_initial_time = time.time()
    multiplier = 3
    while(time.time() - process_initial_time < temporizador):
        if (potency <= 1000000):        
            number *= multiplier
            potency += 1
    return [number, potency]
 ################################################   
def temp3(number = 1, potency = 1, temporizador = 1):
    process_initial_time = time.time()
    multiplier = 5
    while(time.time() - process_initial_time < temporizador):
        if (potency <= 1000000):
            number *= multiplier
            potency += 1
    return [number, potency]
################################################
def run_all_processes(temporizador = 1):
    temp1_numb = [1,1]
    temp2_numb = [1,1]
    temp3_numb = [1,1]
################################################
    queue = Queue()
    queue.put(1)
    queue.put(2)
    queue.put(3)
   ################################################
    while not queue.empty():
        process = queue.get()
        ################################################
        if process == 1:
            temp1_numb = temp1(temp1_numb[0], temp1_numb[1], temporizador)
            if temp1_numb[1] <= 1000000 :
                queue.put(1)
                # Finalização do primeiro processo
            else:
                print("Temporizador finalizou Primeiro processo")
        
        elif process == 2:
            temp2_numb = temp2(temp2_numb[0], temp2_numb[1], temporizador)
            if temp2_numb[1] <= 1000000 :
                queue.put(2)
                # Finalização do segundo processo
            else:
                print("Temporizador finalizou Segundo processo")

        elif process == 3:
            temp3_numb = temp1(temp3_numb[0], temp3_numb[1], temporizador)
            if temp3_numb[1] <= 1000000 :
                queue.put(3)
                # Finalização do terceiro processo
            else:
                print("Temporizador finalizou Terceiro processo")

main()