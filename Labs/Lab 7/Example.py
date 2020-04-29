
keywords = open("keywords.txt", "r")
positive, negative, neutral = [], [], []
for line in keywords:
    word, value = line.split(",")
    value = int(value.strip("\n"))
    if value == 20:
        positive.append(word)
    elif value == -10:
        negative.append(word)
    else:
        neutral.append(word)
tweet = "I really am very happy for you I love the weather I am also sad and have some regrets about being so tired"
sumVal = 0
for word in tweet.split(" "):
    if word in positive:
        sumVal += 20
    elif word in negative:
        sumVal -= 10
print("positive: ", str(positive))
print("negative: ", str(negative))
print("neutral: ", str(neutral))
print("SumVal: ", sumVal)
