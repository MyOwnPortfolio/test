import time
import requests


class Checking:
    def __init__(self, url, key, value, wait, headers):
        self.url = url
        self.key = key
        self.value = value
        self.wait = wait
        self.headers = headers

    def presence(self):
        self.checking(True)

    def absence(self):
        self.checking(False)

    def checking(self, clause):
        # if clause = True it means that we check whether there is the value in list
        # the same as if we wrote:     availability = self.value in self.names_list()
        # if clause = False it means that we check whether there isn't the value in list
        # the same as if we wrote:     availability = self.value not in self.names_list()
        availability = (self.value in self.names_list()) == clause
        wait = 0

        while availability is not True:
            time.sleep(1)
            wait += 1
            availability = (self.value in self.names_list()) == clause

            if wait > self.wait:
                print('{0} seconds and information still unavailable'.format(self.wait))
                assert False

    def names_list(self):
        json_resp = requests.get(self.url, headers=self.headers).json()
        return [item[self.key] for item in json_resp]
