import requests
import json
import time


def save_req_data(place):

    url = f'https://www.google.com/search?tbm=map&authuser=0&hl=en&gl=np&pb=!4m12!1m3!1d54482.371265892485!2d83.4425462!3d27.507410150000005!2m3!1f0!2f0!3f0!3m2!1i711!2i739!4f13.1!7i20!10b1!12m16!1m1!18b1!2m3!5m1!6e2!20e3!10b1!12b1!13b1!16b1!17m1!3e1!20m3!5e2!6b1!14b1!19m4!2m3!1i360!2i120!4i8!20m57!2m2!1i203!2i100!3m2!2i4!5b1!6m6!1m2!1i86!2i86!1m2!1i408!2i240!7m42!1m3!1e1!2b0!3e3!1m3!1e2!2b1!3e2!1m3!1e2!2b0!3e3!1m3!1e8!2b0!3e3!1m3!1e10!2b0!3e3!1m3!1e10!2b1!3e2!1m3!1e9!2b1!3e2!1m3!1e10!2b0!3e3!1m3!1e10!2b1!3e2!1m3!1e10!2b0!3e4!2b1!4b1!9b0!22m6!1sMjRLZfXDINGO4-EP1aW7oAE%3A1221!2s1i%3A0%2Ct%3A11886%2Cp%3AMjRLZfXDINGO4-EP1aW7oAE%3A1221!7e81!12e5!17sMjRLZfXDINGO4-EP1aW7oAE%3A2306!18e15!24m88!1m29!13m9!2b1!3b1!4b1!6i1!8b1!9b1!14b1!20b1!25b1!18m18!3b1!4b1!5b1!6b1!9b1!12b1!13b1!14b1!15b1!17b1!20b1!21b1!22b0!25b1!27m1!1b0!28b0!31b0!10m1!8e3!11m1!3e1!14m1!3b1!17b1!20m2!1e3!1e6!24b1!25b1!26b1!29b1!30m1!2b1!36b1!39m3!2m2!2i1!3i1!43b1!52b1!54m1!1b1!55b1!56m2!1b1!3b1!65m5!3m4!1m3!1m2!1i224!2i298!71b1!72m17!1m5!1b1!2b1!3b1!5b1!7b1!4b1!8m8!1m6!4m1!1e1!4m1!1e3!4m1!1e4!3sother_user_reviews!9b1!89b1!103b1!113b1!117b1!26m4!2m3!1i80!2i92!4i8!30m0!34m18!2b1!3b1!4b1!6b1!8m6!1b1!3b1!4b1!5b1!6b1!7b1!9b1!12b1!14b1!20b1!23b1!25b1!26b1!37m1!1e81!42b1!47m0!49m7!3b1!6m2!1b1!2b1!7m2!1e3!2b1!50m4!2e2!3m2!1b1!3b1!61b1!67m2!7b1!10b1!69i670&q={place}&oq={place}&gs_l=maps.3..38i39i111i444k1j38i426k1l2j38i578i444k1j38i426k1.1255895.1257390.18.1264639.8.8.....174.1168.0j7.7.....0....1..maps..1.7.1194.0..38i444k1j38i39i111i426k1j38i376k1j38i377k1j38.&tch=1&ech=7&psi=MjRLZfXDINGO4-EP1aW7oAE.1699427379238.1'


    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.5',
    'Referer': 'https://www.google.com/',
    'DNT': '1',  
}
    data = requests.get(url, headers=headers)

    data = data.text
    data = data.rstrip("/*""*/")

    try:
        parsed_data = json.loads(data)
        data = parsed_data["d"]
        data = data.lstrip(")]}'")
    except json.JSONDecodeError as e:
        print("Error parsing JSON:", e)
    

    def create_indexed_dict(data, prefix=''):
        if isinstance(data, list):
            indexed_dict = {}
            for index, item in enumerate(data):
                key = f"{prefix}_{index}"
                indexed_dict[key] = create_indexed_dict(item, prefix=key)
            return indexed_dict
        else:
            return data

    indexed_data = create_indexed_dict(parsed_data)

    
    latitude = indexed_data['_6']['_6_9']['_6_9_2']
    longitude = indexed_data['_6']['_6_9']['_6_9_3']
    name = indexed_data['_6']['_6_11']

    data = {}
    data['name'] = name
    data['latitude'] = latitude
    data['longitude'] = longitude

    time.sleep(2)

    return data

if __name__ == '__main__':
    places = ['Surkhet', 'Tansen Durbar', 'Gosaikunda Lake', 'Bhaktapur Durbar Square', 'Besisahar', 'Simara', 'Janakpur', 'Biratnagar', 'Mein Khola', 'Jhapa', 'Gaur', 'Gorkha', 'Dhankuta', 'Jiri', 'Kathmandu', 'Dhampus', 'Madhyapur Thimi', 'Rara Lake', 'Dhunche', 'Kopan Monastery', 'Kamalamai', 'Makalu Base Camp', 'Lamjung', 'Bardia National Park', 'Phoksundo Lake', 'Barpak', 'Birendranagar', 'Rupa Lake', 'Siddharthanagar', 'Nuwakot', 'Baglung', 'Mahendranagar', 'Nepalgunj', 'Hetauda', 'Langtang National Park', 'Tikapur', 'Poon Hill', 'Chandragiri Hills', 'Rajbiraj', 'Bhadrapur', 'Birgunj', 'Gulariya', 'Suklaphanta Wildlife Reserve', 'Khanikhola', 'Sagarmatha National Park', 'Solukhumbu', 'Kalinchowk', 'Durbar Marg', 'Ilam', 'Dolpo', 'Khandbari', 'Ramechhap', 'Bandipur', 'Hattisar', 'Rara National Park', 'Charikot', 'Basantapur Durbar Square', 'Dhorpatan Hunting Reserve', 'Doti', 'Manaslu Conservation Area', 'Tumlingtar', 'Tal Barahi', 'Sauraha', 'Birtamode', 'Renjo La Pass', 'Lahan', 'Koshi Tappu Wildlife Reserve', 'Nagarkot', 'Damauli', 'Langtang Valley', 'Dhulikhel', 'Beni', 'Marpha', 'Achham', 'Kalapathar', 'Devghat', 'Sainbu', 'Boudhanath Stupa', 'Jaleshwor', 'Ghorepani', 'Thamel', 'Kanchenjunga Conservation Area', 'Butwal', 'Bhimsen', 'Ghandruk', 'Patan Durbar Square', 'Bardiya National Park', 'Lumbini', 'Karnali', 'Gosainkunda', 'Ghorahi', 'Lukla', 'Sukla Phanta Wildlife Reserve', 'Lumbini Sacred Garden', 'Bhaktapur', 'Munglin', 'Tatopani', 'Lalitpur', 'Rupa Tal', 'Tilaurakot', 'Gaighat', 'Phakding', 'Helambu', 'Gosainkunda Lake', 'Annapurna Conservation Area', 'Phidim', 'Kagbeni', 'Swayambhunath Stupa', 'Mustang', 'Rukumkot', 'Tulsipur', 'Kirtipur', 'Gosaikunda', 'Kalaiya', 'Waling', 'Hile', 'Rasuwa', 'Biratchowk', 'Terhathum', 'Thyangboche', 'Siddharthanagar (Bhairahawa)', 'Pashupatinath Temple', 'Lakeside Pokhara', 'Muktinath Temple', 'Khaptad National Park', 'Kusma', 'Rolpa', 'Fewa Lake', 'Begnas Lake', 'Panchthar', 'Chitwan National Park', 'Namche Bazaar', 'Dhangadhi', 'Dharan', 'Chainpur', 'Palpa', 'Bharatpur', 'Thame', 'Gokyo Lake', 'Taudaha Lake', 'Shey Phoksundo National Park', 'Jumla', 'Damak', 'Ghale Gaun', 'Sandakpur', 'Dharapani', 'Dhading Besi', 'Halesi', 'Phewa Lake', 'Jomsom', 'Syangja', 'Tansen', 'Panaoti', 'Maratika Cave', 'Pokhara', 'Makalu Barun National Park', 'Kathmandu Valley', 'Kakani', 'Annapurna Base Camp', 'Simikot', 'Patan', 'Kawasoti', 'Itahari']

    test_data = ['Surkhet', 'Tansen Durbar', 'Gosaikunda Lake', 'Bhaktapur Durbar Square']

    total_data = {}
    for place in test_data:
        data = save_req_data(place)
        total_data[place] = data
    
    with open('total_data.json', 'w') as file:
        json.dump(total_data, file, indent=4)






    





