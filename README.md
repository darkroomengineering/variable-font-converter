# Generate Static Fonts from Variable Font

This script allows you to generate static font instances from a variable font using the FontTools library. This can be useful for creating multiple static versions of a font with different properties (e.g., weight, slant, optical size).

## Requirements

- Python 3.x
- FontTools library

You can install FontTools using pip:

```sh
pip install fonttools
```

## Usage

1. **Define the instances you want to generate**: 
   Modify the `instances` list to define the different static instances you want to create. Each instance is a dictionary with keys corresponding to the font variation axes (e.g., `wght`, `slnt`, `opts`) and values specifying the desired values for those axes.

2. **Set the variable font path**: 
   Specify the path to your variable font file in the `variable_font_path` variable.

3. **Set the output folder**: 
   Specify the path to the folder where you want the generated static fonts to be saved in the `output_folder` variable.

4. **Run the script**: 
   Execute the script to generate the static fonts.

### Example

```python
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
```

### Parameters

- `variable_font_path`: The path to the variable font file.
- `output_folder`: The folder where the generated static fonts will be saved.
- `instances`: A list of dictionaries specifying the desired values for the font variation axes.

### Output

The script will generate and save static font files in the specified output folder. The file names will include the base name of the variable font and the values of the specified axes.

## License

This script is provided "as is" without warranty of any kind. Use it at your own risk.