from .jpegConverter import JpegConverter
from .pngConverter import PngConverter
from .gifConverter import GifConverter 

class ConvertFactory:
    def create_converter(self, format):
        self.image_converters = {
            "jpeg" : JpegConverter,
            "png" : PngConverter,
            "gif" : GifConverter
        }

        image_converter = self.image_converters.get(format.lower())
        return image_converter

