FIRST_SYMBOL = '>'
SECOND_SYMBOL = '<'
SPACE_SYMBOL = ' '

while True:
    try:
        n = int(input('Введите число кенгуру >> '))
    except ValueError:
        print('Введено не число!')
        continue
    except KeyboardInterrupt:
        print('\nВыход из программы...')
        break
    begin_pos = FIRST_SYMBOL*n + ' ' + SECOND_SYMBOL*n
    final_pos = begin_pos[::-1]
    positions = [[begin_pos]]
    while True:
        cur_branch = positions.pop()
        cur_pos = cur_branch[-1]
        if cur_pos == final_pos:
            positions = cur_branch
            break
        indexes = [cur_pos.find(f'{FIRST_SYMBOL}{SPACE_SYMBOL}'), 
                   cur_pos.find(f'{FIRST_SYMBOL}{SECOND_SYMBOL}{SPACE_SYMBOL}'),
                   cur_pos.find(f'{SPACE_SYMBOL}{SECOND_SYMBOL}'),
                   cur_pos.find(f'{SPACE_SYMBOL}{FIRST_SYMBOL}{SECOND_SYMBOL}')]
        if indexes == [-1]*4:
            continue
        for i in range(len(indexes)):
            if indexes[i] != -1:
                next_move, move_index = i, indexes[i]
                match next_move:
                    case 0:
                        add_pos = cur_pos[0:move_index] + f'{SPACE_SYMBOL}{FIRST_SYMBOL}' + cur_pos[move_index+2:]
                    case 1:
                        add_pos = cur_pos[0:move_index] + f'{SPACE_SYMBOL}{SECOND_SYMBOL}{FIRST_SYMBOL}' + cur_pos[move_index+3:]
                    case 2:
                        add_pos = cur_pos[0:move_index] + f'{SECOND_SYMBOL}{SPACE_SYMBOL}' + cur_pos[move_index+2:]
                    case 3:
                        add_pos = cur_pos[0:move_index] + f'{SECOND_SYMBOL}{FIRST_SYMBOL}{SPACE_SYMBOL}' + cur_pos[move_index+3:]
                positions.append(cur_branch + [add_pos])
    for i, step in enumerate(positions):
        print(f'Шаг {i}: {step}')
