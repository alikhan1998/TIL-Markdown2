# TIL-Markdown2

# TIL Converter - Convert Markdown to HTML
TIL Converter is a command-line tool for converting "Today I Learned" (TIL) posts written in Markdown to HTML.

## Installation 
To use TIL Converter, you need to have Python and the required libraries installed. You can install the necessary libraries using pip:

```bash
pip install markdown
pip install tomlkit

## Usage
To convert a Markdown file to HTML, run the following command:
python til_converter.py input.txt

Command-Line Options
-o, --output: Specify the output directory (default is "til").
-s, --stylesheet: Use a custom CSS stylesheet.
-c, --config: Use a config file to specify command-line options.
...

## Examples
Example 1: Convert a Single File
To convert a single Markdown file to HTML, run:
python til_converter.py post.txt

## Example 2: Convert All Files in a Folder
To convert all Markdown files in a folder, provide the folder path:
python til_converter.py /path/to/folder

## Example 3: Convert a Single File Using Options Specified in a Config File

# Option 1: use command line arguments:
python til_converter.py examples/sample.txt --output "./build" 
--stylesheet "https://cdn.jsdelivr.net/npm/water.css@2/out/water.css"

# Option 2: use a config file
python til_converter.py examples/sample.txt -c examples/config.toml
