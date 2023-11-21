import timeit

def get_n_base_num(num: int, base: int, n: int) -> str:
    res = ''
    while num > 0:
        dig = num % base
        res += str(dig)
        num //= base
    if len(res) < n:
        res = '0'*(n-len(res)) + res[::-1]
    else:
        res = res[::-1]
    return res

TEAMS_COUNT = 3
works = []
teams = [0] * TEAMS_COUNT
greedy_iters = 0
enum_iters = 0

with open('data.txt') as file:
    for line in file:
        works.append(list(map(int, line.rstrip().split('\t'))))
n = len(works)
greedy_begin = timeit.default_timer()
greedy_best_option = ''
for work in works:
    greedy_iters += 1
    m_work = min(work)
    teams[work.index(m_work)] += m_work
    greedy_best_option += str(work.index(m_work))

greedy_end = timeit.default_timer()
greedy_time_execution = greedy_end - greedy_begin
greedy_value = max(teams)
print(f'Жадный алгоритм >> Результат: {greedy_value}, Решение: {greedy_best_option}, Время выполнения: {greedy_time_execution*1000:.2f} мс, Кол-во итераций: {greedy_iters}')

enum_min = float('inf')
enum_best_option = 0
enum_begin = timeit.default_timer()
for i in range(TEAMS_COUNT**n):
    inter_teams = [0]*TEAMS_COUNT
    enum_iters += 1
    pos = get_n_base_num(i, TEAMS_COUNT, n)
    for k, j in enumerate(pos):
        inter_teams[int(j)] += works[k][int(j)]
    res_teams_work = max(inter_teams)
    if res_teams_work < enum_min:   enum_min, enum_best_option = res_teams_work, pos

enum_end = timeit.default_timer()
enum_time_execution = enum_end - enum_begin
print(f'Перебор всех вариантов >> Результат: {enum_min}, Решение: {enum_best_option}, ', end='')
if enum_time_execution > 1:
    print(f'Время выполнения: {enum_time_execution:.2f} с, Кол-во итераций: {enum_iters}', end='')
else:
    print(f'Время выполнения: {enum_time_execution*1000:.2f} мс, Кол-во итераций: {enum_iters}', end='')