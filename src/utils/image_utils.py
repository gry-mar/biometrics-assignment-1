from enum import Enum
from PIL import Image
import cv2
import numpy as np
import math

class ScaleType(Enum):
    LINEAR = 0
    CONSTANT = 1
    QUADRATIC = 2


def change_luminance(image: Image, scale_type: ScaleType, factor: float = 1, clip: bool = False) -> Image:
    """
    Change the luminance of an image by scaling the Y channel values.
    
    Parameters:
        image (Image): Input image read as RGB
        scale_type (ScaleType): Type of scaling that will be used.
        factor (float): Scaling factor for luminance adjustment.
                        Can be a constant value or 1/n for scaling.
        clip (bool): to use np.clip should be True, to use linear scaling False
    
    Returns:
        Image: bgr image with adjusted luminance.
    """

    yuv_image = cv2.cvtColor(image, cv2.COLOR_RGB2YUV)
    y_channel = yuv_image[:,:,0]
    if scale_type == ScaleType.CONSTANT:
        if clip:
            y_channel_scaled = np.clip(y_channel.astype(np.float32) + factor, 0, 255)
        else: 
            y_channel_scaled = (y_channel.astype(np.float32)+ factor) / (np.max(y_channel.astype(np.float32) + factor)) * 255

    elif scale_type == ScaleType.LINEAR:
        y_channel_scaled = y_channel * factor
        if clip:
            y_channel_scaled = np.clip(y_channel_scaled.astype(np.float32), 0, 255)
        else:
            y_channel_scaled = (y_channel_scaled - np.min(y_channel_scaled)) / (np.max(y_channel_scaled) - np.min(y_channel_scaled)) * 255

    elif scale_type == ScaleType.QUADRATIC:
        if clip:
            y_channel_scaled = np.clip(y_channel.astype(np.float32) ** 2, 0, 255)
        else: 
            y_channel_scaled = (y_channel.astype(np.float32) ** 2) / (np.max(y_channel.astype(np.float32) ** 2)) * 255

    yuv_image[:,:,0] = y_channel_scaled.astype(np.uint8)
    result_image = cv2.cvtColor(yuv_image, cv2.COLOR_YUV2RGB)
    return result_image


def extend_image_to_shape(image: Image, new_width, new_height, fill_color=(0, 0, 0)):
    """
    Extends or crops an image to the specified dimensions.

    Parameters:
        image (Image): Path to the input image.
        new_width (int): The target width of the image.
        new_height (int): The target height of the image.
        fill_color: The color used to fill the extended areas (default is black).

    Returns:
        new_image (Image): A new image with the specified dimensions.
    """

    old_height, old_width = image.shape[:2]

    new_image = np.full((new_height, new_width, 3), fill_color, dtype=np.uint8)

    x_offset = (new_width - old_width) // 2
    y_offset = (new_height - old_height) // 2

    x_offset = max(0, x_offset)
    y_offset = max(0, y_offset)

    copy_width = min(old_width, new_width)
    copy_height = min(old_height, new_height)

    new_image[y_offset:y_offset+copy_height, x_offset:x_offset+copy_width] = image[0:copy_height, 0:copy_width]

    return new_image


def add_gaussian_noise(image: Image, mean: float=0, std: float=25) -> Image:
    """Adds Gaussian noise to image
    
    Parameters:
        image: Image
        mean: float
        std: float
    
    Returns:
        noisy_image: Image"""
    noise = np.random.normal(mean, std, image.shape).astype(np.uint8)
    noisy_image = cv2.add(image, noise)
    return noisy_image


def calculate_psnr(original_image, noisy_image) -> float:
    """Calculate PSNR between original and noisy images.
    
    Parameters:
        original_image: Image
        noisy_image: Image
    
    Returns:
        psnr: float
    """
    mse = np.mean((original_image - noisy_image) ** 2)
    if mse == 0:
        return float('inf')
    max_pixel = 255.0
    psnr = 20 * math.log10(max_pixel / math.sqrt(mse))
    return psnr