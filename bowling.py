def score(game):
    game = game.lower()
    result = 0
    frame = 1
    in_first_half = True
    for i in range(len(game)):
        if game[i] == '/':
            result += 10 - last
        else:
            result += get_value(game[i])

        last = get_value(game[i])

        if frame < 10  and last == 10:
            if is_spare(game[i]):  # if is_spare(game[i])
                result += get_value(game[i+1])
            elif game[i] == 'x':
                result += get_value(game[i+1])
                if game[i+2] == '/':
                    result += 10 - get_value(game[i+1])
                else:
                    result += get_value(game[i+2])

        if not in_first_half:
            frame += 1

        in_first_half = not in_first_half

        if game[i] == 'x':
            in_first_half = True
            frame += 1
    return result

def get_value(char):
    if char in ['x' , '/']:
        return 10
    elif char == '-':
        return 0
    elif int(char) in range(1, 10):
        return int(char)

    raise ValueError()

def is_spare(score):
    return score == '/'
