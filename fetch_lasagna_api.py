import pandas as pd
import requests

url = "http://127.0.0.1:5000/submit"

sequences = {
    'sequences': [
        'GACCAATGATTATTAGCCAAT',
        'GGCCAGCCTTGCCTTGACCAATAGCCTTGACAAGGCAAACTT',
        'CCCGAGCCGCTGATTGGCTTTCAGG',
        'ACCAATGACTTTTAAGTACC',
        'CCAAT'

    ],
    'headers': [
        'site_0',
        'site_1',
        'site_2',
        'site_3',
        'site_4'
    ]}

payload = {'sequences': sequences, 'k': 0}

response = requests.request("POST", url, json=payload)

print(response.json())


