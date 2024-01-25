import requests
from pprint import pprint


class PostsApiClient:
    URL = 'https://jsonplaceholder.typicode.com/'

    def get_posts_by_user(self, userId):
        response = requests.get(f'{self.URL}/posts?userId={userId}')
        posts = response.json()
        first_3 = posts[:3]
        return first_3, len(posts) - 3

    def get_comments_by_post(self, postId):
        response = requests.get(f'{self.URL}/comments?postId={postId}')
        return response.json()

    def create_post(self, new_post):
        response = requests.post(f'{self.URL}/posts', json=new_post)
        return response.json()
    def get_to_do_by_user(self,userId):
        response=requests.get(f'{self.URL}/todos?usedId={userId}&completed=false')
        return response.json()

client=PostsApiClient()
posts,left=client.get_posts_by_user(1)

pprint(posts)
print(f'+{left} more posts/')



'''
2. Alege un post, și afișează lista de comentarii. Alege un album, si afiseaza lista de photos.
'''

pprint(client.get_comments_by_post(100))
'''3. Creeaza un post nou 
(atentie, acesta NU va fi salvat, dar putem
 analiza răspunsul pentru a vedea cum ar arata în
  viitor dacă ar fi fost salvat). Încearcă să-l
   creezi cu si fără id. Ce observi?
'''
payload={
    'title':'new title',
    'body':'new body',
    'userId':1


}
pprint(client.create_post(payload))

'''5. Folosind query parameters, filtrează lista de todos pentru userul ales 
astfel incat sa afisezi doar todos care nu sunt completed.
'''

pprint(client.get_to_do_by_user(1))