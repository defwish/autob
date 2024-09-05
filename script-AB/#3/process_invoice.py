import pdfplumber
import pandas as pd
import re

pdf_path = r"C:\Users\Paula\Desktop\script-AB\#3\invoice.pdf"

def extract_data_from_pdf(pdf_path):
    data = []

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            lines = text.split("\n")
            for line in lines:
               
                match = re.search(r'(\d+)\s+(.+?)\s+(\d+\.\d{4})\s+RON\s+(\d+\.\d{2}|\d+)\s', line)

                if match:
                    cod = match.group(1) 
                    nume_articol = match.group(2)  
                    pret_unitar = match.group(3)  
                    cantitate_facturata = match.group(4) 
                    data.append([cod, nume_articol, pret_unitar, cantitate_facturata])

    df = pd.DataFrame(data, columns=['Cod', 'Nume articol', 'Pret Unitar', 'Cantitate facturata'])

    df.to_csv('Articole_Facturate.csv', index=False)
    print("Data extracted and saved to Articole_Facturate.csv")

extract_data_from_pdf(pdf_path)
