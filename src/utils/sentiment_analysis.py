def analyze_sentiment(tweet):
    from textblob import TextBlob

    analysis = TextBlob(tweet)
    score = analysis.sentiment.polarity

    if score > 0:
        label = 'positive'
    elif score < 0:
        label = 'negative'
    else:
        label = 'neutral'

    return score, label