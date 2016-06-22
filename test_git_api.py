import requests


class TestGitApi:

    token = 'my_token'  # this is token for authorization on github
    headers = {"Authorization": "token %s" % token}

    def test_set_up(self):
        # this is the url and data for creating "BestQA" repository
        url = 'https://api.github.com/user/repos'
        r = requests.get(url, headers=self.headers)
        j = r.json()

        for item in j:
            if item['full_name'] in ('MyOwnPortfolio/BestQA', 'MyOwnPortfolio/BestOfTheBestQA'):
                url = 'https://api.github.com/repos/%s' % item['full_name']
                rm = requests.delete(url, headers=self.headers)
                assert rm.status_code == 204

    def test_create_repo(self):
        # this is the url and data for creating "BestQA" repository
        url = 'https://api.github.com/user/repos'
        data = {"name": "BestQA", "description": "This is repository for MyOwnPortfolio"}
        r = requests.post(url, headers=self.headers, json=data)
        assert r.status_code == 201

    def test_rename_repo(self):
        url = 'https://api.github.com/repos/MyOwnPortfolio/BestQA'
        data = {"name": "BestOfTheBestQA"}
        r = requests.patch(url, headers=self.headers, json=data)
        assert r.status_code == 200

    def test_change_description_of_repo(self):
        url = 'https://api.github.com/repos/MyOwnPortfolio/BestOfTheBestQA'
        data = {"name": "BestOfTheBestQA", "description": "This is BestOfTheBestQA repository for MyOwnPortfolio"}
        r = requests.patch(url, headers=self.headers, json=data)
        assert r.status_code == 200

    def test_add_file_to_repo(self):
        url = 'https://api.github.com/repos/MyOwnPortfolio/BestOfTheBestQA/contents/file.txt'
        data = {"path": "file.txt", "message": "initial commit", "content": "dGhpcyBpcyBzb21lIHRleHQ="}
        r = requests.put(url, headers=self.headers, json=data)
        assert r.status_code == 201

    def test_get_all_branches(self):
        url = 'https://api.github.com/repos/MyOwnPortfolio/BestOfTheBestQA/branches'
        r = requests.get(url, headers=self.headers)
        assert r.status_code == 200

    def test_get_master_branch(self):
        url = 'https://api.github.com/repos/MyOwnPortfolio/BestOfTheBestQA/branches/master'
        r = requests.get(url, headers=self.headers)
        assert r.status_code == 200
