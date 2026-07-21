n = int(input())
for _ in range(n):
    word = input()
    length = len(word)
    if length <= 10:
        print(word)
    else:
        first_letter = word[0]
        last_letter = word[length - 1]
        middle_count = length - 2
        result = first_letter + str(middle_count) + last_letter
        print(result)