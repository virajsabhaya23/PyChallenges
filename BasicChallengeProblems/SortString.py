def sort_words(userInput):
    return (' '.join(sorted(userInput.split(), key=str.casefold)))

print(sort_words('banana ORANGE apple'))