import requests
import sys


def get_count_word(u, w):
    r = requests.get(u)
    if r.status_code == 200:
        return len(r.text.split('{0}'.format(w))) - 1
    else:
        return 'ERROR:{0}'.format(r.status_code)


u = sys.argv[1]
w = sys.argv[2]
l = get_count_word(u, w)
print('{0}'.format(l))
