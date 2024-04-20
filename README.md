# Проект по тестированию сайта [invest.akbars.ru](https://invest.akbars.ru/) - цифровые инвестиционные продукты:
- ИИС
- БС
- ПИФы
- Доверительное управление
----


> Открытие инвест-продуктов  

> Пополнение

Главная страница сайта [invest.akbars.ru](https://invest.akbars.ru/)
![invest.akbars.ru](/images/site_main.png)

Форма для подачи заявки на открытие продукта
![invest.akbars.ru](/images/open_iis.png) 
Автотесты и ручные тесты в рамках данного проекта заполняют данную форму по шагам. 

----

## Список проверок, реализованных в автотестах:

### UI автотесты:

- [x] Переход к форме открытия счёта (ИИС\БС\ДУ) и открытие в шаге 1 статичных документов (2 документа)
- [x] в шаге 1 заполнение обязательных полей и переход к следующему шагу
- [x] В шаге 1 попытка перейти к следующему шагу не заполнив поля
- [x] в шаге 2 заполнение обязательных полей и переход к следующему шагу
- [x] в шаге 3 - поля по умолчанию и переход к шагу 4

![image](/images/autotests.png)
----
## Список ручных тестов:

![image](/images/manual_tests.png)
### Проект реализован с использованием:


![python](https://raw.githubusercontent.com/temirkhanovams/temirkhanovams/main/icons/python.png)
![pytest](https://raw.githubusercontent.com/temirkhanovams/temirkhanovams/main/icons/pytest.png)
![pycharml](https://raw.githubusercontent.com/temirkhanovams/temirkhanovams/main/icons/pycharm.png)
![selene](https://raw.githubusercontent.com/temirkhanovams/temirkhanovams/main/icons/selene.png)
![selenium](https://raw.githubusercontent.com/temirkhanovams/temirkhanovams/main/icons/selenium.png)
![selenoid](https://raw.githubusercontent.com/temirkhanovams/temirkhanovams/main/icons/selenoid.png)
![jenkins](https://raw.githubusercontent.com/temirkhanovams/temirkhanovams/main/icons/jenkins.png)
![allure_report](https://raw.githubusercontent.com/temirkhanovams/temirkhanovams/main/icons/allure_report.png)
![allure_testops](https://raw.githubusercontent.com/temirkhanovams/temirkhanovams/main/icons/allure_testops.png)
![jira](https://raw.githubusercontent.com/temirkhanovams/temirkhanovams/main/icons/jira.png)
![github](https://raw.githubusercontent.com/temirkhanovams/temirkhanovams/main/icons/github.png)
![telegram](https://raw.githubusercontent.com/temirkhanovams/temirkhanovams/main/icons/telegram.png)
![git](https://raw.githubusercontent.com/temirkhanovams/temirkhanovams/main/icons/git.png)


> Для полноценного прохождения всех тестов необходимо в шаге 4 ввести код, полученный в смс - это ручной тест.
`.env`
>
Для написания UI-тестов используется фреймворк `Selene`, современная «обёртка» вокруг `Selenium WebDriver`, паттерн PageObject.  
Библиотека модульного тестирования: `PyTest`  
`Jenkins` выполняет удаленный запуск тестов в графическом интерфейсе. Установки дополнительных приложений на компьютер
пользователя не требуется.  
`Selenoid` запускает браузер с тестами в контейнерах `Docker` (и записывает видео)  
Фреймворк `Allure Report` собирает графический отчет о прохождении тестов  
После завершения тестов `Telegram Bot` отправляет в `Telegram` краткий вариант `Allure Report`

----

### Локальный запуск
Ветка на github: [for_allure_in_local](https://github.com/temirkhanovams/qa_guru_project_homework_15/blob/for_allure_in_local)

1) Скачать проект и открыть в IDE
Необходимо создать в корне проекта файл `.env` и заполнить его актуальными тестовыми параметрами:  
`LOGIN="***"`  
`PASSWORD="***"`  
2) Для локального запуска необходимо выполнить команду в терминале:  
   - [x] Запустить все тесты через консоль, если настроен pytest.ini (указана папка для хранения отчетов)  
      ```commandline
      pytest
      ```
      или
      ```commandline
      pytest .\tests\invest_akbars\
      ```
   - [x] Запустить все тесты, если в pytest.ini не указаны параметры папки и параметры удаления
      ```commandline
      pytest --clean-alluredir --alluredir=allure-results
      ```
   - [x] Запустить определённый тест отдельно:  
      ```commandline
      pytest .\tests\invest_akbars\test_open_iis_form.py::test_form_open_iis_step3_positive
      ```
3) Сгенерировать allure-отчёт (локальный) - Windows в корне проекта в папке allure-results
```commandline
allure.bat serve allure-results
```
или без указания папки (он указан в файле pytest.ini)
```commandline
allure.bat serve
```

4) Результат: откроется web-страница с отчетом Allure Report

----

### ![jenkins](https://raw.githubusercontent.com/temirkhanovams/temirkhanovams/main/icons/jenkins.png) Удаленный запуск автотестов  
- Выполняется на сервере Jenkins
> <a target="_blank" href="https://jenkins.autotests.cloud/job/C10_Marina_t_s_unut15_MY_PROJECT">Ссылка на проект в Jenkins</a>
----
#### Для запуска автотестов в Jenkins  
1. Открыть <a target="_blank" href="https://jenkins.autotests.cloud/job/C10_Marina_t_s_unut15_MY_PROJECT">проект в Jenkins (job)</a>
2. Выбрать пункт `Build with Parameters`
3. Выбрать браузер
4. Выбрать версию браузера
4. Указать комментарий для уведомления в Телеграмм
5. Нажать кнопку `Build`
6. Результат запуска сборки можно посмотреть в отчёте Allure  
---
### 1) Проект в Jenkins  
[Project in Jenkins](https://jenkins.autotests.cloud/job/C10_Marina_t_s_unut15_MY_PROJECT)
![Project in Jenkins](/images/jenkins_job.png)
### 2) Параметры запуска билда в Jenkins  
- Либо с параметрами по умолчанию
- Либо указать свои параметры
![Build in Jenkins](/images/jenkins_build_parametrize.png)
После этого запустится билд, а после его выполнения рядом появятся иконки для просмотра отчётов в Allure и AllureTestOps
![image gif](https://raw.githubusercontent.com/temirkhanovams/temirkhanovams/main/video/build_11.gif)
### 3) ![Allure logo](https://raw.githubusercontent.com/temirkhanovams/temirkhanovams/main/icons/allure_report.png) Allure отчет по автотестам  
[Report in Allure](https://jenkins.autotests.cloud/job/C10_Marina_t_s_unut15_MY_PROJECT/11/allure/#suites/f060e8ca884180d3ef8856f59eb3c0d5/3ed5e72d9f0c075/)  
![image_allure_report](images/allure_report_11.png)  
![Report in Allure](/images/allure_report_build_11.png)

Отчет позволяет получить детальную информацию по всем шагам тестов, включая скриншоты и log - файлы

#### <img width="3%" title="Allure report" src="https://raw.githubusercontent.com/temirkhanovams/temirkhanovams/main/icons/selenoid.png"> Видео прохождения теста:

Видеозапись каждого теста генерируется с помощью `Selenoid` после успешного запуска тестов.

![image_gif](https://raw.githubusercontent.com/temirkhanovams/temirkhanovams/main/video/Step3.gif)

### <img width="3%" title="Allure report" src="https://raw.githubusercontent.com/temirkhanovams/temirkhanovams/main/icons/telegram.png"> Получение уведомлений о прохождении тестов в Telegram

После завершения сборки специальный Telegram-бот отправляет сообщение с отчетом.

![telegram_report_10](/images/telegram_report_10.png)
![telegram_report_11](/images/telegram_report_11.png)

### <img width="3%" title="Allure report" src="https://raw.githubusercontent.com/temirkhanovams/temirkhanovams/main/icons/allure_testops.png"> Интеграция с Allure TestOps
[Dashboards AllureTestOps](https://allure.autotests.cloud/project/4179/dashboards)  
Так же вся отчетность сохраняется в Allure TestOps, где строятся аналогичные графики.  

![Dashboards AllureTestOps](/images/allure_testops_dashboards.png) 

TestOps также позволяет:
- Добавлять к [Suite AllureTestOps](https://allure.autotests.cloud/project/4179/test-cases?treeId=8184)   ручные тесты 
- Управлять всеми тест-кейсами или с каждым отдельно
- Перезапускать каждый тест отдельно от всех тестов
- Настроить интеграцию с Jira и др.  
![allure_testops_suites](/images/allure_testops_suites.png) 

---

### <img width="3%" title="Allure report" src="https://raw.githubusercontent.com/temirkhanovams/temirkhanovams/main/icons/jira.png"> Интеграция с Jira
[Jira issue](https://jira.autotests.cloud/browse/HOMEWORK-1192)  
Настроив через Allure TestOps интеграцию с Jira, [в задаче](https://jira.autotests.cloud/browse/HOMEWORK-1192) можно интегрировать результаты прохождения тестов и список тест-кейсов из AllureTestOps.  
А также после прохождения ручных и автотестов создать Release в AllureTestOps, и интегрировать его результаты тоже.  

[Тест-раны в AllureTestOps](https://allure.autotests.cloud/project/4179/launches)
- Здесь видим ран, который был запущен через Jenkins. Он с автотестами `C10_Marina_t_s_unut15_MY_PROJECT - #11`
- И Run с автотестами и ручными тестами `Release_003`, который был собран вручную в AllureTestOps. 

AllureTestOps, будучи системой управления тестами, позволяет запускать автотесты, и выполнять всевозможные манипуляции с ручными тестами.
![Dashboards AllureTestOps](/images/allure_testops_runs.png) 

В задаче Jira - результаты прохождения тест-ранов из AllureTestOps, а также список тестов, относящихся к данной задаче.

![Dashboards AllureTestOps](/images/jira_vs_allure_integration.png) 
