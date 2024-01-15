headersURL = {"scheme": "https", "accept": "*/*", "accept-encoding": "gzip, deflate, br", "accept-language": "zh-CN,zh;q=0.9", "content-length": "524", "content-type": "application/json;charset:utf-8;", "origin": "https://www.tripadvisor.cn", "referer": "https://www.tripadvisor.cn/Hotels-g298557-Xi'an-Hotels.html", "sec-ch-ua": "\".Not/A)Brand\";v=\"99\", \"Google Chrome\";v=\"103\", \"Chromium\";v=\"103\"", "sec-ch-ua-mobile": "?0", "sec-ch-ua-platform": "\"Windows\"", "sec-fetch-dest": "empty", "sec-fetch-mode": "cors", "sec-fetch-site": "cross-site", "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36", "x-ta-uid": "d2795620-74ca-4070-b4d0-fc2d3c8f22e4"}

hotel_info_URL = 'https://m.ctrip.com/restapi/soa2/20874/hotelListForPc'

post_data = {"geoId": 298557, "sort": "RANK", "checkInDate": "", "checkOutDate": "", "adultNum": 1, "childNum": 0, "roomNum": 1, "needFilters": True, "pageSize": 30, "nearbyLocationId": "", "filters": [{"type": "price", "param": ""}, {"type": "facility", "param": ""}, {"type": "lv", "param": ""}, {"type": "spec", "param": ""}, {"type": "style", "param": ""}, {"type": "type", "param": ""}, {"type": "rating", "param": ""}, {"type": "brand", "param": ""}, {"type": "zone", "param": ""}, {"type": "distance", "param": ""}], "distanceSelectName": "", "childList": []}

page_detail_URL = 'https://m.ctrip.com/restapi/soa2/20997/getList'

page_detail_post_data = {"frontPage": "USER_REVIEWS", "selected": {"airlineIds": [], "airlineSeatIds": [], "langs": ["zhCN"], "ratings": [], "seasons": [], "tripTypes": [], "airlineLevel": []},}

hotel_details_headers = {"authority": "m.ctrip.com",
                "method": "POST",
                "path": "/restapi/soa2/20997/getList", "scheme": "https", "accept": "*/*", "accept-encoding": "gzip, deflate, br", "accept-language": "zh-CN,zh;q=0.9", "content-length": "206", "content-type": "application/json;charset:utf-8;", "origin": "https://www.tripadvisor.cn", "sec-ch-ua": "\".Not/A)Brand\";v=\"99\", \"Google Chrome\";v=\"103\", \"Chromium\";v=\"103\"", "sec-ch-ua-mobile": "?0", "sec-ch-ua-platform": "\"Windows\"", "sec-fetch-dest": "empty", "sec-fetch-mode": "cors", "sec-fetch-site": "cross-site", "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36", "x-ta-uid": "d2795620-74ca-4070-b4d0-fc2d3c8f22e4"}