from itertools import permutations

def solve():
    word1 = input("Enter first word: ").upper()
    word2 = input("Enter second word: ").upper()
    result = input("Enter result word: ").upper()

    letters = ""
    for ch in word1 + word2 + result:
        if ch not in letters:
            letters += ch

    for p in permutations("0123456789", len(letters)):
        d = dict(zip(letters, p))

        if d[word1[0]] == '0' or d[word2[0]] == '0' or d[result[0]] == '0':
            continue

        n1 = int("".join(d[ch] for ch in word1))
        n2 = int("".join(d[ch] for ch in word2))
        n3 = int("".join(d[ch] for ch in result))

        if n1 + n2 == n3:
            print("\nSolution Found")
            print(word1, "=", n1)
            print(word2, "=", n2)
            print(result, "=", n3)
            return

    print("No Solution Found")

solve()
