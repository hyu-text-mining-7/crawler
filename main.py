import requests
import json
import pprint
import common

restaurant_list = []

# 국회의사당 내 가게 10페이지
for page in range(1, 2): # page는 1부터 10까지 순서대로 바뀜. 페이징 때문에 씀.
    # 요청 생성
    req = requests.get(
        url = common.restaurantInquiryData.getHostUrl(),
        headers = common.restaurantInquiryData.getDefaultHeader(),
        params = common.restaurantInquiryData.getDefaultParams(page),
        cookies = common.restaurantInquiryData.getDefaultCookies()) 
    # 가맹점 목록에 추가
    for element_dict in json.loads(req.content.decode())['restaurants']:
        restaurant_list.append({'id':element_dict['id'], 'name':element_dict['name']})

print("취득한 가맹점 개수 : ", len(restaurant_list))

comments = []
for restaurant in restaurant_list:
    rid = restaurant['id']
    for page in range(1, 2):
        inq_data_obj = common.reviewInquiryData(rid)
        req = requests.get(
            url = inq_data_obj.getHostUrl(),
            headers = inq_data_obj.getDefaultHeader(),
            params = inq_data_obj.getDefaultParams(page),
            cookies = inq_data_obj.getDefaultCookies())
        print(req.url)
        for comment_dict in json.loads(req.content.decode()):
            comments.append({'id':str(rid), # 가맹점ID
                'rating_quantity':str(comment_dict['rating_quantity']), # 분량(양) 점수
                'rating_taste':str(comment_dict['rating_taste']), # 맛 점수
                'rating_delivery':str(comment_dict['rating_delivery']), # 배달 점수
                'comment':comment_dict['comment']
            })

print("추출된 댓글 양: ", len(comments))

print("데이터를 파일로 출력합니다.")
f = open("RAWDATA.txt", "w", encoding="utf8")
for e in comments:
    f.write(("ID:"+e['id'] + "\t" +
            "QR:"+e['rating_quantity'] + "\t" +
            "TR:"+e['rating_taste'] + "\t" +
            "DR:"+e['rating_delivery'] + "\t" +
            "CMT:"+e['comment'].strip("\r\n").strip("\n").strip("\t"))+ "\n")
f.close()
print("파일출력이 완료되었습니다.")