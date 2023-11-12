import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

def get_emotion(sentence):
    # Initialize the sentiment analyzer
    sid = SentimentIntensityAnalyzer()

    # Get the sentiment scores for the sentence
    sentiment_scores = sid.polarity_scores(sentence)

    # Determine the emotion based on the sentiment scores
    if sentiment_scores['compound'] >= 0.05:
        emotion = 'Positive'
    elif sentiment_scores['compound'] <= -0.05:
        emotion = 'Negative'
    else:
        emotion = 'Neutral'

    # Calculate the emotion score
    emotion_score = (sentiment_scores['compound'] + 1) * 50

    return emotion, emotion_score

# Test the function
sentence = "I'm absolutely thrilled and overjoyed with the amazing news!" #<-Sample Sentence
emotion, emotion_score = get_emotion(sentence)
print("Emotion:", emotion)
print("Emotion Score:", emotion_score)
