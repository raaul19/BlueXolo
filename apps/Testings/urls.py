from django.conf.urls import url

from .views import KeyWordsView, NewKeywordView, DeleteKeywordView, CollectionsView, NewCollectionsView, EditCollectionsView, \
    DeleteCollectionsView, EditKeywordView, TestcaseView, NewTestcaseView, EditTestcaseView, DeleteTestcaseView



urlpatterns = [
    url(r'^keywords/$', KeyWordsView.as_view(), name="keywords"),
    url(r'^keywords/new/$', NewKeywordView.as_view(), name="new-keywords"),
    url(r'^keywords/edit/(?P<pk>\d+)$', EditKeywordView.as_view(), name="edit-keywords"),
    url(r'^keywords/(?P<pk>\d+)/delete/$', DeleteKeywordView.as_view(), name="delete-keywords"),
    #TestCase
    url(r'^testcases/$', TestcaseView.as_view(), name="testcases"),
    url(r'^testcases/new/$', NewTestcaseView.as_view(), name="new-testcase"),
    url(r'^testcases/edit/(?P<pk>\d+)$', EditTestcaseView.as_view(), name="edit-testcase"),
    url(r'^testcases/(?P<pk>\d+)/delete/$', DeleteTestcaseView.as_view(), name="delete-keywords"),
    #Collections
    url(r'^collections/$', CollectionsView.as_view(), name="collections"),
    url(r'^collections/new/$', NewCollectionsView.as_view(), name="new-collections"),
    url(r'^collections/(?P<pk>\d+)/$', EditCollectionsView.as_view() , name='edit-collections'),
    url(r'^collections/(?P<pk>\d+)/delete/$', DeleteCollectionsView.as_view(), name="delete-collections"),
]