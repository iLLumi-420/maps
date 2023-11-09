import requests
import json
import time


def save_req_data(location, search_term):

    url = f'https://www.google.com/search?tbm=map&authuser=0&hl=en&gl=np&pb=!4m12!1m3!1d54390.43727584774!2d83.41443194264933!3d27.692500881120388!2m3!1f0!2f0!3f0!3m2!1i835!2i739!4f13.1!7i20!10b1!12m16!1m1!18b1!2m3!5m1!6e2!20e3!10b1!12b1!13b1!16b1!17m1!3e1!20m3!5e2!6b1!14b1!19m4!2m3!1i360!2i120!4i8!20m57!2m2!1i203!2i100!3m2!2i4!5b1!6m6!1m2!1i86!2i86!1m2!1i408!2i240!7m42!1m3!1e1!2b0!3e3!1m3!1e2!2b1!3e2!1m3!1e2!2b0!3e3!1m3!1e8!2b0!3e3!1m3!1e10!2b0!3e3!1m3!1e10!2b1!3e2!1m3!1e9!2b1!3e2!1m3!1e10!2b0!3e3!1m3!1e10!2b1!3e2!1m3!1e10!2b0!3e4!2b1!4b1!9b0!22m6!1sMjRLZfXDINGO4-EP1aW7oAE%3A2942!2s1i%3A0%2Ct%3A11886%2Cp%3AMjRLZfXDINGO4-EP1aW7oAE%3A2942!7e81!12e5!17sMjRLZfXDINGO4-EP1aW7oAE%3A3130!18e15!24m88!1m29!13m9!2b1!3b1!4b1!6i1!8b1!9b1!14b1!20b1!25b1!18m18!3b1!4b1!5b1!6b1!9b1!12b1!13b1!14b1!15b1!17b1!20b1!21b1!22b0!25b1!27m1!1b0!28b0!31b0!10m1!8e3!11m1!3e1!14m1!3b1!17b1!20m2!1e3!1e6!24b1!25b1!26b1!29b1!30m1!2b1!36b1!39m3!2m2!2i1!3i1!43b1!52b1!54m1!1b1!55b1!56m2!1b1!3b1!65m5!3m4!1m3!1m2!1i224!2i298!71b1!72m17!1m5!1b1!2b1!3b1!5b1!7b1!4b1!8m8!1m6!4m1!1e1!4m1!1e3!4m1!1e4!3sother_user_reviews!9b1!89b1!103b1!113b1!117b1!26m4!2m3!1i80!2i92!4i8!30m28!1m6!1m2!1i0!2i0!2m2!1i530!2i739!1m6!1m2!1i785!2i0!2m2!1i835!2i739!1m6!1m2!1i0!2i0!2m2!1i835!2i20!1m6!1m2!1i0!2i719!2m2!1i835!2i739!34m18!2b1!3b1!4b1!6b1!8m6!1b1!3b1!4b1!5b1!6b1!7b1!9b1!12b1!14b1!20b1!23b1!25b1!26b1!37m1!1e81!42b1!47m0!49m7!3b1!6m2!1b1!2b1!7m2!1e3!2b1!50m4!2e2!3m2!1b1!3b1!61b1!67m2!7b1!10b1!69i670&q={search_term}%20in%20{location}&oq={search_term}%20in%20{location}&gs_l=maps.3..38i72k1l5.24688.50696.25.56929.26.26.....288.4910.0j19j6.25.....0....1..maps..1.25.4990.0..38i377i430i444k1j38i377i430i429k1j38i377i430i426k1j38i426k1j38i39k1j38i39i129k1j38i377k1j38i376k1j38i429k1j38i10i377k1j38i10i376k1j38i10i377i430i444k1j38i10i377i430i426k1j38i10i426k1j38i10i377i430i427k1j38i10i377i430k1.&tch=1&ech=14&psi=MjRLZfXDINGO4-EP1aW7oAE.1699427379238.1'


    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.5',
    'Referer': 'https://www.google.com/',
    'DNT': '1',  
}
    data = requests.get(url, headers=headers)

    data = data.text
    data = data.rstrip('/*""*/')

    try:
        parsed_data = json.loads(data)
        req_data = parsed_data["d"]
        final_data = req_data.lstrip(")]}'\n")
        json_data = json.loads(final_data)
    except json.JSONDecodeError as e:
        print("Error parsing JSON:", e)
        print(data)
        return {}
    

    def create_indexed_dict(data):
        if isinstance(data, list):
            indexed_dict = {}
            for index, item in enumerate(data):
                indexed_dict[index] = create_indexed_dict(item)
            return indexed_dict
        elif isinstance(data, dict):
            indexed_dict = {}
            for key, value in data.items():
                indexed_dict[key] = create_indexed_dict(value)
            return indexed_dict
        else:
            return data

    indexed_data = create_indexed_dict(json_data)
    items = indexed_data[0][1]

    required_data = []
    for item in items.values():
        name = item.get(14,{}).get(11,None)
        latitude = item.get(14, {}).get(9, {}).get(2, None)
        longitude = item.get(14, {}).get(9, {}).get(3, None)

        if name:
            required_data.append({'name': name, 'latitude': latitude, 'longitude': longitude})


   
    time.sleep(5)

    return required_data

if __name__ == '__main__':
    

    test_data = ['Kathmandu']
    search_term = 'Resturants'

    total_data = {}
    
    for place in test_data:
        data = save_req_data(place, search_term)
        total_data[place] = data
    
    with open('total_data.json', 'w') as file:
        json.dump(total_data, file, indent=4)






    





