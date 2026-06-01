import re
from nltk.sentiment import SentimentIntensityAnalyzer

text = """
The smart way to keep people passive and obedient is to strictly limit the spectrum of acceptable opinion, but allow very lively debate within that spectrum – even encourage the more critical and dissident views.
That gives people the sense that there’s free thinking going on, while all the time the presuppositions of the system are being reinforced by the limits put on the range of the debate.
"""
words = re.findall(r"\b\w+(?:ed|ing)\b", text)
sia = SentimentIntensityAnalyzer()
score = sia.polarity_scores(text)
print("Words ending in -ed or -ing:")
print(words)
print("\nSentiment score:")
print(score["compound"])