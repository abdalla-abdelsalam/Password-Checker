import hashlib
import requests


def request_api_data(prefix):
    res = requests.get("https://api.pwnedpasswords.com/range/"+prefix)
    if(res.status_code != 200):
        raise RuntimeError(
            f"Error fetching: {res.status_code} check the api and try again")
    return res.text

# getting the sha1 hashed password


def get_hashed_password(password):
    hash_object = hashlib.sha1(password.encode('utf-8'))
    hased_password = hash_object.hexdigest()
    return hased_password.upper()


def check_password(data, tail):
    for line in data.splitlines():
        if line[:35] == tail:
            return line[36:]
    return 0

# start from here


def main():
    password = input('Please enter your password: ')
    hased_password = get_hashed_password(password)
    # sending the first 5 characters of a SHA-1 password hash to the pwnedpasswords api
    data = request_api_data(hased_password[:5])
    leaked_times = check_password(data, hased_password[5:])
    if int(leaked_times) == 0:
        print("Great! your password has been never ever leaked before!!")
    else:
        print(
            f"Oh nooooo! your password has been leaked {leaked_times} times before!!")
        print("You should probably change it")


if __name__ == "__main__":
    main()
