# http://127.0.0.1:8000/
# http://127.0.0.1:8000/polls
# http://127.0.0.1:8000/admin/ Username: admin Password: 123456
# flake8 path_to_dir/Django
# (C:\Users\zubko\PycharmProjects\Django)


import django


def main():
    print(django.get_version())
    pass


if __name__ == '__main__':
    main()
