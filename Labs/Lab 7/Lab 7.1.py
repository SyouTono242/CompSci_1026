TWEET = "I really am very happy for you I love the weather I am also sad and have some regrets about being so tired"

NEGATIVE_WORDS, NEUTRAL_WORDS, POSITIVE_WORDS = [], [], []

text = open("keywords.txt", "r")
for x in range(0,10):
    line = text.readline()
    words = line.rsplit(',')
    if int(words[1]) == 20:
        POSITIVE_WORDS.append(words[0])
    elif int(words[1]) == 0:
        NEUTRAL_WORDS.append(words[0])
    elif int(words[1]) == -10:
        NEGATIVE_WORDS.append(words[0])
print("The positive keywords are", POSITIVE_WORDS,
      "\nThe negative keywords are", NEGATIVE_WORDS,
      "\nThe neutral keywords are", NEUTRAL_WORDS)

tweetWords = TWEET.rsplit()
sentiment = 0
for word in tweetWords:
    if word in POSITIVE_WORDS:
        sentiment = sentiment + 20
    elif word in NEGATIVE_WORDS:
        sentiment = sentiment - 10
print("The sentiment of the tweet is", sentiment)
