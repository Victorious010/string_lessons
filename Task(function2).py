def to_weird(words):
    result = []
    for word in words.split():
        preresult = ''
        for i in range(len(word)):
            if i % 2:
                preresult += word[i].lower()
            else:
                preresult += word[i].upper()
        result.append(preresult)
    return ' '.join(result)


strin = "Hello"
print(to_weird(strin))
