def count():
    count = 0
    word = input('Enter a word: ')
    letter = input('Enter a letter: ')
    for x in word:
        if x == letter:
            count += 1
    print('There are', count, 'instances of the letter', letter, 'in', word + '.')

count()
