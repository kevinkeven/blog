from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('<slug:slug>', views.PostDetailView.as_view(), name='post_detail'),
    #path('tag/<slug:slug>', views.PostDetailView.as_view(), name='post_list_by_tag'),
    path('<slug:slug>/share', views.PostShareView.as_view(), name='share_post'),
    path('sharer/done', views.SharedPostView.as_view(), name='share_done'),
    path('contact/us', views.ContactUsView.as_view(), name='contact_us'),
    path('search/', views.SearchView.as_view(), name='search'),
]
