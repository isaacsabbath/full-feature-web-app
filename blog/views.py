from django.shortcuts import render

posts = [
{
       'author': 'Isaacs',
       'title': 'blog post 1',
       'content': 'Firstblog post',
       'date_posted' : 'March 1, 2023'
},
{
       'author': 'Wangui',
       'title': 'blog post 2',
       'content': 'Secondblog post',
       'date_posted' : 'March 1, 2023'
}
]

def home(request): #function to return a http request
       context = {
              'posts': posts
       }
       return render(request, 'blog/home.html', context)

def about(request):
       return render(request, 'blog/about.html', {'title': 'About'})

       

