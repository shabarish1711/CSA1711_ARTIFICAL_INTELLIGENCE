def maximum(a, b):
    if a > b:
        return a
    return b


def minimum(a, b):
    if a < b:
        return a
    return b


def minimax(tree, level, max_player):
    if level == 2:
        return tree

    if max_player:
        left = minimax(tree[0], level + 1, False)
        right = minimax(tree[1], level + 1, False)
        return maximum(left, right)

    else:
        left = minimax(tree[0], level + 1, True)
        right = minimax(tree[1], level + 1, True)
        return minimum(left, right)


tree = [
    [[3, 5], [2, 9]],
    [[12, 5], [23, 23]]
]

answer = minimax(tree, 0, True)

print("Best value:", answer)

