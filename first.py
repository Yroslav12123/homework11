def strings_longer_than_ten(strings):
    long_strings = [s for s in strings if len(s) > 10]
    print(f"Список стрічок довжиною більше 10 символів: {long_strings}")
    return long_strings

strings = ['Ця стрічка набагато більше за 10 символів']
result = strings_longer_than_ten(strings)

