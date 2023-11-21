def perm(ls):
    if len(ls) == 0:
        return []
    elif len(ls) == 1:
        return [ls]
    else:
        res = []
        for i in range(len(ls)):
            cur_elem = ls[i]
            else_elems = ls[:i] + ls[i+1:]
            for j in perm(else_elems):
                res.append([cur_elem] + j)
        return res

while True:
    with open('data.txt') as file:
        n = int(file.readline().rstrip())
        boxes = [list(map(int, box.split())) for box in file.readline().rstrip().split(',')]
    perms = perm(list(range(n)))
    best_perm, best_time = [], float('inf')
    for perm in perms:
        time = 0
        for i in range(len(perm)):
            if i == 0:
                time += boxes[perm[i]][0]
            else:
                if boxes[perm[i-1]][1] > boxes[perm[i]][0]:
                    time += boxes[perm[i-1]][1]
                else:
                    time += boxes[perm[i]][0]
        if time < best_time:    best_time, best_perm = time, perm
    print(f'Время обработки коробок: {best_time}')
    print(f'Порядок подачи коробок: {[boxes[ind] for ind in best_perm]}')
    break
