from utils.utils import *
import utils.config as cfg
from tensorflow.keras import models
import pickle

model = models.load_model(cfg.spam_detector_path)
# Load tokenizer
tokenizer = pickle.load(open(cfg.tokenizer_path, 'rb'))