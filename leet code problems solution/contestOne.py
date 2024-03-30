def game_score(n, cards):
    sereja_score = 0
    dima_score = 0

    left = 0
    right = n - 1

    for _ in range(n):
        if cards[left] > cards[right]:
            sereja_score += cards[left]
            left += 1
        else:
            sereja_score += cards[right]
            right -= 1

        if left > right:
            break

        if cards[left] > cards[right]:
            dima_score += cards[left]
            left += 1
        else:
            dima_score += cards[right]
            right -= 1

        if left > right:
            break

    return sereja_score, dima_score

# Input
n = int(input())
cards = list(map(int, input().split()))

# Calculate scores
sereja_score, dima_score = game_score(n, cards)

# Output
print(sereja_score, dima_score)
