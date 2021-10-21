import random
words_bank = ['tree','flower','blue','coffee','apple','glasses','book']
jun = 7
m = ''
user_word = ''
user_true_chars = []

word = random.choice(words_bank)

while True:
    for i in range(len(word)):
        if word[i] in user_true_chars:
            print(word[i],end = ' ')
        else:
            print('_',end = ' ')

    user_char = input('\nplease enter a character : ')

    if user_char in word:
        user_true_chars.append(user_char)
        print('YES')
    else:
        jun -= 1 
        print('NO')

    # for i in range(0,len(user_true_chars)):
    #     m = ''.join(user_true_chars[i])
    #     user_word = user_word+''+m
    #     print(user_word)
    a = b = 0
    array_true_word = word.split()
    for i in user_true_chars:
        for j in array_true_word:
            if user_true_chars[i] == array_true_word[j]:
                a = 1
                break
        
    if user_word == word:
        print('YOU WIN !!! (-:')
        break

    if jun == 0:
        print('GAME OVER !!!')
        break