import f as f


def wordsMastch(sentence1, sentence2):
    words1 = sentence1.strip().split(" ")
    words2 = sentence2.split(" ")
    score = 0
    for word1 in words1:
        for word2 in words2:
            if word1.lower() == word2.lower():
                score += 1
    return score

if __name__ == '__main__':
    # print(wordsMastch("My name is Prabal Gupta", "Prabal is a good boy"))
    # sentences = ["My name is Prabal Gupta", "Prabal is a good boy", "this is python", "Python is very easy",
    #              "but not too much easy", "prabal is a python developer and Python developer are nice and good"]
    with open("prabal_e.txt") as f:
        fileData = f.read()
    with open("srijan_e.txt") as f:
        file2Data = f.read()
    sentences = [fileData, file2Data]
    search = input("Search here : ")
    import time
    startTime = time.time()
    scores = [wordsMastch(search, sentence) for sentence in sentences]
    # print(scores)
    sortedFinalScores = [sortedScore for sortedScore in sorted(zip(scores, sentences), reverse=True)]
    finishTime = time.time()
    timeTaken = finishTime - startTime
    # print(sortedFinalScores)

    print(f"{len(sortedFinalScores)} results found in..({timeTaken})")
    for score, item in sortedFinalScores:
        print(f" \"{sentences}\", \nappeared {score} times.")