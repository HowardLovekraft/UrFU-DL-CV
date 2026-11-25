# Ссылка на датасет
[https://disk.yandex.ru/d/ywO9_qnlDulNgQ](https://disk.yandex.ru/d/ywO9_qnlDulNgQ)

# Условие
Решить задачу классификации изображений (https://disk.yandex.ru/d/ywO9_qnlDulNgQ). 
Метки по умолчанию — алфавитный порядок папок классов 
(butterfly=0, cat=1, ...).

Формат ответа (Смотри пример `submission_dl1.csv`):
```csv
FILE_NAME,TARGET 
ee32b90c29f11c22d2524518b7444f92e37fe5d404b0144390f8c079a4e5b6_640.jpg,0
ee33b00e2ee90021d85a5854ee454296eb70e3c818b413449df1c17fa2ee_640.jpg,0
ee37b70620fd1c22d2524518b7444f92e37fe5d404b0144390f8c079a2efb1_640.jpg,0
ee3cb70b2bf31c22d2524518b7444f92e37fe5d404b0144390f8c079a2efb1_640.jpg,0
```

# Запуск
```shell
# Выберите версию PyTorch - CPU- или CUDA-версию
vi pyproject.toml
uv sync
# В одной сессии
uv run mlflow server 5000
# В другой сессии
uv run jupyter lab
```