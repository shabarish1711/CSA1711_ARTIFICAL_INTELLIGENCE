def alpha_beta(tree, alpha, beta, maximizing):

    # If the node is a number, return it
    if isinstance(tree, int):
        return tree

    if maximizing:
        best = -999

        for child in tree:
            value = alpha_beta(child, alpha, beta, False)
            best = max(best, value)
            alpha = max(alpha, best)

            # Beta cutoff
            if alpha >= beta:
                break

        return best

    else:
        best = 999

        for child in tree:
            value = alpha_beta(child, alpha, beta, True)
            best = min(best, value)
            beta = min(beta, best)

            # Alpha cutoff
            if alpha >= beta:
                break

        return best


# Game tree
tree = [
    [[3, 5], [2, 9]],
    [[12, 5], [23, 23]]
]

result = alpha_beta(tree, -999, 999, True)

print("Best value:", result)
