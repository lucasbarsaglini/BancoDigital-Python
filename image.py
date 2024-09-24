from PIL import Image, ImageFilter
import numpy as np

class ImageProcessor:
    def __init__(self, image_path):
        self.image = Image.open(image_path)

    def resize(self, width, height):
        resized_image = self.image.resize((width, height))
        return resized_image

    def rotate(self, degrees):
        rotated_image = self.image.rotate(degrees)
        return rotated_image

    def to_grayscale(self):
        grayscale_image = self.image.convert("L")
        return grayscale_image

    def apply_filter(self, filter_type):
        if filter_type == 'BLUR':
            filtered_image = self.image.filter(ImageFilter.BLUR)
        elif filter_type == 'CONTOUR':
            filtered_image = self.image.filter(ImageFilter.CONTOUR)
        else:
            raise ValueError("Filtro não suportado.")
        return filtered_image

    def save_image(self, output_path):
        self.image.save(output_path)
