from bs4 import BeautifulSoup

# Path to your HTML file and output text file
html_file = 'cucumber-html-report (3).html'
output_text_file = 'output.txt'

# Read and parse the HTML file
with open(html_file, 'r', encoding='utf-8') as file:
    soup = BeautifulSoup(file, 'html.parser')

# Extract text content and clean up extra whitespace
text_content = soup.get_text(separator=' ', strip=True)

# Save the cleaned text content to a text file
with open(output_text_file, 'w', encoding='utf-8') as file:
    file.write(text_content)

print("Extraction complete. The text file is saved as:", output_text_file)
