import gc
from PIL import Image
from torch import Tensor
from torchvision.transforms.v2 import Transform, Pad


class PadToSize(Transform):
    """
    Добавляет constant padding до целевого размера (H, W).

    Parameters:
        target_size: Целевой размер изображения
        fill: Значение для каналов в паддинг-пикселях
    """
    def __init__(self, target_size: tuple[int, int], fill: int = 0):
        super().__init__()
        self.target_h, self.target_w = target_size
        self.fill = fill

    def transform(self, inpt: Any, params: dict[str, Any]):
        img = inpt
        if isinstance(img, Tensor):
            h, w = img.shape[-2], img.shape[-1]
        elif isinstance(img, Image):
            w, h = img.size
        else:
            img_type = type(img)
            raise RuntimeError(f"Image has to be torch.Tensor or PIL.Image. Image's type is {img_type}")
        
        pad_h = self.target_h - h
        pad_w = self.target_w - w

        # Считаем отступы для центрирования изображения
        pad_top = pad_h // 2
        pad_bottom = pad_h - pad_top
        pad_left = pad_w // 2
        pad_right = pad_w - pad_left

        return Pad(
            padding=(pad_left, pad_top, pad_right, pad_bottom), 
            fill=self.fill, 
            padding_mode='constant'
        )(img)


def clear_memory(device: torch.DeviceType):
    """Очищает утекшую CUDA-память."""
    GB = 1024 * 1024 * 1024
    if device == 'cuda':
        cuda.empty_cache()
        gc.collect()
        cuda_alloc = cuda.memory_allocated() / GB
        cuda_reserve = cuda.memory_reserved() / GB
        print(f"CUDA allocated: {cuda_alloc:.2f} GB")
        print(f"CUDA reserved:  {cuda_reserve:.2f} GB")