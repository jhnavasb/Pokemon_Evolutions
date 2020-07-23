from evolution.models import pokemon, chain
import requests

url1 = 'https://pokeapi.co/api/v2/evolution-chain/{id}'
url2 = 'https://pokeapi.co/api/v2/pokemon/{id}'


def get_evolutions(res):
    evo_url = {
        '0': [],
        '1': [],
        '2': []
    }
    e_chain = []

    try:
        evo_url['0'].append(res['chain']['species']['url'])
        e_chain.append(res['chain']['species']['name'])
        for x in res['chain']['evolves_to']:
            evo_url['1'].append(x['species']['url'])
            e_chain.append(x['species']['name'])
            for y in x['evolves_to']:
                evo_url['2'].append(y['species']['url'])
                e_chain.append(y['species']['name'])
    except:
        pass

    return [evo_url, e_chain]


def evo_chain(id):
    url = url1.format(id=id)
    try:
        response = requests.get(url).json()
    except:
        return "unavailable"

    evo_list, evo_names = get_evolutions(response)
    for k, v in evo_list.items():
        for item in v:
            pokedb(item, k, id)

    return evo_names


def temp():
    for x in range(1, 428):
        print(evo_chain(x))
    return "done"


def get_id(url):
    s = url.split('/')
    return s[-2]


def pokedb(url_id, rank, n):
    id = get_id(url_id)
    url = url2.format(id=id)
    response = requests.get(url)
    response = response.json()

    c = chain(id=int(n))
    c.save()
    p = pokemon(
        id=int(response['id']),
        name=response['name'],
        height=int(response['height']),
        weight=int(response['weight']),
        hp=int(response['stats'][0]['base_stat']),
        attack=int(response['stats'][1]['base_stat']),
        defense=int(response['stats'][2]['base_stat']),
        special_attack=int(response['stats'][3]['base_stat']),
        special_defense=int(response['stats'][4]['base_stat']),
        speed=int(response['stats'][5]['base_stat']),
        rank=int(rank),
        evo_chain=c
    )
    p.save()


def poke(name, rank, chain):
    url = url2.format(name=name)
    response = requests.get(url).json()

    info = {
        'id': response['id'],
        'name': name,
        'height': response['height'],
        'weight': response['weight'],
        'stats': {
            'hp': response['stats'][0]['base_stat'],
            'atk': response['stats'][1]['base_stat'],
            'def': response['stats'][2]['base_stat'],
            'satk': response['stats'][3]['base_stat'],
            'sdef': response['stats'][4]['base_stat'],
            'spd': response['stats'][5]['base_stat']
        },
        'rank': rank,
        'chain': chain
    }

    return info
