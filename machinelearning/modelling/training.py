from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten, Conv1D, MaxPooling1D, Dropout, Activation, Input
from tensorflow.keras.layers import Embedding, LSTM

# Others
import numpy as np
import pandas as pd
from tensorflow.keras.callbacks import EarlyStopping
from sklearn.model_selection import train_test_split

from machinelearning.preprocessing.ingestionAndWrangling import text_to_wordlist


def read_data():
    data = pd.read_csv(r"data/email_data.csv")
    data['text'] = data['text'].apply(text_to_wordlist)


def model_training():
    data = read_data()
    tokenizer = Tokenizer()
    tokenizer.fit_on_texts(data['text'])
    vocab_size = len(tokenizer.word_index) + 1
    sequences = tokenizer.texts_to_sequences(data['text'])
    max_len = 300
    padded_docs = pad_sequences(sequences, maxlen=max_len, padding='post')
    labels = np.array(data['spam'])
    embeddings_index = dict()
    f = open(r'data/glove.6B.100d.txt', encoding="utf8")
    for line in f:
        values = line.split()
        word = values[0]
        coefs = np.asarray(values[1:], dtype='float32')
        embeddings_index[word] = coefs
    f.close()
    print('Loaded %s word vectors.' % len(embeddings_index))
    embedding_matrix = np.zeros((vocab_size, 100))
    for word, index in tokenizer.word_index.items():
        embedding_vector = embeddings_index.get(word)
        if embedding_vector is not None:
            embedding_matrix[index] = embedding_vector
    model = Sequential()
    model.add(Embedding(vocab_size, 100, weights=[embedding_matrix], input_length=max_len, trainable=True))
    model.add(Conv1D(64, 2, activation='relu'))
    model.add(MaxPooling1D(2))
    model.add(Dropout(0.3))
    model.add(Conv1D(128, 2, activation='relu'))
    model.add(MaxPooling1D(2))
    model.add(Dropout(0.3))
    model.add(Conv1D(256, 2, activation='relu'))
    model.add(MaxPooling1D(2))
    model.add(Dropout(0.3))
    model.add(Flatten())
    model.add(Dense(1, activation='sigmoid'))
    # compile the model
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    # summarize the model
    print(model.summary())

    X_train, X_test, y_train, y_test = train_test_split(padded_docs, labels, test_size=0.2, random_state=42)

    class_weight = {0: 1.,
                    1: 3.3}

    early_stop = EarlyStopping(monitor='val_loss', restore_best_weights=True, patience=5)

    model.fit(X_train, y_train, epochs=50, batch_size=32, validation_split=0.2, callbacks=[early_stop],
              class_weight=class_weight)
    # evaluate the model
    loss, accuracy = model.evaluate(X_test, y_test, verbose=0)
    print('Accuracy: %f' % (accuracy * 100))
    model.save(r'model/spam_detector.h5')
