import requests
Github_URL = "https://api.github.com/search/repositories"
search_word = input("Enter search word")
Github_sort_order= "star"
Github_display_order= "desc"
Github_PARAM = { 'q':search_word,'sort':Github_sort_order,'order':Github_display_order }
Github_response = requests.get(url = Github_URL, params = Github_PARAM)
Github_data = Github_response.json()
print(Github_data)
print ("----------------")
Gitlab_URL = "https://gitlab.com/api/v4/projects"
Gitlab_param = { 'q':search_word }
Gitlab_response = requests.get(url = Gitlab_URL, params = Gitlab_param )
Gitlab_data = Gitlab_response.json()
print(Gitlab_data)

# need to process json response