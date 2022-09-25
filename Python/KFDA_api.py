# 라이브러리 import
import requests
import pprint
import json

# url 입력
url = 'http://apis.data.go.kr/1471000/FoodHistInfoService1/getItemHtfsPrdlsttList1?ServiceKey=8LzgSgcr6PC9n%2Bl0Xqr%2BFX3URQ7OnDUvekNe%2FhG5YBSTnAht9iiek3z5jsHiPDWCtyATcS8vvpxMPS1ASL0Z8g%3D%3D&numOfRows=3&pageNo=1&type=json'

# url 불러오기
response = requests.get(url)

#데이터 값 출력해보기
contents = response.text

print(contents)