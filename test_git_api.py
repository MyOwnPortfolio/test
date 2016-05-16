import requests


class TestGitApi:

    def test_pre_conditions(self):
        # this is token for authorization on github
        headers = {"Authorization": "token c3b188e49a77bbfda67e68aa4624a46d2779add0"}
        # this is the url and data for creating "BestQA" repository
        url = 'https://api.github.com/user/repos'
        r = requests.get(url, headers=headers)
        j = r.json()
        for item in j:
            if item['full_name'] == 'MyOwnPortfolio/BestQA':
                url_best = 'https://api.github.com/repos/MyOwnPortfolio/BestQA'
                rm_best = requests.delete(url_best, headers=headers)
                assert rm_best.status_code == 204
                break
        for item in j:
            if item['full_name'] == 'MyOwnPortfolio/BestOfTheBestQA':
                url_best_of = 'https://api.github.com/repos/MyOwnPortfolio/BestOfTheBestQA'
                rm_best_of = requests.delete(url_best_of, headers=headers)
                assert rm_best_of.status_code == 204
                break

    def test_one(self):
        # this is token for authorization on github
        headers = {"Authorization": "token c3b188e49a77bbfda67e68aa4624a46d2779add0"}
        # this is the url and data for creating "BestQA" repository
        url = 'https://api.github.com/user/repos'
        data = {"name": "BestQA",
                "description": "This is repository for MyOwnPortfolio"}
        r = requests.post(url, headers=headers, json=data)
        assert r.status_code == 201

    def test_two(self):
        # this is token for authorization on github
        headers = {"Authorization": "token c3b188e49a77bbfda67e68aa4624a46d2779add0"}
        url = 'https://api.github.com/repos/MyOwnPortfolio/BestQA'
        data = {"name": "BestOfTheBestQA"}
        r = requests.patch(url, headers=headers, json=data)
        assert r.status_code == 200

    def test_three(self):
        # this is token for authorization on github
        headers = {"Authorization": "token c3b188e49a77bbfda67e68aa4624a46d2779add0"}
        url = 'https://api.github.com/repos/MyOwnPortfolio/BestOfTheBestQA'
        data = {"name": "BestOfTheBestQA", "description": "This is BestOfTheBestQA repository for MyOwnPortfolio"}
        r = requests.patch(url, headers=headers, json=data)
        assert r.status_code == 200

    def test_four(self):
        # this is token for authorization on github
        headers = {"Authorization": "token c3b188e49a77bbfda67e68aa4624a46d2779add0"}
        url = 'https://api.github.com/repos/MyOwnPortfolio/BestOfTheBestQA/contents/file.txt'
        data = {"path": "file.txt", "message": "initial commit", "content": "dGhpcyBpcyBzb21lIHRleHQ="}
        r = requests.put(url, headers=headers, json=data)
        assert r.status_code == 201

    def test_five(self):
        # this is token for authorization on github
        headers = {"Authorization": "token c3b188e49a77bbfda67e68aa4624a46d2779add0"}
        url = 'https://api.github.com/repos/MyOwnPortfolio/BestOfTheBestQA/branches'
        r = requests.get(url, headers=headers)
        assert r.status_code == 200

    def test_six(self):
        # this is token for authorization on github
        headers = {"Authorization": "token c3b188e49a77bbfda67e68aa4624a46d2779add0"}
        url = 'https://api.github.com/repos/MyOwnPortfolio/BestOfTheBestQA/branches/master'
        r = requests.get(url, headers=headers)
        assert r.status_code == 200
