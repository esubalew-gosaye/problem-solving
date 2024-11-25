# Problem: A - Education Squad - https://codeforces.com/gym/504384/problem/A

rows = [input() for i in range(3)]
cols = ["".join([rows[i][j] for i in range(3)]) for j in range(3)]
diagonals = [
    "".join([rows[i][i] for i in range(3)]),
    "".join([rows[i][2 - i] for i in range(3)])
]
lines = rows + cols + diagonals

# To store winners
individual_winners = set()
team_winners = set()

# Check each line
for line in lines:
    unique_chars = set(line)

    # Individual winner
    if len(unique_chars) == 1:
        individual_winners.add(next(iter(unique_chars)))

    # Two-head team winner
    if len(unique_chars) == 2:
        chars = tuple(sorted(unique_chars))  # Sort to ensure uniqueness in pairs
        team_winners.add(chars)

# Output results
print(len(individual_winners))
print(len(team_winners))