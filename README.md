# Sprint_5
**Проект 5 спринта, UI testing сайта Stellar Burgers.**

**Структура проекта**
* locators.py — содержит локаторы для всех элементов интерфейса.
* curl.py — содержит URL-адреса используемых страниц.
* data.py — содержит тестовые учетные данные.
* helper.py — содержит вспомогательные функции для генерации данных.
* conftest.py - содержит фикстуры

### **Сценарии, покрытые тестами**

**Регистрация**  
* Успешная регистрация
test_success_registration()
Проверяет регистрацию с валидными данными: имя, email в формате логин@домен, пароль ≥ 6 символов.

* Некорректный пароль
test_registration_invalid_password_error_message()
Проверяет, что при вводе недопустимого пароля появляется сообщение об ошибке.

* Пустой пароль
test_registration_empty_password_no_message()
Проверяет, что при попытке регистрации с пустым паролем регистрация не проходит.

**Вход в аккаунт**  
* С главной страницы  
test_enter_account_main_page_valid_credentials_account_opened()  
Проверяет вход по кнопке «Войти в аккаунт» на главной.

* Через кнопку «Личный кабинет»  
test_enter_account_account_page_valid_credentials_account_opened()  
Переход в «Личный кабинет», затем авторизация.  

* Через форму регистрации  
test_enter_account_registration_form_valid_credentials_account_opened()  
Переход из регистрации в форму входа, затем вход.  

* Через восстановление пароля  
test_enter_account_forgot_password_valid_credentials_account_opened()  
Переход из формы восстановления в форму входа, затем вход.

**Переходы**  
* Переход в «Личный кабинет»  
test_goto_account_account_opened()  
Проверка перехода по клику на кнопку «Личный кабинет».

* Переход из «Личного кабинета» в «Конструктор»  
По кнопке «Конструктор»: test_goto_constructor_main_site_opened()  
По клику на логотип: test_goto_constructor_logo_main_site_opened()

**Выход из аккаунта**  
Выход через личный кабинет  
test_exit_account_main_site_opened()  
Проверяет, что пользователь выходит из аккаунта и попадает на страницу входа.

**Раздел «Конструктор»**  
* Переход к разделу «Соусы»  
test_sauces_scroll_to_sauces_section()  
Проверяет клик по табу и наличие заголовка.

* Переход к разделу «Булки»  
test_buns_scroll_to_buns_section()  
Проверяет переход к разделу «Булки».

* Переход к разделу «Начинки»
test_fillings_scroll_to_fillings_section()
Проверяет переход к разделу «Начинки».

