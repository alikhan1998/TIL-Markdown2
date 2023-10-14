import os
import argparse
import sys
import markdown2
from tomlkit.toml_file import TOMLFile

def convert_to_html(markdown_text):
    # Convert Markdown to HTML
    return markdown2.markdown(markdown_text)

def process_file(input_file, output_folder, stylesheet_url=None):
    # Read the content of the input file
    with open(input_file, 'r') as file:
        markdown_text = file.read()

    # Convert Markdown to HTML
    html_content = convert_to_html(markdown_text)

    # Create the output file path
    input_filename = os.path.basename(input_file)
    output_file = os.path.join(output_folder, input_filename.replace('.txt', '.html'))

    # Write the HTML content to the output file
    with open(output_file, 'w') as file:
        if stylesheet_url:
            # Include the custom stylesheet URL in the HTML header
            file.write(f'<!DOCTYPE html>\n<html>\n<head>\n'
                       f'<link rel="stylesheet" href="{stylesheet_url}">\n'
                       f'<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">\n'
                       f'<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>\n'
                       f'<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>\n'
                       f'<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>\n'
                       f'</head>\n<body>\n')
        else:
            file.write('<!DOCTYPE html>\n<html>\n<head>\n</head>\n<body>\n')

        # Write the HTML content
        file.write(html_content)

        # Close the HTML tags
        file.write('\n</body>\n</html>')

def get_config_file_data(config_file):
    """
    Reads a config file and returns the data in a TOMLDocument object.
    A TOMLDocument object can be used the same as a dictionary object.
 
    Args:
        config_file (String): the path of the config file (.toml file)
 
    Returns:
        TOMLDocument: the config file contents if read was successful
        None: if read was unsuccessful (invalid config path, invalid config file contents)
    """
    try:
        return TOMLFile(config_file).read()
    except:
        return None

def main():
    output_path = None
    stylesheet_url = None

    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='TIL Tool - Convert Markdown to HTML')
    parser.add_argument('input', help='Input .txt file')
    parser.add_argument('-o', '--output', default='til', help='Output directory for HTML files')
    parser.add_argument('-s', '--stylesheet', help='Custom stylesheet URL')
    parser.add_argument('-c', '--config', help='Use config file instead of command-line args')
    args = parser.parse_args()

    # Check if user has opted to use a config file
    if args.config:
        # If config file does not exist, exit with error message
        if not os.path.isfile(args.config):
            print(f"Error: Config file {args.config} does not exist\n")
            sys.exit()

        # Extract data from config file into a dictionary-like object
        config_args = get_config_file_data(args.config)

        # If data extraction from config file failed, exit with error message
        if not config_args:
            print(f"Error: Unable to parse config file {args.config} as TOML\n")
            sys.exit()
        
        # Get output path from config file
        if "output" in config_args:
            output_path = config_args["output"]

        # Get stylesheet url from config file
        if "stylesheet" in config_args:
            stylesheet_url = config_args["stylesheet"]
    else:
        # Get output path from command-line args
        output_path = args.output

        # Get stylesheet url from command-line args
        stylesheet_url = args.stylesheet 

    # Create the output folder if it doesn't exist
    os.makedirs(output_path, exist_ok=True)

    # Process the input file
    process_file(args.input, output_path, stylesheet_url)

if __name__ == '__main__':
    main()
