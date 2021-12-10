# Cralwer
yogiyo.co.kr 데이터 크롤러 입니다.

# Dependencies
* [requests](https://pypi.org/project/requests)
## Install
아래의 명령어를 입력하여 스크립트 실행에 필요한 라이브러리를 설치해주십시오.
```
pip3 install requests
```

# File format
파일은 `RAWDATA.txt`라는 이름으로 출력되며 각 컬럼은 아래의 순서로 이루어져 있습니다.
1. id → 가맹점ID
2. total → 총점
3. quantity → 양
4. taste → 맛
5. delivery → 배달
6. document → 리뷰 내용

## Example
```
id	total	quantity	taste	delivery	document
9990001	5	5	5	5	좋은 가게에요!!
9990001	5	5	5	5	맛있게 잘먹었어요.
9990001	5	5	5	5	👍
```
