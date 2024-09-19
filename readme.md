# API Usage Instructions

## Retrieving Data from the Innoforest API and saving as JSON
To retrieve data from the Innoforest API, use the following curl command. Repeat this call for each page of results.

```shell
curl --request GET \
  --url 'https://liveapi.innoforest.co.kr/seed/corp/v1/findseedcorpsummary?page=1&limit=20&bizArray=11,7,15,5,16,2,21,10,17,22,12,4,13,19,1,3,20,9,18,8,14,6,23,24&invstCdArray=30,20,32,34,36,38,40,42,50,55,70,99&userCd=S&empFrom=30&empTo=10000&provinceArray=11&keyword=&orderByField=&tagArray=&tagText=&invstCdFrom=&invstCdTo=&invstWholeValFrom=&invstWholeValTo=&invstFrom=&invstTo=&salesFrom=&salesTo=&isHiring=&isRecommendHiring=' \
  --header 'accept: application/json' \
  --header 'dnt: 1' \
  --header 'origin: https://www.innoforest.co.kr' \
  --header 'priority: u=1, i' \
  --header 'referer: https://www.innoforest.co.kr/' \
  --header 'sec-ch-ua: "Not;A=Brand";v="24", "Chromium";v="128"' \
  --header 'sec-ch-ua-mobile: ?1' \
  --header 'sec-ch-ua-platform: "Android"' \
  --header 'sec-fetch-dest: empty' \
  --header 'sec-fetch-mode: cors' \
  --header 'sec-fetch-site: same-site' \
  --header 'user-agent: Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Mobile Safari/537.36' \
  --header 'withcredentials: true'
```

### 수집기준
- 카테고리: 전체
- 투자단게: Series A 이상
- 고용인원: 30인 ~ 10,000인
- 지역: 서울


## Converting JSON to TSV

```shell
python json_to_tsv.py
```

