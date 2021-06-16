from django.shortcuts import render
import requests


# Create your views here.


def get_type(img):
    data = {
        'QmVrg1EWUe15WmAJtUr2cf5Le6TatwH9Ed7qrkD6xVPqfN': 0,  # Test
        'QmWcWnQtu5iAT9TxNYHqtoSooswvbpJgQPUwjzu1ihb7nS': 1,  # Golden Mega
        'QmXUMMThuxypj5fNgp3bnCuWwbUEQsZi5THdETyyKisg8x': 2,  # Golden Mini
        'QmW5w5kczjfwrTNahwxFx63J6bS2y68tEfqEHozVffDsQr': 3,  # Silver Mega
        'QmZHU9toJGB2aZ4Xy7LG3BZ6ThEESyRuViJrUaMw83bfGA': 4,  # Silver Mini
        'QmVWLMawR76ELRC2hqQgdAcC3tFVrAevrLgGUNdnRVWkLP': 5,  # Bronze Mega
        'Qma8VokEZCNHiRK1HJJUCSviTBxzAyC4avLh67VtGTpn5M': 6   # Bronze Mini
    }

    return data[img]


def index(request):
    return render(request, 'main.html',
                  {'title': 'WaxRaffle',
                   'selected': 0})


def purchase(request):
    return render(request, 'purchase.html',
                  {'title': 'Purchase',
                   'selected': 1})


def inventory(request):
    params = {
        'page': 'null',
        'limit': 200,
        'collection_name': 'thewaxraffle',
        'schema_name': '',
        'order': 'transferred_at_time',
        'sort': 'desc',
        'owner': 'e.hba.wam'  # request.user.username
    }
    req = requests.get('https://wax.api.atomicassets.io/atomicassets/v1/assets', params).json()
    packs = [{'aid': pack['asset_id'],
              'tp': get_type(pack['data']['img']),
              'mint': pack['template_mint']
              }
             for pack in req['data']]
    packs.sort(key=lambda x: x['tp'])
    return render(request, 'inventory.html',
                  {'title': 'Try Your Luck',
                   'selected': 2,
                   'packs': packs})
