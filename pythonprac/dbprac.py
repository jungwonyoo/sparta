from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta  # 'dbsparta'라는 이름의 db를 만듭니다.

# insert / find / update / delete

# MongoDB에 insert 하기

# doc = {'name':'mark','age':25}
# db.users.insert_one(doc)

# find 하기

print("------------")
# 같은 나이에 있는 user 가져오기
same_ages = list(db.users.find({'age': 20}))
print(same_ages)

print("------------")
# 전체 user 가져오기
all_person = list(db.users.find({}, {'_id': False}))  # False 쓰면 값 안 가져온다는 뜻

for person in same_ages:
    print(all_person)

print("------------")
# 값 하나만 가져오기 find_one 사용
user = db.users.find_one({'name': 'bobby'})
print(user)

# update 하기 (update_one, update_many)

# 생김새
# db.people.update_many(찾을조건,{ '$set': 어떻게바꿀지 })

print("------------update")
db.users.update_one({'name': 'bobby'}, {'$set': {'age': 19}})
print(user)

# delete 하기 (delete_one, delete_many)

print("------------delete")
db.users.delete_one({'name': 'bobby'})
print(user)


# 저장 - 예시
doc = {'name':'bobby','age':21}
db.users.insert_one(doc)

# 한 개 찾기 - 예시
user = db.users.find_one({'name':'bobby'})

# 여러개 찾기 - 예시 ( _id 값은 제외하고 출력)
same_ages = list(db.users.find({'age':21},{'_id':False}))

# 바꾸기 - 예시
db.users.update_one({'name':'bobby'},{'$set':{'age':19}})

# 지우기 - 예시
db.users.delete_one({'name':'bobby'})