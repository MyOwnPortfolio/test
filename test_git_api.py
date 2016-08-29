import requests
import auxiliary


class TestGitApi:

    token = '--------------------------------------'  # this is token for authorization on github
    headers = {"Authorization": "token %s" % token} # https://developer.github.com/v3/oauth/#web-application-flow
    basic_url = 'https://api.github.com'

    def test_set_up(self):    	
        url = '%s/user/repos' % self.basic_url # https://developer.github.com/v3/repos/#list-your-repositories
        r = requests.get(url, headers=self.headers)
        j = r.json()

        # if repo was created we would delete it
        for item in j:
            if item['full_name'] in ('MyOwnPortfolio/BestQA', 'MyOwnPortfolio/BestOfTheBestQA'):
                url = '%s/repos/%s' % (self.basic_url, item['full_name'])
                requests.delete(url, headers=self.headers)

    def test_create_repo(self):
        url = '%s/user/repos' % self.basic_url # https://developer.github.com/v3/repos/#create
        data = {"name": "BestQA", "description": "This is repository for MyOwnPortfolio"} # https://developer.github.com/v3/repos/#create
        requests.post(url, headers=self.headers, json=data) #creating our repo

        auxiliary.Checking(url, 'name', 'BestQA', 60, self.headers).presence() # check whether repo has been created

    def test_rename_repo(self):
        url = '%s/repos/MyOwnPortfolio/BestQA' % self.basic_url # https://developer.github.com/v3/repos/#edit
        data = {"name": "BestOfTheBestQA"} # https://developer.github.com/v3/repos/#edit
        requests.patch(url, headers=self.headers, json=data)

        check_url = '%s/user/repos' % self.basic_url # https://developer.github.com/v3/repos/#list-your-repositories
        auxiliary.Checking(check_url, 'name', 'BestOfTheBestQA', 60, self.headers).presence() # check whether repo has been renamed

    def test_change_description_of_repo(self):
        url = '%s/repos/MyOwnPortfolio/BestOfTheBestQA' % self.basic_url # https://developer.github.com/v3/repos/#edit
        data = {"name": "BestOfTheBestQA", "description": "This is BestOfTheBestQA repository for MyOwnPortfolio"} # https://developer.github.com/v3/repos/#edit
        requests.patch(url, headers=self.headers, json=data)

        check_url = '%s/user/repos' % self.basic_url # https://developer.github.com/v3/repos/#list-your-repositories
        auxiliary.Checking(check_url, 'description',
                           'This is BestOfTheBestQA repository for MyOwnPortfolio',
                           60, self.headers).presence() # check whether repo description has been changed

    def test_add_file_to_repo(self):
        url = '%s/repos/MyOwnPortfolio/BestOfTheBestQA/contents/file.txt' % self.basic_url # https://developer.github.com/v3/repos/contents/#create-a-file
        data = {"path": "file.txt", "message": "initial commit", "content": "dGhpcyBpcyBzb21lIHRleHQ="} # https://developer.github.com/v3/repos/contents/#create-a-file
        requests.put(url, headers=self.headers, json=data)

        check_url = '%s/repos/MyOwnPortfolio/BestQA/contents/' % self.basic_url # https://developer.github.com/v3/repos/contents/#get-contents
        auxiliary.Checking(check_url, 'name', 'file.txt', 60, self.headers).presence() # check whether file has been created

    def test_delete_repo(self):
        url = '%s/repos/MyOwnPortfolio/BestOfTheBestQA' % self.basic_url # https://developer.github.com/v3/repos/#delete-a-repository
        requests.delete(url, headers=self.headers)

        check_url = '%s/user/repos' % self.basic_url # https://developer.github.com/v3/repos/#list-your-repositories
        auxiliary.Checking(check_url, 'name', 'BestOfTheBestQA', 60, self.headers).absence() # check whether repo has been deleted
