import time
import json
from jsonpath import jsonpath
import numpy as np
import pandas as pd
import requests
import os
import time
import random
from tqdm import tqdm
#==============================================#
# some key params in request, We abide by */robots.txt, config.py will not be published
#==============================================#
from config import headersURL, hotel_info_URL, post_data, page_detail_URL, page_detail_post_data, hotel_details_headers

hotel_info_URL = hotel_info_URL
headersURL = headersURL

def hotelURL(num):
    """get hotel page info details, including the hotel item urls

    Args:
        num (int): page number on TripAdvisor.com

    Returns:
        dataframes: hotelurl, locationid
    """
    name=np.array([])
    hotelurl = np.array([])
    locationid=np.array([])
    lat=np.array([])
    lng=np.array([])
    url = hotel_info_URL
    headers = headersURL
    for j in tqdm(range(num)):
        post_data.setdefault("pageIndex", j)
        data = post_data
        time.sleep(np.random.randint(3,6))
        res = requests.post(url=url, json=data, headers=headers)
        jtext = json.loads(res.text)
        name = np.append(name,np.array(jsonpath(jtext,'$..hotels[0:].name')))
        hotelurl = np.append(hotelurl,np.array(jsonpath(jtext,'$..hotels[0:].url' )))
        locationid = np.append(locationid,np.array(jsonpath(jtext,'$..hotels[0:].taLocationId')))
        lat = np.append(lat, np.array(jsonpath(jtext,'$..hotels[0:].latitude')))
        lng = np.append(lng , np.array(jsonpath(jtext,'$..hotels[0:].longitude')))
    pd.DataFrame({'name':name,'latitude':lat,'longtitude':lng,'locationid':locationid,'hotelurl':hotelurl}).to_csv('hotels_info.csv')
    return hotelurl,locationid

def getjsonrev(url_hotel,locationid):
    """get json format reviews details

    Args:
        url_hotel (str): url of hotel items
        locationid (int): an key param in web request
    """
    for j in tqdm(range(0,len(url_hotel))):
        details = []
        hotel_details_headers.update({"referer": f'{url_hotel[j]}'})
        headers = hotel_details_headers

        purl = page_detail_URL
        i = 1
        while True:
            page_detail_post_data.update({"locationId": locationid[j], "pageInfo": {"num": i, "size": 50}})
            data = page_detail_post_data
            time.sleep(random.randint(2,5))
            # time.sleep(np.random.randint(3,6))
            res = requests.post(url=purl, json=data, headers=headers)
            jtext = json.loads(res.text)
            detail = jsonpath(jtext, '$.details')[0]
            details.extend(detail)

            if not jsonpath(jtext, '$.pageInfo.hasNext')[0]:
                break
            i += 1
        try:
            hotel_name = details[0]['locationInfo']['name']
            jfile = json.dumps(details, ensure_ascii=False)
            with open(f'{hotel_name}.json', 'w', encoding='utf-8') as f:
                f.write(jfile)
        except:
            time.sleep(60)
            continue

if __name__=='__main__':
    page_num = int(input('Please input the page number:'))
    # Setting the file path
    if not os.path.exists('../data'):
        os.mkdir('../data')
    os.chdir("../data")
    # Get hotel URL and locid for crawling internal information
    url_hotel, locationid = hotelURL(page_num)
    # Get reviews' detail
    getjsonrev(url_hotel, locationid)