# Expert_ARd

Выставочный-тестовый образец необходимые объяснения внутри.

Если кратко указываем путь к файлу пдф, получаем схожий с эталоном текст (Наименование объекта капитального строительства - ОКС), степень схожести, номер страницы на которой выявлен схожий с эталоном текст, а также пдф файл с подчеркнутым схожим текстом. Есть функция для исправления орфографических ошибок схожего текста, но пока не стал включать в докер.

EXPERT.ipynb - содержит разные эксперименты с моделью и демонстрационный вариант.

EXPERT_2.ipynb - основной рабочий код (учтите что времени было всего 3 дня). Было бы больше времени там и преобразовать пдф в картинки можно и потом сегментировать текст налево и направо.

создано все необходимое для докера - папка Хакатон. Находясь в терминале в папке docker: 

docker build -t myapp .

docker run myapp

есть проблемы с вводом эталонного текста при сборке. Пока не разобрался как решить думаю эксперты поймут.

обратите внимание на видео-демонстрацию. При необходимости можно воспользоваться ссылкой в колаб где первоначально работал и проверить работоспособность заменив пути файлов в демонстрационном варианте. не забудьте подгрузить библиотеки модули инструменты из первого раздела в том числе pip (если будете ориентироваться на colab). https://colab.research.google.com/drive/1ZPBaL-IDqBB-bLk4ciHdNGZ1gKLJv0Vk?usp=sharing
