import requests

class HttpHandler():
    def __init__(self, base_url):
        self.base_url = "http" + base_url + "/api/"
        self.session = requests.Session()

    def log_event(self, e):
        json = { 'event': e }
        r = self.session.post(self.base_url + "log_event", json=json)
        if r.status_code == 200:
            return True
        else:
            return False
