from django.http import HttpResponse, HttpResponseNotFound
from django.urls import path
from django.shortcuts import render

# Create your views here.

calling_card = {
       "name": "Иван",
       "middle": "Петрович",
       "surname": "Иванов",
       "phone": "8-923-600-01-02",
       "email": "vasya@mail.ru"
}

items = [
{"id": 1, "name": "Кроссовки abibas" ,"quantity":5},
{"id": 2, "name": "Куртка кожаная" ,"quantity":2},
{"id": 5, "name": "Coca-cola 1 литр" ,"quantity":12},
{"id": 7, "name": "Картофель фри" ,"quantity":0},
{"id": 8, "name": "Кепка" ,"quantity":124},
]

def home(request):
   context = {
       "name": 'Себастьян Перейро',
       "email": 'my_mail@mail.ru'
   }
   return render(request, "index.html", context)
    # text = """<h1>"Изучаем django"</h1>
    #          <strong>Автор</strong>: <i>Иванов И.П.</i>
    #          <br><a href="about">about</a></br>
    #          <a href="items_list">items_list</a></br>
    #          <a href="item">item</a>
    #          """
    # return HttpResponse(text)

def about(request):
    about_me = f"""
    Имя: <b>{calling_card["name"]}</b><br>
    Отчество: <b>{calling_card["middle"]}</b><br>
    Фамилия: <b>{calling_card["surname"]}</b><br>
    Телефон: <b>{calling_card["phone"]}</b><br>
    Email: <b>{calling_card["email"]}</b><br>
    """

    return HttpResponse(about_me)


# utr /item/1
# utr /item/2

# Списки, кортежи, строки это индексы
# Словари - это ключи

def get_item(request, id):
    """По указанному id функция возвращает имя и кол-во"""
    for item in items:
        if item['id'] == id:
            context = {
                'item' : item
            }
            return render(request, "item-page.html", context)
        
            # if item['id'] == id:
        #      result = f"""
        #      <h1>Имя: {item["name"]} </h1>
        #      <p>Количество: {item["quantity"]}</p>
        #      <a href='/items_list'> Назад </a>
        #      """
        #      return HttpResponse(result)
        
            
    # return HttpResponseNotFound(f'Item with id={id} not found')

def items_list(request):
    # result = "<h2>Список товаров</h2><ol>"
    # for item in items:
    #     result += f"<li><a href='/item/{item['id']}'>{item['name']}</li>"
    # result += '</ol>'
    # return HttpResponse(result)
    context = {
        "items": items
    }
    # Аргументы render: Запрос(request), Имя шаблона, Контекст(чем заполняем)
    return render(request, "items-list.html", context)

