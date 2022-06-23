from flask import Flask
from flask import request

from lasagna import Align

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return 'my lasagna API'


@app.route('/submit', methods=['POST'])
def submit():
    result = request.get_json()
    fasta_file = result['sequences']
    k = 0

    return Align(fasta_file, k)


