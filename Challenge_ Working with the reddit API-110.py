## 2. Authenticating with the API ##

headers = {"Authorization": "bearer 13426216-4U1ckno9J5AiK72VRbpEeBaMSKk", "User-Agent": "Dataquest/1.0"}

params = {"t":"day"}

python_top = requests.get("https://oauth.reddit.com/r/python/top", headers=headers, params=params).json()

print(python_top)

## 3. Getting the Most Upvoted Post ##

headers = {"Authorization": "bearer 13426216-4U1ckno9J5AiK72VRbpEeBaMSKk", "User-Agent": "Dataquest/1.0"}

params = {"t":"day"}

python_top = requests.get("https://oauth.reddit.com/r/python/top", headers=headers, params=params).json()

#print(python_top)

teste = python_top['data']['children'][0]['data']['title']

most_upvoted = python_top['data']['children'][0]['data']['id']

## 4. Getting Post Comments ##

comments = requests.get("https://oauth.reddit.com/r/python/comments/4b7w9u", headers=headers).json()

## 5. Getting the Most Upvoted Comment ##

headers = {"Authorization": "bearer 13426216-4U1ckno9J5AiK72VRbpEeBaMSKk", "User-Agent": "Dataquest/1.0"}

comments = requests.get("https://oauth.reddit.com/r/python/comments/4b7w9u", headers=headers).json()

comments_list = comments[1]['data']['children']

most_upvoted_comment = comments_list[2]['data']['id']

## 6. Upvoting a Comment ##

#Creating these params in order to vote for a comment of this specific  id user
payload= {'dir': 1, 'id': 'd16y4ry'}

headers = {"Authorization": "bearer 13426216-4U1ckno9J5AiK72VRbpEeBaMSKk", "User-Agent": "Dataquest/1.0"}

vote = requests.post("https://oauth.reddit.com/api/vote", headers=headers, json=payload)

status = vote.status_code