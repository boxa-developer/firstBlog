from django.urls import path
from .views import (
    all_posts, add_auth,
    authors, get_tags,
    add_tag, update_tag,
    delete_tag, get_tag,
    get_auth,
)

urlpatterns = [
    # Posts URL routing
    path('post/all', all_posts, name='all_p'),
    # Auth URL routing
    path('auth/add', add_auth, name='add_u'),
    path('auth/all', authors),
    path('auth/get/<int:auth_id>', get_auth),
    # Tags URL routing
    path('tag/all', get_tags),
    path('tag/get/<int:tag_id>', get_tag),
    path('tag/add', add_tag),
    path('tag/update', update_tag),
    path('tag/delete', delete_tag)
]
