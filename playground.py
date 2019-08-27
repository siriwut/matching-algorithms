# Gestalt Pattern Matching algorithm
# https://en.wikipedia.org/wiki/Gestalt_Pattern_Matching

from difflib import SequenceMatcher
import statistics

product1 = [{
    'name': 'CONVERSE One Star Psy-Kicks Slip - Black',
    'image': 'https://img.com/converse-1',
    'price': 2390.00,
    'attributes': {
        'brand': 'CONVERSE',
        'color': 'BLACK',
        'model_number': 'A1234',
    }
},
 {
     'name': 'CONVERSE ONE STAR PSY-KICKS SLIP BLACK',
     'image': 'https://img.com/converse-2',
     'price': 2390.00,
     'attributes': {
         'brand': 'CONVERSE',
         'color': 'ดำ',
         'model_number': 'A1234',
     }
 }]

product2 = [{
    'name': 'CONVERSE One Star Psy-Kicks Slip - Black',
    'image': 'https://img.com/converse-1',
    'price': 2390.00,
    'attributes': {
        'brand': 'CONVERSE',
        'color': 'BLACK',
        'model_number': 'A1234',
    }
},
 {
     'name': 'CONVERSE ONE STAR PSY-KICKS SLIP BLACK',
     'image': 'https://img.com/converse-2',
     'price': 2390.00,
     'attributes': {
         'brand': 'CONVERSE',
         'color': 'ดำ',
         'model_number': 'A1234',
     }
 }]





def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()


# def match_product(p1, p1):


def main():
    name1 = similar(product1[0]['name'], product1[1]['name'])
    brand1 = similar(product1[0]['attributes']['brand'], product1[1]['attributes']['brand'])
    color1 = similar(product1[0]['attributes']['color'], product1[1]['attributes']['color'])

    name2 = similar(product2[0]['name'], product2[1]['name'])
    brand2 = similar(product2[0]['attributes']['brand'], product2[1]['attributes']['brand'])
    color2 = similar(product2[0]['attributes']['color'], product2[1]['attributes']['color'])


    print('--MEAN1--')
    avg1 = statistics.mean([name1, brand1, color1])
    print(avg1)


    print('--MEAN2--')
    avg2 = statistics.mean([name2, brand2, color2])
    print(avg2)

    # print(similar('60.00', '55.00'))
    # print(similar('50', '55'))

    # print(value2)
    # print(value2)
    # print(value1)
    # print(value2)

main()
