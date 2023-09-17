import os
import argparse
import markdown
import shutil

def convert_to_html(markdown_text):
    # Split text into paragraphs based on two consecutive newline characters
    paragraphs = markdown_text.split("\n\n")
    
    # Wrap each paragraph in <p>...</p> tags
    paragraphs = ["<p>{}</p>".format(paragraph.strip()) for paragraph in paragraphs]
    
    # Combine paragraphs into HTML content
    html_content = "\n".join(paragraphs)
    
    return html_content

def process_file(input_file, output_folder):
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
        file.write(html_content)

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='TIL Tool - Convert Markdown to HTML')
    parser.add_argument('input', help='Input .txt file or folder of .txt files')
    parser.add_argument('-o', '--output', default='til', help='Output directory for HTML files')
    args = parser.parse_args()

    # Remove existing 'til' folder if it exists
    if os.path.exists(args.output):
        shutil.rmtree(args.output)
    
    # Create a new 'til' folder
    os.makedirs(args.output)

    # Process the input (file or folder)
    if os.path.isfile(args.input):
        process_file(args.input, args.output)
    elif os.path.isdir(args.input):
        # Process all .txt files in the input folder
        for filename in os.listdir(args.input):
            if filename.endswith('.txt'):
                input_file = os.path.join(args.input, filename)
                process_file(input_file, args.output)

if __name__ == '__main__':
    main()
