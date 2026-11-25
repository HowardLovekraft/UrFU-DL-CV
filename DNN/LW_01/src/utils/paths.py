from pathlib import Path
from typing import Callable


def fixdir(func: Callable[[], Path]):
    """Создает директорию, если её не существует."""
    def wrapper() -> Path:
        dir_path = func()
        if dir_path:
            dir_path.mkdir(parents=True, exist_ok=True)
        return dir_path
    return wrapper


def get_project_root() -> Path:
    """Возвращает абсолютный путь к проекту."""
    return Path.cwd().resolve()


def get_dataset_path() -> Path:
    """Возвращает путь к датасету."""
    path = get_project_root() / "dataset"
    if not path.exists():
        raise FileNotFoundError("Датасет должен быть в сурсах!")
    return path
    
def get_dataset_data_path() -> Path:
    """Возвращает путь к данным датасета."""
    return get_dataset_path() / 'train'

def get_label_map_path() -> Path:
    """Возвращает путь к файлу с классами и номерами."""
    return get_dataset_path() / 'label_map.csv'

def get_dataset_labels_path() -> Path:
    """Возвращает путь к разметке данных датасета."""
    return get_dataset_path() / 'train.csv'

def get_train_labels_path() -> Path:
    """Возвращает путь к разметке обучающей выборки."""
    return get_dataset_path() / 'train_train.csv'

def get_val_labels_path() -> Path:
    """Возвращаеть путь к разметке валидационной выборки."""
    return get_dataset_path() / 'train_val.csv'

def get_submit_data_path() -> Path:
    """Возвращаеть путь к тестовым данным."""
    return get_dataset_path() / 'test'


@fixdir
def get_weights_path() -> Path:
    """Возвращаеть путь к весам моделей."""
    return get_project_root() / 'weights'