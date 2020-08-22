from pathlib import Path

# Path to model
spam_detector_path = Path(r'../modelling/model/spam_detector.h5')

# Path to tokenizer
tokenizer_path = Path(r'../modelling/model/tokenizer.pickle')

url_regex = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
