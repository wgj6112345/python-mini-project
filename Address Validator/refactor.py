def validate_email(email:str) -> bool:
    if email.find("@") != -1 and email.find(".") != -1:
        return True
    return False

while True:
    x = input("请输入你的邮箱📮: ")
    f = lambda x: print("邮箱验证通过✅") if validate_email(x) else print("该邮箱无效❌！！")
    f(x)