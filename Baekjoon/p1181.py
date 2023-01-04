
def solution():
    wordnum = int(input())
    words = dict()
    for _ in range(wordnum):
        word = input()
        if words.get(len(word))==None:
            words[len(word)] = [word]
        else:
            words[len(word)] += [word]
    wordlen = list(words.keys())
    wordlen.sort()
    for length in wordlen:
        wordlist = words[length]
        wordlist = list(set(wordlist))
        wordlist.sort()
        for w in wordlist:
            print(w)

if __name__=="__main__":
    solution()
