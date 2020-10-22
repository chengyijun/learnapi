# Create your tests here.
import hashlib


def f1(x):
    print(x)


def f2(x):
    print(x)


def test(f1, f2):
    f1('给f1传递的参数')
    f2('给f2传递的参数')


test(f1, f2)


def md5(data):
    return hashlib.md5(bytes(data, encoding='utf-8')).hexdigest()


print(md5('abel'))
print(md5('tank'))
