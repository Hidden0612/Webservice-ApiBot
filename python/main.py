from getapi import GetApi

TOKEN = ""
api = GetApi(TOKEN)
register = api.register()
if register["code"] == 100: # OK
    print("Register ...")
    phone = input("Phone => ")
    hash = api.send_phone(phone)
    if hash["code"] == 100 : #OK
        code = input("Code => ") #Get Code Login
        __data = api.send_code(phone,code,hash["hash"])
        print(__data)
        if __data["code"] == 100 : #OK
            api_id = __data["api_id"]
            api_hash = __data["api_hash"]

    else:
        print(hash)
else:
    print(register)
