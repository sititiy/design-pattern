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

        converter_class = self.image_converters.get(format.lower())
        

        return converter_class(format)


