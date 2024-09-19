import requests
import json
import time

def crawl_innoforest_api():
    base_url = 'https://liveapi.innoforest.co.kr/seed/corp/v1/findseedcorpsummary'
    params = {
        'page': 1,
        'limit': 20,
        'bizArray': '11,7,15,5,16,2,21,10,17,22,12,4,13,19,1,3,20,9,18,8,14,6,23,24',
        'invstCdArray': '30,20,32,34,36,38,40,42,50,55,70,99',
        'userCd': 'S',
        'empFrom': 30,
        'empTo': 10000,
        'provinceArray': 11,
    }
    headers = {
        'accept': 'application/json',
        'dnt': '1',
        'origin': 'https://www.innoforest.co.kr',
        'priority': 'u=1, i',
        'referer': 'https://www.innoforest.co.kr/',
        'sec-ch-ua': '"Not;A=Brand";v="24", "Chromium";v="128"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Mobile Safari/537.36',
        'withcredentials': 'true'
    }

    all_data = []
    total_pages = None

    while True:
        response = requests.get(base_url, params=params, headers=headers)
        
        if response.status_code == 200:
            data = response.json()
            all_data.extend(data.get('data', []))
            
            if total_pages is None:
                total_pages = data.get('totalPages', 0)
                print(f"Total pages: {total_pages}")
            
            current_page = data.get('currentPages', 0)
            print(f"Page {current_page}/{total_pages} crawled successfully. Total items: {len(all_data)}")
            
            if current_page >= total_pages:
                break
            
            params['page'] = current_page + 1
        else:
            print(f"Failed to crawl page {params['page']}. Status code: {response.status_code}")
            break
        
        time.sleep(1)  # Add a delay to avoid overwhelming the server

    # Save all data to a JSON file
    with open('innoforest_data.json', 'w', encoding='utf-8') as f:
        json.dump(all_data, f, ensure_ascii=False, indent=2)

    print(f"Crawling completed. Total items: {len(all_data)}. Data saved to innoforest_data.json")

if __name__ == "__main__":
    crawl_innoforest_api()