from .converterBase import Converter

class JpegConverter(Converter):
    def __init__(self, format):
        super().__init__(format)
        
    def convert(self, input_format):
        print(f"Converting from {input_format} to JPEG.")
        
