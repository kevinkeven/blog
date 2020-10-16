from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from .models import Comment, Post, Feedback
from .forms import EmailPostShare, CommentForm, FeedbackForm
from django.db.models import Count
import time
from django.core.mail import send_mail
from django.views import generic
from django.contrib.postgres.search import SearchVector, SearchRank, SearchQuery

# Create your views here.
class PostListView(generic.ListView):
    queryset = Post.published.all()
    paginate_by = 5
    template_name = 'blog/post/post_list.html'
    context_object_name = 'posts'
        

class PostDetailView(generic.DetailView, generic.FormView):
    queryset = Post.published.all()
    form_class = CommentForm
    template_name = 'blog/post/post_detail.html'

    def form_valid(self, form):
        self.object = self.get_object()
        new_comment = form.save(commit=False)
        new_comment.post = self.object
        new_comment.save()

        return redirect(reverse('blog:post_detail', kwargs={'slug': self.object.slug}))

    def get_context_data(self, **kwargs):
        self.object = self.get_object()
        ctx = super().get_context_data(**kwargs)
        post_tags_ids = self.object.tags.values_list('id', flat=True)
        similar_posts = Post.published.filter(tags__in=post_tags_ids).exclude(id=self.object.id)
        ctx['similar_posts'] = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags','-publish')[:4]
        ctx['comments'] = self.object.comments.filter(active=True)
        return ctx



class PostShareView(generic.FormView, generic.DetailView):
    queryset = Post.published.all()
    form_class = EmailPostShare
    template_name = 'blog/post/share.html'
    context_object_name = 'post'
    
    def form_valid(self, form):
        self.object = self.get_object()
        cd = form.cleaned_data
        post_url = self.request.build_absolute_uri(self.object.get_absolute_url())
        subject = '{} ({}) recommends you reading "{}"'.format(cd['name'], cd['email'], self.object.title)
        message = 'Read "{}" at {}\n\n{}\'s comments:{}'.format(self.object.title, post_url, cd['name'], cd['comments'])
        send_mail(subject, message, 'admin@myblog.com', [cd['to']])

        return redirect(reverse_lazy('blog:share_done'))
    

class SharedPostView(generic.TemplateView):
    template_name = 'blog/post/share_done.html'

class PostCommentView(generic.FormView, generic.DetailView):
    queryset = Post.published.all()
    form_class = CommentForm
    template_name = 'blog/post/share.html'

class ContactUsView(generic.TemplateView, generic.FormView):
    template_name = 'blog/feedback.html'
    form_class = FeedbackForm
    sent = False

    def form_valid(self, form):
        cd = form.cleaned_data
        subject = '{} ({}) Feedback'.format(cd['name'], cd['email'])
        message = cd['message']
        sender = cd['email']
        send_mail(subject, message, sender, ['admin@myblog.com'])
        self.sent = True

        return redirect(reverse_lazy('blog:contact_us'))

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['sent'] = self.sent
        return ctx

class SearchView(generic.View):
    def get(self, request, *args, **kwargs):
        queryset = Post.published.all()
        query = request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) |
                Q(overview__icontains=query)                
            ).distinct()
        
        context = {
            'result': queryset,
            'query': query
        }

        return render(request, 'blog/post/search.html', context)