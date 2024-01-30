# read json file, and print all user names
import json

filleenmae='user.json'
fp=open(fileename,'r')

users = json.load(fp)
print(type(users))
for user in user:
    print(user['name'])