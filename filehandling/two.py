import json
emp_dict ={
    'eid':'Rahul',
     'ename': 4500.00,
     'esal': True,
     'discount':None
}
print(emp_dict)
# convert python dict to json

emp_str = json.dumps(emp_dict)
print(emp_str)