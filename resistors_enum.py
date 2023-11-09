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

while True:
    try:
        n = int(input('[Количество резисторов] >> '))
        res_values = list(map(int, input('[Номиналы резистров] >> ').split()))
        res_set_value = int(input('[R0] >> '))
    except ValueError:
        print('Введено не число!')
        continue
    enumeration = get_enumeration(n)
    closest_value = None
    for elem in enumeration:
        sum = 0
        for val in elem: sum += res_values[val-1]
        print(f'> {[res_values[res-1] for res in elem]} <{sum}>')
        if closest_value == None:   closest_value = sum
        else: 
            if abs(sum-res_set_value) < abs(closest_value-res_set_value):
                closest_value = sum
    print(f'Ближайшее значение: {closest_value}', end='\n')
    if not input('[Повторить?(r)] >> ') == 'r':
        break