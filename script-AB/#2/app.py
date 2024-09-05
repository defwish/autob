from flask import Flask, request, render_template, redirect, url_for, send_from_directory
import requests
from bs4 import BeautifulSoup
import openpyxl
import os

app = Flask(__name__)

# inlocuieste cookies , headers , params cu cele din browserul propriu dupa login + search pe site 
def scrape_data(product_code):
    cookies = {
    'cookies aici',
}

    headers = {
    'headers aici',
}

    params = {
    'CSPToken': 'pune csp token aici',
    'Preis': '',
    'Farben': '',
    'Material': '',
    'Kategorie': '',
    'suche': 'F 026 400 068',
}
    search_url = f"https://online.autobrand.ro/csp/berta/portal/ArtSuche.csp?CSPToken={params['CSPToken']}&Preis=&Farben=&Material=&Kategorie=&suche={product_code}"

    response = requests.get(search_url, cookies=cookies, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    product_table = soup.find("table", class_="sortiertabelle itemlist tabelle-anwahl display stripe")

    
    file_path = f"product_data_{product_code.replace(' ', '_')}.xlsx"

    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.append(["Denumire", "Pret", "Disponibilitate", "Producator"])

    if product_table:
        for row in product_table.find_all('tr')[1:]:
            product_code_cell = row.find("td", class_="itemlist-col-ATNR")
            if product_code_cell and product_code in product_code_cell.text.strip():
                product_name = row.find("td", class_="itemlist-col-BEZ").text.strip()
                price = row.find("td", class_="itemlist-col-VKEINZ").text.strip()
                availability_cell = row.find("td", class_="itemlist-col-BESTANDVGST")
                availability_text = ""
                if availability_cell:
                    availability_link = availability_cell.find("a", title=True)
                    if availability_link:
                        availability_text = availability_link["title"].strip()
                manufacturer = row.find("td", class_="itemlist-col-HERSTELLBEZ").text.strip()

                sheet.append([product_name, price, availability_text, manufacturer])

    workbook.save(file_path)
    return file_path

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        product_code = request.form['product_code']
        file_path = scrape_data(product_code)
        return redirect(url_for('download_file', filename=os.path.basename(file_path)))
    return render_template('index.html')

@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory('.', filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
