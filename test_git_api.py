import unittest
import requests
import auxiliary


class TestGitApi(unittest.TestCase):

    token = '1234567890123456789012345678901234567890'
    headers = {"Authorization": "token %s" % token}
    basic_url = 'https://api.github.com'

    def testCreateRepo(self):
        self.createRepo("BestQA", "This is repository for MyOwnPortfolio")

        url = '%s/user/repos' % self.basic_url
        auxiliary.Checking(url, 'name', 'BestQA', 60, self.headers).presence()

    def testRenameRepo(self):
        self.createRepo("BestQa", "This is repository for MyOwnPortfolio")

        url = '%s/repos/MyOwnPortfolio/BestQA' % self.basic_url
        data = {"name": "BestOfTheBestQA"}
        requests.patch(url, headers=self.headers, json=data)

        check_url = '%s/user/repos' % self.basic_url
        auxiliary.Checking(check_url, 'name', 'BestOfTheBestQA', 60, self.headers).presence()

    def testChangeDescriptionOfRepo(self):
        self.createRepo("BestOfTheBestQA", "This is repository for MyOwnPortfolio")

        url = '%s/repos/MyOwnPortfolio/BestOfTheBestQA' % self.basic_url
        data = {"name": "BestOfTheBestQA", "description": "This is BestOfTheBestQA repository for MyOwnPortfolio"}
        requests.patch(url, headers=self.headers, json=data)

        check_url = '%s/user/repos' % self.basic_url
        auxiliary.Checking(check_url, 'description',
                           'This is BestOfTheBestQA repository for MyOwnPortfolio',
                           60, self.headers).presence()

    def testAddFileToRepo(self):
        self.createRepo("BestOfTheBestQA", "This is repository for MyOwnPortfolio")

        url = '%s/repos/MyOwnPortfolio/BestOfTheBestQA/contents/file.txt' % self.basic_url
        data = {"path": "file.txt", "message": "initial commit", "content": "dGhpcyBpcyBzb21lIHRleHQ="}
        requests.put(url, headers=self.headers, json=data)

        check_url = '%s/repos/MyOwnPortfolio/BestOfTheBestQA/contents/' % self.basic_url
        auxiliary.Checking(check_url, 'name', 'file.txt', 60, self.headers).presence()

    def testDeleteRepo(self):
        self.createRepo("BestOfTheBestQA", "This is repository for MyOwnPortfolio")

        url = '%s/repos/MyOwnPortfolio/BestOfTheBestQA' % self.basic_url
        requests.delete(url, headers=self.headers)

        check_url = '%s/user/repos' % self.basic_url
        auxiliary.Checking(check_url, 'name', 'BestOfTheBestQA', 60, self.headers).absence()

    def tearDown(self):
        url = '%s/user/repos' % self.basic_url
        r = requests.get(url, headers=self.headers)
        j = r.json()

        for item in j:
            if item['full_name'] in ('MyOwnPortfolio/BestQA', 'MyOwnPortfolio/BestOfTheBestQA'):
                url = '%s/repos/%s' % (self.basic_url, item['full_name'])
                requests.delete(url, headers=self.headers)

    def createRepo(self, name, description):
        self.name = name
        self.description = description
        url = '%s/user/repos' % self.basic_url
        data = {"name": name, "description": description}
        requests.post(url, headers=self.headers, json=data)

if __name__ == '__main__':
    unittest.main()
