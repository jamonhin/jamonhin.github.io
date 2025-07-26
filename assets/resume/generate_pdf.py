#!/usr/bin/env python3
"""
Script to convert HTML resume to PDF
Requires: pip install weasyprint
Usage: python3 generate_pdf.py
"""

try:
    from weasyprint import HTML, CSS
    import os
    
    def generate_pdf():
        # Get the directory of this script
        script_dir = os.path.dirname(os.path.abspath(__file__))
        
        # Define paths
        html_file = os.path.join(script_dir, 'james-montoya-resume.html')
        pdf_file = os.path.join(script_dir, 'james-montoya-resume.pdf')
        
        # Additional CSS for better PDF formatting
        pdf_css = CSS(string='''
            @page {
                size: Letter;
                margin: 0.5in;
            }
            body {
                font-size: 11px;
            }
            .resume-container {
                margin: 0;
                padding: 0;
            }
        ''')
        
        # Convert HTML to PDF
        HTML(filename=html_file).write_pdf(pdf_file, stylesheets=[pdf_css])
        print(f"PDF generated successfully: {pdf_file}")
        
    if __name__ == "__main__":
        generate_pdf()
        
except ImportError:
    print("WeasyPrint not installed. To generate PDF:")
    print("1. Install WeasyPrint: pip install weasyprint")
    print("2. Run: python3 generate_pdf.py")
    print("Alternative: Open james-montoya-resume.html in browser and print to PDF")
