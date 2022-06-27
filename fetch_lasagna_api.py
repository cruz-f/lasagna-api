import requests


url = "http://127.0.0.1:5000/submit"

sequences = {
    'sequences': [
        'GGACAAGTTGAAACTTGCAC',
        'AAACATGTCAGCACTTGCTT',
        'CAGCATGTTCACACAAGCCA',
        'GGGCCTGTCTCCAACTTGCCC',
        'GGGCATGTGCATTCAAGTTT',
        'GGTCTTGTTTAGACTTGCTC',
        'GGGCTTCAGGGCGCATGCCC',
        'AGGCAAGATGAAACATATCA',
        'TCACAAGTTAGAGACAAGCCTGGGCGTGGGC',
        'GGACAAGCCCTGACAAGCCA',
        'GGAAGTGACG',
        'AGAGGACGGGGCGTGCCCCGACGTG',
        'GGGCATGTCCGGGCAA'

    ],
    'headers': [
        'site_0',
        'site_1',
        'site_2',
        'site_3',
        'site_4',
        'site_5',
        'site_6',
        'site_7',
        'site_8',
        'site_9',
        'site_10',
        'site_11',
        'site_12'
    ]}

payload = {'sequences': sequences, 'k': 0}

response = requests.request("POST", url, json=payload)

print(response.json())
