class SentimentAnalysis(object):
    dict_word_polarity = {}
    count_positive = 0;
    count_negative = 0;
    count_default = 0;


    def __init__(self):
        sentilexpt = open(r"C:\Users\Admin\dev\SentiLex-lem-PT02.txt",'r')

        for i in sentilexpt.readlines():
            after_dot = i.find('.')
            word = (i[:after_dot])
            after_pol = i.find('POL')
            polarity = (i[after_pol+4:after_pol+6]).replace(';','')
            self.dict_word_polarity[word] = polarity

    def score_sentiment(self, sentence):
        sentence = sentence.lower()
        list_sentiment = []
        for w in sentence.split():
            list_sentiment.append(int(self.dict_word_polarity.get(w, 0)))
        score = sum(list_sentiment)
        if score > 0:
            self.count_positive += 1
        elif score == 0:
            self.count_default += 1
        else:
            self.count_negative += 1

    def get_sentiment_result(self):
        list_sentiment_result = [self.count_positive, self.count_default, self.count_negative]
        return list_sentiment_result