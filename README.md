# «Python и БД. ORM»
___
__1.__ Составить модели классов SQLAlchemy по схеме:
![](book_publishers_scheme.png)

Легенда: система хранит информацию об издателях (авторах), их книгах и фактах продажи. Книги могут продаваться в разных магазинах, поэтому требуется учитывать не только что за книга была продана, но и в каком магазине это было сделано, а также когда.

Интуитивно необходимо выбрать подходящие типы и связи полей.

__2.__ Используя SQLAlchemy, составить запрос выборки магазинов, продающих целевого издателя.

Напишите Python-скрипт, который:

- подключается к БД любого типа на ваш выбор, например, к PostgreSQL;
- импортирует необходимые модели данных;
- принимает имя или идентификатор издателя (publisher), например, через input(). Выводит построчно факты покупки книг этого издателя:

>_название книги | название магазина, в котором была куплена эта книга | стоимость покупки | дата покупки_

__3.__ Заполните БД тестовыми данными.

Пример содержания в JSON-файле.

Возможная реализация: прочитать JSON-файл, создать соотведствующие экземляры моделей и сохранить в БД.