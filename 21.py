def username_generator(first_name, last_name):
    if len(first_name) < 3:
        username_first_part = first_name
    else:
        username_first_part = first_name[:3]
    if len(last_name) < 4:
        username_second_part = last_name
    else:
        username_second_part = last_name[: 4]
    username = username_first_part + username_second_part
    return username
def password_generator(username):
    password = ""
    if username:
        password = username[-1] + username[: -1]
    return password
first_name = "Abe"
last_name = "Simpson"
username = username_generator(first_name, last_name)
print(f"Сгенерированное имя пользователя: {username}")
password = password_generator(username)
print(f"Сгенерированный временный пароль: {password}")