# Format Release for GitLab

Этот скрипт преобразует данные из текстового файла в форматированный список. 

## Как использовать

1. Создайте файл `input.txt` в директории скрипта и добавьте данные в следующем формате (скопируйте из relases в jira соответсвующего номера релиза):

```
Проблема 
[ROAD-23219] - Описание проблемы 1
[ROAD-23221] - Описание проблемы 2
Задача 
[ROAD-23276] - Описание задачи 1
```

2. Запустите скрипт:
```bash
python script.py
```

3. Форматированный вывод будет сохранён в файле `output.txt`.

```
**Проблема**
- [ROAD-23219] - Описание проблемы 1
- [ROAD-23221] - Описание проблемы 2
**Задача** 
- [ROAD-23276] - Описание задачи 1
```
