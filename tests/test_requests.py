import requests


# EXERCISE 1: API AUTOMATION
def get_api(id_user):
    api = requests.get(f"https://reqres.in/api/users/{id_user}")
    return api


def get_user_data(id_user):
    data = requests.get(f"https://reqres.in/api/users/{id_user}").json().get("data")
    return data


def test_api1():
    # Happy path
    assert get_api(1).status_code == 200


def test_api2():
    # Unhappy path
    assert get_api(0).status_code == 404


def test_api3():
    data = get_user_data(4)
    assert len(data) == 5


# EXERCISE 2: STRING MATCHING ALGORITHM
def check_parentesis(letras):
    valid_caracteres = []

    for i in letras:
        if i == "(":
            valid_caracteres.append(i)
        elif i == "[":
            valid_caracteres.append(i)
        elif i == ")":
            if valid_caracteres[-1] == "(":
                valid_caracteres.pop()
        elif i == "]":
            if valid_caracteres[-1] == "[":
                valid_caracteres.pop()

    return len(valid_caracteres) == 0


def test_string1():
    assert check_parentesis('(abc') == False


def test_string2():
    assert check_parentesis(')abc)') == False


def test_string3():
    assert check_parentesis('(a[b)c]d') == False


def test_string4():
    assert check_parentesis('(a[b]c)') == True
