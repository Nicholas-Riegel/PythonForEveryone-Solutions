def countMethod():
    word = input('Enter a word: ')
    letter = input('Enter a letter: ')
    count = word.count(letter)
    print('There are', count, 'instances of the letter', letter, 'in', word + '.')
    
countMethod()
