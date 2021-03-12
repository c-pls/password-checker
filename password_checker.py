import requests
import hashlib
import sys

def request_api(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Errors {res.status_code}, something happend')

    return res


def get_pass_leak_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())

    flag = False
    for key, counter in hashes:
        if key == hash_to_check:
            print(f'This has been hacked {counter} times ')
            flag = True
    if not flag:
                print('Fine. You can carry on')


# This API return the tail of the password
def get_full_data(response):
    print(response.text)

# Check the password


def pass_check(password):
    m = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = m[:5], m[5:]

    response = request_api(first5_char)
    get_pass_leak_count(response, tail)


def main():
    password_list = sys.argv[1:]


    for password in password_list:
        pass_check(password)

#def main():
  # read from the file
      # with open('password.txt', 'r') as p_file:
          # password_file = p_file.read()
          # print(password_file)
          #     pass_check('123455')
if __name__ == '__main__':
    main()

