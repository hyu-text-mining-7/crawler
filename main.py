import requests
import json
import pprint
import common

restaurant_list = []

# 국회의사당 내 가게 10페이지
for page in range(1, 2): # page는 1부터 10까지 순서대로 바뀜. 페이징 때문에 씀.
    # 요청 생성
    host_url = common.restaurantInquiryData.getHostUrl()
    default_header = common.restaurantInquiryData.getDefaultHeader()
    default_cookies = common.restaurantInquiryData.getDefaultCookies()
    req = requests.get(
        url = host_url,
        headers = default_header,
        params = common.restaurantInquiryData.getDefaultParams(page),
        cookies = default_cookies) 
    # 가맹점 목록에 추가
    for element_dict in json.loads(req.content.decode())['restaurants']:
        restaurant_list.append({'id':element_dict['id'], 'name':element_dict['name']})

print("취득한 가맹점 개수 : ", len(restaurant_list))

comments = []
for restaurant in restaurant_list:
    # Request 필요 데이터 미리 로드
    rid = restaurant['id']
    inq_data_obj = common.reviewInquiryData(rid)
    host_url = inq_data_obj.getHostUrl()
    default_header = inq_data_obj.getDefaultHeader()
    default_cookies = inq_data_obj.getDefaultCookies()
    for page in range(1, 2):
        req = requests.get(
            url = host_url,
            headers = default_header,
            params = inq_data_obj.getDefaultParams(page),
            cookies = default_cookies)
        for comment_dict in json.loads(req.content.decode()):
            comments.append({'id':str(rid), # 가맹점ID
                'rating_total':str(comment_dict['rating']), # 총점
                'rating_quantity':str(comment_dict['rating_quantity']), # 분량(양) 점수
                'rating_taste':str(comment_dict['rating_taste']), # 맛 점수
                'rating_delivery':str(comment_dict['rating_delivery']), # 배달 점수
                'comment':comment_dict['comment']
            })

print("추출된 댓글 양: ", len(comments))

print("데이터를 파일로 출력합니다.")
f = open("RAWDATA.txt", "w", encoding="utf8")
f.write("id\ttotal\tquantity\ttaste\tdelivery\tdocument\n")
for e in comments:
    f.write("%s\t%s\t%s\t%s\t%s\t%s\n" %
        (e['id'], e['rating_total'], e['rating_quantity'], e['rating_taste'], e['rating_delivery'], e['comment'].replace("\r\n", "").replace("\n", "").replace("\t", ""))
    )
f.close()
print("파일출력이 완료되었습니다.")