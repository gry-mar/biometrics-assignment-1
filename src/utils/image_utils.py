from enum import Enum
from PIL import Image
import cv2
import numpy as np

class ScaleType(Enum):
    LINEAR = 0
    CONSTANT = 1
    QUADRATIC = 2


def change_luminance(image: Image, scale_type: ScaleType, factor: float = 1) -> Image:
    """
    Change the luminance of an image by scaling the Y channel values.
    
    Parameters:
        image (Image): Input image.
        acale_type (ScaleType): Type of scaling that will be used.
        factor (float): Scaling factor for luminance adjustment.
                        Can be a constant value or 1/n for scaling.
    
    Returns:s
        Image: Image with adjusted luminance.
    """

    assert scale_type != 0
    yuv_image = cv2.cvtColor(image, cv2.COLOR_BGR2YUV)
    y_channel = yuv_image[:,:,0]
    if scale_type == ScaleType.CONSTANT:
        y_channel_scaled = np.clip(y_channel + factor, 0, 255).astype(np.uint8)
    elif scale_type == ScaleType.LINEAR:
        y_channel_scaled = np.clip(y_channel * factor, 0, 255).astype(np.uint8)
    elif scale_type == ScaleType.QUADRATIC:
        y_channel_scaled = np.clip(y_channel ** 2, 0, 255).astype(np.uint8)

    yuv_image[:,:,0] = y_channel_scaled
    result_image = cv2.cvtColor(yuv_image, cv2.COLOR_YUV2BGR)

    return result_image