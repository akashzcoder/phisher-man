from tensorflow.keras import models
import pickle
from tensorflow.keras.preprocessing import sequence

from machinelearning.preprocessing.ingestionAndWrangling import text_to_wordlist
from machinelearning.utils import config


def predict(email: str):
    model = models.load_model(config.spam_detector_path)
    # Load tokenizer
    tokenizer = pickle.load(open(config.tokenizer_path, 'rb'))
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
