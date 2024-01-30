# read json file, print all male users
import json
filename ='user.json'
fp = open (filename,'r')

users=json.load(fp)
print(type(users))

for user in users:
     if user['gender']=="male":
         print(user['name'], user['id'],user['gender'])
         
         
         """ for user in list(filter(lambda user: user['gender']=='male', user)):
             print(user['name'], ":", user['id'])"""