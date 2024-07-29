import requests

url = "http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0"
service_key = "1UPBAyWDIKQvwcQpLM0vF7PqOeQ9VgjVfjprgq3cf71RgOifhPFlyDbL6ZaC%2BHkbWK3wnXB6UDtzorewuSwHHA%3D%3D"

params = {
    'Servicekey' : service_key,
    'numOfRows' : 30,
    'pageNo' : 1,
    'dataType' : 'JSON',
    'base_date' : '20200611',
    'base_time' : '1400',
    'nx' : 18,
    'ny' : 1
}

res = requests.get(url=url, params=params)
print(res.status_code, type(res.text), res.url)
print()
print(res.text)