import pdfkit
from bs4 import BeautifulSoup

# Path to your HTML file and output PDF file
html_file = 'cucumber-html-report (3).html'
output_pdf = 'output.pdf'

# Read and parse the HTML file
with open(html_file, 'r', encoding='utf-8') as file:
    soup = BeautifulSoup(file, 'html.parser')

# Extract text content and clean up extra whitespace
text_content = soup.get_text(separator=' ', strip=True)

# Save text content to a temporary HTML file with CSS to reduce spacing
temp_html_file = 'temp.html'
html_template = f"""
<html>
<head>
    <style>
        body {{
            font-family: Arial, sans-serif;
            line-height: 1.2;
            margin: 20px;
            white-space: pre-wrap;
            word-wrap: break-word;
        }}
        p {{
            margin: 0;
            padding: 0;
        }}
    </style>
</head>
<body><pre>{text_content}</pre></body>
</html>
"""
with open(temp_html_file, 'w', encoding='utf-8') as file:
    file.write(html_template)

# Path to wkhtmltopdf executable
path_to_wkhtmltopdf = r'C:\Program Files\wkhtmltox\bin\wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf=path_to_wkhtmltopdf)

# Convert the temporary HTML file to PDF
pdfkit.from_file(temp_html_file, output_pdf, configuration=config)

print("Conversion complete. The PDF file is saved as:", output_pdf)
