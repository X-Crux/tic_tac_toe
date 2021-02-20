def status_game(_string):
    playing_field(_string)
    count_x, count_o, count_empty = counts(_string)
    triple_counts = find_wins(_string)

    if abs(count_x - count_o) > 1 or triple_counts['value'] > 1:
        return 'Impossible', 0
    elif triple_counts['value'] == 1:
        return f"{triple_counts['key']} wins", 0
    elif count_empty > 0:
        return 'Game not finished', 1
    elif triple_counts['value'] == 0:
        return 'Draw', 0


def find_wins(_string):
    triple_counts = {'key': None, 'value': 0}
    if _string[0] == _string[1] == _string[2] and _string[0] != '_':
        triple_counts['key'] = _string[0]
        triple_counts['value'] += 1
    if _string[3] == _string[4] == _string[5] and _string[3] != '_':
        triple_counts['key'] = _string[3]
        triple_counts['value'] += 1
    if _string[6] == _string[7] == _string[8] and _string[6] != '_':
        triple_counts['key'] = _string[6]
        triple_counts['value'] += 1
    if _string[0] == _string[3] == _string[6] and _string[0] != '_':
        triple_counts['key'] = _string[0]
        triple_counts['value'] += 1
    if _string[1] == _string[4] == _string[7] and _string[1] != '_':
        triple_counts['key'] = _string[1]
        triple_counts['value'] += 1
    if _string[2] == _string[5] == _string[8] and _string[2] != '_':
        triple_counts['key'] = _string[2]
        triple_counts['value'] += 1
    if _string[0] == _string[4] == _string[8] and _string[0] != '_':
        triple_counts['key'] = _string[0]
        triple_counts['value'] += 1
    if _string[2] == _string[4] == _string[6] and _string[2] != '_':
        triple_counts['key'] = _string[2]
        triple_counts['value'] += 1
    return triple_counts


def counts(_string):
    count_x = 0
    count_o = 0
    count_empty = 0
    for i in _string:
        if i == 'X':
            count_x += 1
        elif i == 'O':
            count_o += 1
        else:
            count_empty += 1
    return count_x, count_o, count_empty


def playing_field(_string):
    print(
        f'{"-" * 9}\n'
        f'| {_string[0]} {_string[1]} {_string[2]} |\n'
        f'| {_string[3]} {_string[4]} {_string[5]} |\n'
        f'| {_string[6]} {_string[7]} {_string[8]} |\n'
        f'{"-" * 9}'
    )


def get_move(list_row, player):
    while True:
        coordinates = input('Enter the coordinates: ').split()
        first = 0
        second = 0
        try:
            first = int(coordinates[0])
            second = int(coordinates[1])
        except ValueError:
            print('You should enter numbers!')
            continue
        except IndexError:
            print('You should enter a second coordinate!')
            continue
        if first < 1 or first > 3 or second < 1 or second > 3:
            print('Coordinates should be from 1 to 3!')
        elif list_row[first - 1][second - 1] != '_':
            print('This cell is occupied! Choose another one!')
        else:
            break
    list_row[first - 1][second - 1] = player
    return ''.join(''.join(row) for row in list_row)


def game(_string, player):
    end_game = 1
    massage = ''
    new_string = _string
    while end_game == 1:
        list_rows = [list(new_string[:3]), list(new_string[3:-3]), list(new_string[6:])]
        new_string = get_move(list_rows, player)
        massage, end_game = status_game(new_string)
        if player == 'X':
            player = 'O'
        else:
            player = 'X'
    print(massage)


if __name__ == '__main__':
    start_player = 'X'
    row_in = '_________'
    playing_field(row_in)
    game(row_in, start_player)
