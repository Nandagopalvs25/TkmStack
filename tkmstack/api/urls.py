from django.urls import path

from .views import StackList,TagCreate,StackDetail,AnswersCreate

urlpatterns = [
    path("stacks",StackList.as_view(),name="stack_list"),
    path("tags",TagCreate.as_view(),name="tag_create"),
     path("answer",AnswersCreate.as_view(),name="answers_create"),
    path("stack/<int:pk>/", StackDetail.as_view(), name="stack_detail"),
]