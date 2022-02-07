from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta  # 'dbsparta'라는 이름의 db를 만듭니다.


# Quiz 1. 영화제목 '매트릭스'의 평점을 가져오기

movie = db.movies.find_one({'title': '매트릭스'}) # '매트릭스' 가져오기
print(movie['point']) # 평점 가져오기


# Quiz 2. '매트릭스'의 평점과 같은 평점의 영화 제목들을 가져오기

movie = db.movies.find_one({'title': '매트릭스'}) # 매트릭스 가져오기
same_point = movie['point'] # 매트릭스 평점 가져오기

movies = list(db.movies.find({'point': same_point})) # 여러 개 찾기

for movie in movies: # 반복
    print(movie['title'])

# Quiz 3. '매트릭스'의 평점을 0으로 만들기

db.movies.update_one({'title':'매트릭스'},{'$set':{'point':'0'}})