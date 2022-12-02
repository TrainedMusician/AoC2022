def read_file(file_path):
    return open(file_path).read().split('\n')


def play_games(content):
    score = 0
    moves = {
        'A': 1,  # Rock
        'B': 2,  # Paper
        'C': 3,  # Scissors
        'X': 1,  # Rock
        'Y': 2,  # Paper
        'Z': 3,  # Scissors
    }
    textual = {
        1: 'Rock',
        2: 'Paper',
        3: 'Scissors'
    }
    for game in content:
        opponent, you = game.split(' ')
        opponent, you = moves[opponent], moves[you]

        # Wins
        # A Y  1 2
        # B Z  2 3
        # C X  3 1

        # Ties
        # A X  1 1
        # B Y  2 2
        # C Z  3 3

        # Loses
        # A Z  1 3
        # B X  2 1
        # C Y  3 2

        if you - 1 == opponent or (you == 1 and opponent == 3):
            status = 'You Win!'
            tmp = 6
        elif opponent == you:
            status = 'Tie!'
            tmp = 3
        else:
            status = 'You lose..'
            tmp = 0
        print('You do %s against %s\t%d vs %d\t%s\t(%d + %d) + %d = %d' % (
            textual[you],
            textual[opponent],
            you,
            opponent,
            status,
            you,
            tmp,
            score,
            score + you + tmp
        ))
        score += you + tmp
        print(score)
    return score


def optimal_wins(content):
    score = 0
    scores_opponent = {
        'A': 1,
        'B': 2,
        'C': 3,
        'X': 1,
        'Y': 2,
        'Z': 3
    }
    moves_winning = {
        1: 2,
        2: 3,
        3: 1
    }
    moves_losing = {
        1: 3,
        2: 1,
        3: 2
    }
    for game in content:
        opponent, you = game.split(' ')
        if you == 'Y':
            # Tie
            score += 3 + scores_opponent[opponent]
        elif you == 'X':
            score += 0 + moves_losing[scores_opponent[opponent]]
        else:
            score += 6 + moves_winning[scores_opponent[opponent]]
        # print(score)
    return score


if __name__ == '__main__':
    # print(play_games(read_file('../inputs/deux.txt')))
    print(optimal_wins(read_file('../inputs/deux.txt')))