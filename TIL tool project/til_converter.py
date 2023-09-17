import os
import argparse
import markdown

def convert_to_html(markdown_text):
    # Convert Markdown to HTML
    html_content = markdown.markdown(markdown_text)
    return html_content

def process_file(input_file, output_folder, custom_css=None):
    # Read the content of the input file
    with open(input_file, 'r') as file:
        markdown_text = file.read()

    # Convert Markdown to HTML
    html_content = convert_to_html(markdown_text)

    # Create the output file path
    input_filename = os.path.basename(input_file)
    output_file = os.path.join(output_folder, input_filename.replace('.txt', '.html'))

    # Create the HTML template with custom styles
    html_template = f'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{input_filename}</title>
        <link rel="stylesheet" href="{custom_css or 'default.css'}">
    </head>
    <body>
        {html_content}
    </body>
    </html>
    '''

    # Write the HTML content to the output file
    with open(output_file, 'w') as file:
        file.write(html_template)

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='TIL Tool - Convert Markdown to HTML')
    parser.add_argument('input', help='Input .txt file or folder of .txt files')
    parser.add_argument('-o', '--output', default='til', help='Output directory for HTML files')
    parser.add_argument('-s', '--stylesheet', help='Custom CSS stylesheet file')
    args = parser.parse_args()

    # Create the output folder if it doesn't exist
    os.makedirs(args.output, exist_ok=True)

    # Process the input (file or folder)
    if os.path.isfile(args.input):
        process_file(args.input, args.output, args.stylesheet)
    elif os.path.isdir(args.input):
        # Process all .txt files in the input folder
        for filename in os.listdir(args.input):
            if filename.endswith('.txt'):
                input_file = os.path.join(args.input, filename)
                process_file(input_file, args.output, args.stylesheet)

if __name__ == '__main__':
    main()
