import random
import time

def get_enumeration(n: int) -> list:
    res = []
    stack = [0]*(n+1)
    k = 0
    while True:
        if stack[k] < n:
            stack[k+1] = stack[k] + 1
            k += 1
        else:
            stack[k-1] += 1
            k -= 1
        if k == 0: break
        res.append(stack[1:k+1])
    return res

def get_bin_enumeration(n: int, res_values: list) -> list:
    res_set_value = 50
    res = []
    closest_value = None
    for i in range(2**n):
        sum = 0
        num = f'0b{i:0{n}b}'
        for j, n in enumerate(num[:1:-1]):
            if n == '1':
                sum += res_values[j]
        if closest_value == None:   closest_value = sum
        else: 
            if abs(sum-res_set_value) < abs(closest_value-res_set_value):
                closest_value = sum
    print(f'Ближайшее значение: {closest_value}', end='\n')

# list(map(int, input('[Номиналы резистров] >> ').split()))
# int(input('[R0] >> '))

while True:
    try:
        n = int(input('[Количество резисторов] >> '))
        res_values = [random.randint(1, 100) for _ in range(n)]
    except ValueError:
        print('Введено не число!')
        continue
    except KeyboardInterrupt:
        break
    res_set_value = 50
    st_t1 = time.time()
    enumerate = get_enumeration(n)
    res1 = time.time() - st_t1
    st_t2 = time.time()
    closest_value = None
    for el in enumerate:
        sum = 0
        for val in el: sum += res_values[val-1]
        if closest_value == None:   closest_value = sum
        else: 
            if abs(sum-res_set_value) < abs(closest_value-res_set_value):
                closest_value = sum
    res2 = time.time() - st_t2
    print(f'Время: {res1} {res2} {res1+res2}')