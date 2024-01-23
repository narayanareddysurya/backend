def deco(func):
    def inner(name):
        if name == "modi":
            print("modi is prime minister")
        else:
            func(name)
    return inner
@deco  
def security(name):
    print("welcome","sai venkat")
def security(name):
    print("Welcome",name)
security(input())