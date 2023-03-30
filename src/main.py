import re
import os
import sys
from googletrans import Translator

# Get the project path, language code, and output file path from the command line arguments
if len(sys.argv) != 4:
    print("Usage: python script.py <project_path> <language_code> <output_file_path>")
    sys.exit(1)
project_path = sys.argv[1]
language_code = sys.argv[2]
output_file_path = sys.argv[3]

# Regular expression pattern to match NSLocalizedString instances
pattern = re.compile(r'NSLocalizedString\("([^"]+)"')

translator = Translator()

# Set to store processed keys
processed_keys = set()

# List to store all the NSLocalizedString keys and values
keys_values = []

# Walk through the project directory and find all .m and .swift files
for root, dirs, files in os.walk(project_path):
    for file in files:
        print(f"Processing file: {file}")
        if file.endswith(".m") or file.endswith(".swift"):
            file_path = os.path.join(root, file)
            with open(file_path, "r") as f:
                contents = f.read()
                # Search for all NSLocalizedString instances in the file
                matches = pattern.findall(contents)
                for match in matches:
                    # Extract the key from the NSLocalizedString instance
                    key = match
                    if key in processed_keys:
                        continue
                    # Translate the key to the specified language
                    try:
                        translation = translator.translate(key, src='en', dest=language_code).text
                        # Replace double quotes with single quotes
                        translation = translation.replace('"', "'").capitalize()
                    except Exception as e:
                        print(f"Error translating key '{key}': {e}")
                        continue
                    keys_values.append((key, translation))
                    processed_keys.add(key)

# Write the keys and values to the output text file
try:
    with open(output_file_path, "w") as f:
        for key, value in keys_values:
            f.write(f'"{key}"="{value}";\n\n')
except Exception as e:
    print(f"Error writing to file '{output_file_path}': {e}")
