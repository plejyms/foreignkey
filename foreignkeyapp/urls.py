from django.urls import path 
from .import views 
urlpatterns=[ 
path('',views.home,name='home'),
path('addcourse',views.addcourse,name='addcourse'),
path('addstudent',views.addstudent,name='addstudent'),
path('show_student',views.show_student,name='show_student'),
path('add',views.add,name='add'),
path('add_student',views.add_student,name='add_student'),
path('show_student',views.show_student,name='show_student'),
path('editpage/<int:pk>',views.editpage,name="editpage"),
path('edit_student_details/<int:pk>',views.edit_student_details,name="edit_student_details"),
path('deletepage/<int:pk>',views.deletepage,name="deletepage"),
]