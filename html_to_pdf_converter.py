import pdfkit

# Path to HTML file
html_file = 'input.html'

# Path to output PDF file
pdf_file = 'output.pdf'

# Options for PDF generation (optional)
options = {
    'page-size': 'A4',
    'margin-top': '0.75in',
    'margin-right': '0.75in',
    'margin-bottom': '0.75in',
    'margin-left': '0.75in',
}

# Convert HTML to PDF
pdfkit.from_file(html_file, pdf_file, options=options)
