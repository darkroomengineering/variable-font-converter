from fontTools.varLib import mutator
from fontTools.ttLib import TTFont
import os

def generate_static_fonts(variable_font_path, output_folder, instances):
    # Ensure the output directory exists
    os.makedirs(output_folder, exist_ok=True)
    
    # Load the variable font
    varfont = TTFont(variable_font_path)
    
    for instance in instances:
        # Generate a static instance
        static_font = mutator.instantiateVariableFont(varfont, instance)
        
        # Create the output file name based on the instance
        instance_name = '-'.join(f'{k}{v}' for k, v in instance.items())
        output_path = os.path.join(output_folder, f'{os.path.basename(variable_font_path).split(".")[0]}-{instance_name}.ttf')
        
        # Save the static font
        static_font.save(output_path)
        print(f'Saved: {output_path}')

# Define the instances you want to generate (e.g., different weights)
instances = [
    {"wght": 10, 'slnt': 4, 'opts': -10},
    {"wght": 12, 'slnt': 4, 'opts': -10},
    {"wght": 14, 'slnt': 4, 'opts': -10},
    {"wght": 16, 'slnt': 4, 'opts': -10},
    {"wght": 18, 'slnt': 4, 'opts': -10},
]

# Path to your variable font
variable_font_path = "path/to/your-variable/font.ttf"

# Output folder
output_folder = "path/to/output/folder"

# Generate static fonts
generate_static_fonts(variable_font_path, output_folder, instances)
