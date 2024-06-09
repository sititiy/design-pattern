from classes.converterFactory import ConvertFactory

def convert_image(input_format, output_format):
    factory = ConvertFactory()
    converter = factory.create_converter(output_format)
    
    converter.convert(input_format)