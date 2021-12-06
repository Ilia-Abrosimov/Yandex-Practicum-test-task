###Тестовое задание в Яндекс.Практикум на "Создатель автоматических тестов на python".
___
Для каждого задания написаны тесты, которые находятся в соответствующих папках. Для первого задания описание тестов находится в файле `test.txt`.  
В папке `fixtures` созданы фикстуры, которые имитируют stdout работы файла с кодом студента (все его print()) в виде одной строки.

# Как выполнять задания
Первое задание не требует написания кода.
Для остальных трёх задач необходимо написать тесты, проверяющие решение студента, и дающие подсказки в случае ошибок.

### Что предоставляет платформа для тестов:
- Решение студента импортируется в тестовый модуль, соответственно все переменные, классы и функции студента доступны в нем. 
- `user_code` — переменная, в которой в виде строки хранится весь код студента.
- `output` — stdout работы файла с кодом студента (все его `print()`) в виде одной строки. 

### Рекомендации по решению заданий
1. Тест должен проверить правильность конечного решения студента, а также шаги, которые к этому решению привели.  
2. Описание найденной ошибки (assert message) должно подсказывать что не так сделал студент.  
3. Сама проверка происходит, используя `assert` и текстовое сообщения студенту:
`assert False, 'Вы ошиблись в выводе на экран'`  
4. Авторское решение не является идеальным, но в рамках задачи будет для вас эталонным, и решение, к которому придет студент, наверняка будет существенно ниже по качеству, так что при написании тестов крайне важно мыслить как студент, а не как автор, который сразу пишет рабочее решение.

### Типичные ошибки студентов
Часто бывает, что студенты изменяют или удаляют исходные переменные, которые мы им даем в прекоде, что потом часто заводит их в тупик.  

### Примечания: 
- Версия Python 3.7
- Тесты нужно писать на чистом pytest, никакого unittest не нужно
- При написании тестов крайне желательно обходиться стандартными библиотеками и модулями, и избегать доп. модулей для pytest без острой необходимости

## Список файлов
В папках с задачами находится прекод (с которого студент начинает решать задание) и авторское (эталонное) решение, по которому пишутся тесты.  
- `precode.py` — прекод для студента
- `author.py` — эталонное решение
- `test.py` — напишите ваш тест в этом файле

## Удачи!