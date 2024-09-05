import pdfplumber
import pandas as pd
import re


def extract_invoice_number_from_pdf(pdf_path):
    invoice_number = None
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            match = re.search(r'Nr\. factura (\d+)', text)
            if match:
                invoice_number = match.group(1)
                break
    return invoice_number


def filter_comenzi_by_invoice_number(invoice_number, comenzi_csv_path, output_csv_path):
   
    headers = ['numar_factura', 'numar_comanda', 'cod_articol', 'id_cantitate']
    
    try:
       
        comenzi = pd.read_csv(comenzi_csv_path, encoding='utf-8', delimiter=',', names=headers, header=None)
    except UnicodeDecodeError:
        comenzi = pd.read_csv(comenzi_csv_path, encoding='latin1', delimiter=',', names=headers, header=None)
    except pd.errors.ParserError:
        print("Error parsing the CSV file. Please check the file format and delimiters.")
        return

    
    print("First few rows of Comenzi.csv:")
    print(comenzi.head())

   
    print(f"Filtering with invoice number: {invoice_number}")

    
    comenzi['numar_factura'] = comenzi['numar_factura'].astype(str)
    filtered_comenzi = comenzi[comenzi['numar_factura'] == str(invoice_number)]

    
    print("Filtered data:")
    print(filtered_comenzi)

    
    filtered_comenzi.to_csv(output_csv_path, index=False)
    print(f"Filtered data has been saved to {output_csv_path}")

def main():
    pdf_path = r"C:\Users\Paula\Desktop\script-AB\#3\invoice.pdf"
    comenzi_csv_path = r"C:\Users\Paula\Desktop\script-AB\#3\Comenzi.csv"
    output_csv_path = r"C:\Users\Paula\Desktop\script-AB\#3\Filtered_Comenzi.csv"

  
    invoice_number = extract_invoice_number_from_pdf(pdf_path)
    
    if invoice_number:
        print(f"Extracted Invoice Number: {invoice_number}")
        
        filter_comenzi_by_invoice_number(invoice_number, comenzi_csv_path, output_csv_path)
    else:
        print("Invoice number not found in the PDF")

if __name__ == "__main__":
    main()
