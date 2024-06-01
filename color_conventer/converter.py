import xml.etree.ElementTree as ET
import pathlib
import os

def change_svg_path_color(input_svg, output_svg, old_color, new_color):
    # Парсинг SVG файла
    tree = ET.parse(input_svg)
    root = tree.getroot()
    
    # Определяем пространство имен SVG
    ns = {'svg': 'http://www.w3.org/2000/svg'}
    
    # Проходим через все элементы path и меняем цвет
    for path in root.findall('.//svg:path', ns):
        style = path.get('style')
        if style and f'fill:{old_color}' in style:
            new_style = style.replace(f'fill:{old_color}', f'fill:{new_color}')
            path.set('style', new_style)
        elif path.get('fill') == old_color:
            path.set('fill', new_color)
    
    # Сохраняем измененный SVG в новый файл
    tree.write(output_svg)

def change_stroke_color(svg_file, original_color, new_color, new_svg_file):
    tree = ET.parse(svg_file)
    root = tree.getroot()
    
    # Find all rectangles in the SVG file
    for rect in root.iter('{http://www.w3.org/2000/svg}rect'):
        # Check if the rectangle has the specified stroke color
        if rect.get('stroke') == original_color:
            rect.set('stroke', new_color)
    
    tree.write(new_svg_file)

# Использование функции
input_one = './legend_bottom.svg'
old_color = '#FCFAF3'
new_color = '#000000'
result_one = f'{pathlib.Path(__file__).parent.resolve()}\\output.svg'

change_stroke_color(input_one, old_color, new_color, result_one)

input_one = f'{pathlib.Path(__file__).parent.resolve()}\\output.svg'
old_color = 'white'
new_color = '#000000'
result_one = f'{pathlib.Path(__file__).parent.resolve()}\\output.svg'

change_stroke_color(input_one, old_color, new_color, result_one)

input_one = f'{pathlib.Path(__file__).parent.resolve()}\\output.svg'
result_one = f'{pathlib.Path(__file__).parent.resolve()}\\output.svg'
old_color = '#56544D'
new_color = '#FFFFFF'

change_svg_path_color(input_one, result_one, old_color, new_color)

input_one = f'{pathlib.Path(__file__).parent.resolve()}\\output.svg'
result_one = './legend_bottom_dark.svg'
old_color = '#6D6B65'
new_color = '#FFFFFF'

change_svg_path_color(input_one, result_one, old_color, new_color)

os.remove(f"{pathlib.Path(__file__).parent.resolve()}\\output.svg")