import sys
import json
import time
import random
import webbrowser

try:
    from urllib.request import urlopen
except ImportError:
    from urllib import urlopen

url = 'http://www.reddit.com/r/wtf/new.json?sort=new&limit=5&show=all'

def _(*args):
    for arg in args:
        sys.stdout.write(arg)
    sys.stdout.flush()

def o_O():
    """Look shocked, c'mon!"""

    timeout = 0.5

    try:
        while True:
            _('\ro_o')
            time.sleep(timeout)
            _('\rO_o')
            time.sleep(timeout)
            _('\rO_O')
            time.sleep(timeout)
            _('\ro_O')
            time.sleep(timeout)
    except KeyboardInterrupt:
        _('\n')
        content = json.load(urlopen(url))
        post_url = random.choice(content['data']['children'])['data']['url']
        if not webbrowser.open(post_url):
            _('Open it: ', post_url, '\n')

if __name__ == '__main__':
    o_O()
