import string
import re
from pathlib import Path

from tensorflow.keras import models
import pickle
from tensorflow.keras.preprocessing import sequence


# Path to model
spam_detector_path = Path(r'model/spam_detector.h5')

# Path to tokenizer
tokenizer_path = Path(r'model/tokenizer.pickle')

url_regex = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'


def text_to_wordlist(text):
    # Remove puncuation
    text = text.translate(string.punctuation)
    # Convert words to lower case and split them
    text = text.lower().split()

    # Remove stop words
    # stops = set(stopwords.words("english"))
    # text = [w for w in text if not w in stops and len(w) >= 3]

    text = " ".join(text)
    # Clean the text
    text = re.sub(r"[^A-Za-z0-9^,!.\/'+-=]", " ", text)
    text = re.sub(r"what's", "what is ", text)
    text = re.sub(r"\'s", " ", text)
    text = re.sub(r"\'ve", " have ", text)
    text = re.sub(r"n't", " not ", text)
    text = re.sub(r"i'm", "i am ", text)
    text = re.sub(r"\'re", " are ", text)
    text = re.sub(r"\'d", " would ", text)
    text = re.sub(r"\'ll", " will ", text)
    text = re.sub(r",", " ", text)
    text = re.sub(r"\.", " ", text)
    text = re.sub(r"!", " ! ", text)
    text = re.sub(r"\/", " ", text)
    text = re.sub(r"\^", " ^ ", text)
    text = re.sub(r"\+", " + ", text)
    text = re.sub(r"\-", " - ", text)
    text = re.sub(r"\=", " = ", text)
    text = re.sub(r"'", " ", text)
    text = re.sub(r"(\d+)(k)", r"\g<1>000", text)
    text = re.sub(r":", " : ", text)
    text = re.sub(r" e g ", " eg ", text)
    text = re.sub(r" b g ", " bg ", text)
    text = re.sub(r" u s ", " american ", text)
    text = re.sub(r"\0s", "0", text)
    text = re.sub(r" 9 11 ", "911", text)
    text = re.sub(r"e - mail", "email", text)
    text = re.sub(r"j k", "jk", text)
    text = re.sub(r"\s{2,}", " ", text)
    return text


def predict(email: str):
    model = models.load_model(spam_detector_path)
    # Load tokenizer
    tokenizer = pickle.load(open(tokenizer_path, 'rb'))
    prediction = predict_spam(email, model, tokenizer)
    print(prediction)
    return prediction


def predict_spam(email_text, model, tokenizer):
    """
    :param email_text: an email that needs to be detected as email or not
    :param model: loaded model for prediction email
    :param tokenizer: process given email text to tokens
    :return: probability of detected threat, the value lay between 0 to 1
    """
    processed_text = text_to_wordlist(email_text)
    tokens = tokenizer.texts_to_sequences([processed_text])
    paded_sequences = sequence.pad_sequences(tokens, maxlen=300, padding='post')
    prediction = model.predict(paded_sequences)
    return prediction[0][0]
