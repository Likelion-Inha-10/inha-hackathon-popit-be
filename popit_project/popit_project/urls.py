from django.contrib import admin
from django.urls import path
from django.views import View
from accounts import views as accounts_views
from profiles import views as profiles_views

from rest_framework_simplejwt.views import TokenRefreshView
# from profiles import views as profiles_views
from add_pop import views as add_pop_views
from django.conf import settings
from django.conf.urls.static import static 
from hamburgers import views as hamburgers_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # 회원가입, 로그인, 로그아웃
    path("signup", accounts_views.RegisterAPIView.as_view()),
    path("login", accounts_views.AuthView.as_view()), 
    path("logout", accounts_views.logout.as_view()),
    
    # 유저 상세 내용 조회(프로필)
    #path('profile/<int:user_id>', profiles_views.main_profile, name = 'main_profile'),

    # 팝 관련
    path('pop', profiles_views.pop_list_all, name = 'pop_list'), # 전체 팝 리스트 조회
    path('pop/pop_list/<int:user_id>', profiles_views.pop_list_user, name = 'pop_list_user1'), # 특정 유저에 대한 팝 리스트 조회
    path('pop/pop_list/create_pop_user_category/<int:user_id>/<int:category_id>', profiles_views.create_pop_user_category, name = 'create_pop_user_category'),  # 특정 유저에 종속하며, 특정 카테고리에 속하는 팝 생성하기    
    path('pop/pop_list/<int:user_id>/<int:pop_id>', profiles_views.pop_list_user2, name = 'pop_list_user2'),
    path('pop/<int:pop_id>/pop_detail', profiles_views.pop_detail, name = 'pop_detail'), # 특정 팝 조회, 수정, 삭제

    # 댓글 관련
    path('comment', profiles_views.comment_list, name = 'comment_list'),  # 모든 댓글 리스트 가져오기
    path('<int:pop_id>/comments', profiles_views.comment_create, name = 'comment_create'), # 특정 해당 팝에 댓글 작성하기 + 특정 팝의 댓글 리스트 가져오기
    path('comment/<int:comment_id>', profiles_views.comment_detail, name = 'comment_detail'), # 특정 댓글 조회, 수정, 삭제하기

    # 프로필 관련
    path('my_profile', profiles_views.my_profile, name = 'my_profile'), # 본인(= 현재 로그인된 회원)에 대한 프로필 띄우기 및 수정
    path('other_profile/<int:user_id>', profiles_views.other_profile, name = 'other_profile'), # 타인에 대한 프로필 띄우기 


    # 햄버거 관련
    path('my_comment_list', hamburgers_views.my_comment_list, name = 'my_comment_list'),
    path('likecount_list', hamburgers_views.likecount_list.as_view(), name = 'likecount_list'),
    path('comment_count_list', hamburgers_views.comment_count_list.as_view(), name = 'comment_count_list'),
    path('created_at_list', hamburgers_views.created_at_list.as_view(), name = 'created_at_list'),

    # 카테고리 or 햄버거 관련 (by 한주형)
    path('follow/<int:user_id>', profiles_views.follow),
    path('viewfollowings',profiles_views.view_followings),
    path('viewfollowers',profiles_views.view_followers),
    path('set_category',profiles_views.set_category),  #사용자가 카테고리들 선택하고 완료버튼 눌렀을때 json으로 넘어온 데이터 처리 
    path('view_category',profiles_views.view_category), #사용자가 카테고리 뭐 골랐는지 보여주기
    path('view_selected_category_pop/<int:category_id>',profiles_views.view_selected_category_pop),
    path('like/<int:pop_id>',profiles_views.like),
] 

# media 파일에 접근할 수 있는 url 도 추가해줘야 함
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

'''
    path('addChemipop',add_pop_views.ChemiPopList.as_view()),
    path('addPythonpop',add_pop_views.PythonPopList.as_view()),
    path('addDjangopop',add_pop_views.DjangoPopList.as_view()),
    path('addEnginMathpop',add_pop_views.EnginMathPopList.as_view()),
    path('addTOEICpop',add_pop_views.TOEICPopList.as_view()),
    
    path('Chemipop/<int:pk>',add_pop_views.ChemiPopDetail.as_view()),  
    path('Pythonpop/<int:pk>',add_pop_views.PythonPopDetail.as_view()),  
    path('Djangopop/<int:pk>',add_pop_views.DjangoPopDetail.as_view()),  
    path('EnginMathpop/<int:pk>',add_pop_views.EnginMathPopDetail.as_view()),  
    path('TOEIC/<int:pk>',add_pop_views.TOEICPopDetail.as_view()),  
    
    path('Chemipoplike/<int:pk>',add_pop_views.ChemiPopDetail.as_view()),

    #path('pop_pressed/<int:pop_id>', profiles_views.pop_pressed, name = 'pop_pressed'),
    #path('follow/<int:user_id>', profiles_views.follow, name = 'follow'),
'''