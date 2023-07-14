from flask import Flask, request
import os
import math
import datetime

from tqdm import tqdm

import pandas as pd
import numpy as np

import tensorflow as tf
from tensorflow import keras

import bert
from bert import BertModelLayer
from bert.loader import StockBertConfig, map_stock_config_to_params, load_stock_weights
from bert.tokenization.bert_tokenization import FullTokenizer
RANDOM_SEED = 42
np.random.seed(RANDOM_SEED)
tf.random.set_seed(RANDOM_SEED)

train=pd.read_csv("train.csv")
valid=pd.read_csv("valid.csv")
test=pd.read_csv("test.csv")

train = pd.concat([train, valid]).reset_index(drop=True)


bert_model_name="uncased_L-12_H-768_A-12"

bert_ckpt_dir = os.path.join("model/", bert_model_name)
bert_ckpt_file = os.path.join(bert_ckpt_dir, "bert_model.ckpt")
bert_config_file = os.path.join(bert_ckpt_dir, "bert_config.json")
bert_ckpt_file = bert_ckpt_file.replace("\\", "/")



class IntentDetectionData:
  DATA_COLUMN = "text"
  LABEL_COLUMN = "intent"

  def __init__(self, train, test, tokenizer: FullTokenizer, classes, max_seq_len=192):
    self.tokenizer = tokenizer
    self.max_seq_len = 0
    self.classes = classes

    train, test = map(lambda df: df.reindex(df[IntentDetectionData.DATA_COLUMN].str.len().sort_values().index), [train, test])

    ((self.train_x, self.train_y), (self.test_x, self.test_y)) = map(self._prepare, [train, test])

    print("max seq_len", self.max_seq_len)
    self.max_seq_len = min(self.max_seq_len, max_seq_len)
    self.train_x, self.test_x = map(self._pad, [self.train_x, self.test_x])

  def _prepare(self, df):
    x, y = [], []

    for _, row in tqdm(df.iterrows()):
      text, label = row[IntentDetectionData.DATA_COLUMN], row[IntentDetectionData.LABEL_COLUMN]
      tokens = self.tokenizer.tokenize(text)
      tokens = ["[CLS]"] + tokens + ["[SEP]"]
      token_ids = self.tokenizer.convert_tokens_to_ids(tokens)
      self.max_seq_len = max(self.max_seq_len, len(token_ids))
      x.append(token_ids)
      y.append(self.classes.index(label))

    return np.array(x), np.array(y)

  def _pad(self, ids):
    x = []
    for input_ids in ids:
      input_ids = input_ids[:min(len(input_ids), self.max_seq_len - 2)]
      input_ids = input_ids + [0] * (self.max_seq_len - len(input_ids))
      x.append(np.array(input_ids))
    return np.array(x)


tokenizer = FullTokenizer(vocab_file=os.path.join(bert_ckpt_dir, "vocab.txt"))

classes = train.intent.unique().tolist()

model = keras.models.load_model("TrainedModelBertBankSystem")

app = Flask(__name__)

@app.route("/processText", methods=["POST"])
def process_text():
    textFromNodeServer = request.json["text"]
    print("Received text:", textFromNodeServer)

    tokenizeSentence=tokenizer.tokenize(textFromNodeServer)
    print(tokenizeSentence)
    tokenizeSentenceID=tokenizer.convert_tokens_to_ids(tokenizeSentence)
    print(tokenizeSentenceID)

    pred_token_ids = [tokenizeSentenceID + [0] * (98 - len(tokenizeSentenceID))]
    pred_token_ids = np.array(pred_token_ids)

    intent_prediction = model.predict(pred_token_ids).argmax(axis=-1)[0]
    intent_label = classes[intent_prediction]

    return intent_label

    # return "Text intent processed successfully"
#38 for normal bank system max seq len 98

if __name__ == "__main__":
    app.run()
