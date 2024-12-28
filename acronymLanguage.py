def acronymLanguage(orgWords, maxLen):
    words = []
    word = []
    wordsLength = 3

    for j in range(maxLen):
        for i in orgWords:
            if j < len(i):
                if wordsLength == 3 and len(word) == 0:
                    word.append(i[j].upper())
                    wordsLength = 0
                else:
                    word.append(i[j].lower())

        if wordsLength == 2 or j == maxLen - 1:
            words.append(''.join(word) + '.')
        else:
            words.append(''.join(word))

        wordsLength += 1
        word = []
    return words

if __name__ == '__main__':
    print('\nAcronym Language')
    print('-----------------')

    again = 'y'

    while again.lower() == 'y':
        orgSentence = input('\nEnter words: ')
        orgWords = orgSentence.split(' ')
        maxLen = max(len(i) for i in orgWords)

        sentence = " ".join(acronymLanguage(orgWords, maxLen))
        print(f'\nAcronym Language: {sentence}')
        again = input('\nTranslate again? (y/n): ')
