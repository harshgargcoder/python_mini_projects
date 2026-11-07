import PyPDF2
import os

def extract_pdf_text(file_path):
    abs_path = os.path.abspath(file_path)
    print(f"Looking for PDF at: {abs_path}")
    
    if not os.path.exists(abs_path):
        print(f"Error: File not found at {abs_path}")
        print("Current working directory:", os.getcwd())
        return None

    text = ""
    try:
        with open(abs_path, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            print(f"Found {len(pdf_reader.pages)} pages in the PDF")
            
            for page in pdf_reader.pages:
                text += page.extract_text()
                
        return text
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None

pdf_paths = [
    "UNIT-I-PPT-1-MCA-20-14.pdf",  # Relative path
    r"D:/Languages/GitHub/Python_mini_project/pdf_extraction/UNIT-I-PPT-1-MCA-20-14.pdf"  # Absolute path
]

for path in pdf_paths:
    print(f"\nTrying path: {path}")
    extracted_text = extract_pdf_text(path)
    if extracted_text:
        print("Extraction successful!")
        print("First 100 characters:")
        print(extracted_text[:100])
        break
else:
    print("\nFailed to find PDF. Please verify:")
    print("1. The file exists in the correct folder")
    print("2. The filename is exactly correct (check capitalization and hyphens)")
    print("3. You're running the script from the right directory")