import markdown2

def convert_md_to_html(md_file_path, output_file_path):
    # Read the content of the Markdown file
    with open(md_file_path, 'r', encoding='utf-8') as md_file:
        md_content = md_file.read()

    # Convert Markdown to HTML
    html_content = markdown2.markdown(md_content)

    # Write the HTML content to the output file
    with open(output_file_path, 'w', encoding='utf-8') as html_file:
        html_file.write(html_content)

# Example usage:
# Replace 'input.md' and 'output.html' with your input Markdown file and desired output HTML file paths
convert_md_to_html('pypi/README.md', 'output.html')
