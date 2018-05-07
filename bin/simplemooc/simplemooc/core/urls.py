from django.urls import path
from .views import listar_todos_produtos, criar_novo_produto, update_produto, delete_produto
urlpatterns = [
    path('', listar_todos_produtos, name="listar_todos_produtos"),
    path('novo-produto', criar_novo_produto, name='criar_novo_produto'),
    path('update-produto/<int:id>/', update_produto, name='update_produto'),
    path('delete-produto/<int:id>/', delete_produto, name='delete_produto')

]