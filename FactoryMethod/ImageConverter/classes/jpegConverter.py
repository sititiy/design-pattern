from .converterBase import Converter

class JpegConverter(Converter):
    def convert(self, input_format):
        self.input_format = input_format
        print(f"Converting from {self.input_format} to JPEG.")
        
