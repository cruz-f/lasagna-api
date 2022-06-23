from typing import List

import pandas as pd
from flask import Flask
from flask import request

from lasagna import Align

app = Flask(__name__)


def relative_frequency(*args, **kwargs):
    kwargs['normalize'] = True
    return pd.value_counts(*args, **kwargs)


def make_pwm(sequences: List[str]) -> pd.DataFrame:
    df = pd.DataFrame([list(seq) for seq in sequences])
    pwm = df.apply(relative_frequency)
    pwm = pwm.fillna(0)
    pwm = pwm.transpose()
    return pwm


@app.route('/', methods=['GET'])
def home():
    return 'my lasagna API'


@app.route('/submit', methods=['POST'])
def submit():
    result = request.get_json()
    fasta_file = result['sequences']
    k = 0

    return Align(fasta_file, k).to_dict()


