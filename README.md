# Sprint_6  Яндекс.Практикум
## Описание структуры проекта
### 📁 Корень проекта
### Файлы
* conftest.py - файл с фикстурой  
* storage.py - хранилище входных данных для проведения тестирования
* helper.py - файл со вспомогателньыми функциями
* requirements.txt — это список всех модулей и пакетов Python, которые нужны для полноценной работы данной программы.

#### 📁 tests - директория с тестами  
* __init__.py - файл необходимый для того, чтобы Python обрабатывал каталоги, содержащие файл, как пакеты
* test_main_page.py - тесты для главной страницы Яндекс.Самокат  
* test_order.py - тесты для формы заказов и редиректов на главную страницу сервиса и Дзен

#### 📁 pages - директория с базовыми страницами  
* __init__.py - файл необходимый для того, чтобы Python обрабатывал каталоги, содержащие файл, как пакеты
* base_page.py - файл с методами для работы с общими элементами проекта  
* main_page.py - файл с методами для главной страницы  
* order_page.py - файл с методами для формы заказа и редиректов на главную страницу и Дзен

#### 📁 locators - директория с локаторами  
* __init__.py - файл необходимый для того, чтобы Python обрабатывал каталоги, содержащие файл, как пакеты
* locators.py - локаторы для всех элементов проекта

#### 📁 allure_results - отчеты о тестировании от фреймворка Allure

 