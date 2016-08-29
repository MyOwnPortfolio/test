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
        # check wherther or not smth is available. In case, when we have created or changed smth and want to check it out
        r = requests.get(self.url, headers=self.headers)
        j = r.json()

        list_of_smth = [item[self.key] for item in j]
        availability = self.value in list_of_smth

        wait = 0
        while availability is not True:
            time.sleep(1)
            wait += 1

            r = requests.get(self.url, headers=self.headers)
            j = r.json()

            list_of_smth = [item[self.key] for item in j]
            availability = self.value in list_of_smth
            if wait > self.wait:
                print('{0} seconds and information still unavailable'.format(self.wait))
                assert False

    def absence(self):
        # check wherther or not smth is unavailable. In case, when we have deleted smth and want to check it out
        r = requests.get(self.url, headers=self.headers)
        j = r.json()

        list_of_smth = [item[self.key] for item in j]
        availability = self.value not in list_of_smth

        wait = 0
        while availability is not True:
            time.sleep(1)
            wait += 1

            r = requests.get(self.url, headers=self.headers)
            j = r.json()

            list_of_smth = [item[self.key] for item in j]
            availability = self.value not in list_of_smth
            if wait > self.wait:
                print('{0} seconds and information still unavailable'.format(self.wait))
                assert False
