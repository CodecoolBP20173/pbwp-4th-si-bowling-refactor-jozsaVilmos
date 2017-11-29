def score(game):
    game = game.lower()
    result = 0
    frame = 1
    in_first_half = True
    frame_limit = 10
    for i in range(len(game)):
        if is_spare(game[i]):
            result += get_value("x") - last
        else:
            result += get_value(game[i])

        last = get_value(game[i])

        if frame < frame_limit  and last == get_value("x"):
            next_score = get_value(game[i+1])
            if is_spare(game[i]):
                result += next_score
            elif game[i] == 'x':
                result += next_score
                if is_spare(game[i+2]):
                    result += get_value("x") - next_score
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
