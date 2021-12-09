"""
Request용 공통 데이터셋

2021, David Jung(https://github.com/hyu-text-mining-7/crawler)
License: GPL-3.0
"""
class restaurantInquiryData:
    """
    가맹점 목록 취득을 위한 데이터셋 모음
    """
    def getHostUrl():
        """
        Request를 던질 URL 취득
        Returns:
            대상 URL (str)
        """
        return 'https://www.yogiyo.co.kr/api/v1/restaurants-geo/?'

    def getDefaultHeader():
        """
        헤더셋. 별도 변경 없이 그대로 쓰면 됨.
        Returns:
            해더셋 (dict)
        """
        return {
                'Accept':'application/json',
                'Accept-Encoding':'gzip, deflate, br',
                'Accept-Language':'ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3',
                'Connection':'keep-alive',
                'Content-Type':'application/x-www-form-urlencoded',
                'Cookie':'sessionid=eb9f3b2c1ed214f5f08295c71594278d; RestaurantListCookieTrigger=true; RestaurantMenuCookieTrigger=true',
                'Host':'www.yogiyo.co.kr',
                'Referer':'https://www.yogiyo.co.kr/mobile/',
                'Sec-Fetch-Dest':'empty',
                'Sec-Fetch-Mode':'cors',
                'Sec-Fetch-Site':'same-origin',
                'TE':'trailers',
                'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0',
                'X-ApiKey':'iphoneap',
                'X-ApiSecret':'fe5183cc3dea12bd0ce299cf110a75a2'
                }

    def getDefaultCookies():
        """
        쿠키셋. 별도 변경 없이 그대로 쓰면 됨.
        Returns:
            쿠키셋 (dict)
        """
        return {'RestaurantListCookieTrigger':'true', 'RestaurantMenuCookieTrigger':'true', 'sessionid':'eb9f3b2c1ed214f5f08295c71594278d'}
    
    def getDefaultParams(page, item='60', lat='37.53196623412091', lng='126.91413324032165'):
        """
        파라메터 기본 값 취득
        
        Args:
            page : 조회할 페이지 인덱스
            item : 한번에 불러 올 아이템 갯수. 시스템 기본 값은 60이며 가능하면 변경하지 말 것.
            lat : 조회 할 위도 값. 기본 값은 국회의사당 기준.
            lng : 조회 할 경도 값. 기본 값은 국회의사당 기준.
        Returns:
            파라메터셋
        """
        # 나머지 파라메터는 시스템 기본 값 준수. 좌표 값은 국회의사당이 회사 근처라서 그냥 써 봄
        return {'page':str(page), 'items':str(item), 'lat':str(lat), 'lng':str(lng), 'order':'rank', 'search':''}


class reviewInquiryData:
    host_url = 'https://www.yogiyo.co.kr/api/v1/reviews/'
    restaurant_id = ''
    """
    리뷰 취득을 위한 데이터셋 모음
    """
    def __init__(self, restaurant_id):
        """
        가맹점ID 반드시 있어야 함
        """
        self.restaurant_id = str(restaurant_id)

    def getHostUrl(self):
        """
        Request를 던질 URL 취득
        Returns:
            대상 URL (str)
        """
        return (self.host_url + self.restaurant_id +'/?')

    def getDefaultHeader(self):
        """
        헤더셋. 별도 변경 없이 그대로 쓰면 됨.
        Returns:
            해더셋 (dict)
        """
        return {
                'Accept':'application/json',
                'Accept-Encoding':'gzip, deflate, br',
                'Accept-Language':'ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3',
                'Connection':'keep-alive',
                'Content-Type':'application/x-www-form-urlencoded',
                'Cookie':'sessionid=eb9f3b2c1ed214f5f08295c71594278d; RestaurantListCookieTrigger=true; RestaurantMenuCookieTrigger=true',
                'Host':'www.yogiyo.co.kr',
                'Referer':'https://www.yogiyo.co.kr/mobile/',
                'Sec-Fetch-Dest':'empty',
                'Sec-Fetch-Mode':'cors',
                'Sec-Fetch-Site':'same-origin',
                'TE':'trailers',
                'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0',
                'X-ApiKey':'iphoneap',
                'X-ApiSecret':'fe5183cc3dea12bd0ce299cf110a75a2'
                }

    def getDefaultCookies(self):
        """
        쿠키셋. 별도 변경 없이 그대로 쓰면 됨.
        Returns:
            쿠키셋 (dict)
        """
        return {'RestaurantListCookieTrigger':'true', 'RestaurantMenuCookieTrigger':'true', 'sessionid':'eb9f3b2c1ed214f5f08295c71594278d'}
    
    def getDefaultParams(self, page, count='10'):
        """
        파라메터 기본 값 취득
        
        Args:
            page : 조회할 페이지 인덱스
            count : 한번에 불러 올 리뷰 갯수. 시스템 기본 값은 10이며 가능하면 변경하지 말 것.
            lat : 조회 할 위도 값. 기본 값은 국회의사당 기준.
            lng : 조회 할 경도 값. 기본 값은 국회의사당 기준.
        Returns:
            파라메터셋
        """
        return {page:str(page), 'count':str(count), 'only_photo_review':'false', 'sort':'time'}