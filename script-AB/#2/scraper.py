import requests
from bs4 import BeautifulSoup
import openpyxl

#inlocuieste cookies , headers , params cu cele din browserul propriu dupa login + search 

cookies = {
    'cookies aici',
}

headers = {
    'headers aici',
}

params = {
    'CSPToken': 'csp token aici',
}



product_code = "F 026 400 068"
search_url = f"https://online.autobrand.ro/csp/berta/portal/ArtSuche.csp?CSPToken={params['CSPToken']}&Preis=&Farben=&Material=&Kategorie=&suche={product_code}"


response = requests.get(search_url, cookies=cookies, headers=headers)


soup = BeautifulSoup(response.content, 'html.parser')


product_table = soup.find("table", class_="sortiertabelle itemlist tabelle-anwahl display stripe")

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

            workbook.save("product_data.xlsx")

print("Data exported to product_data.xlsx")
             
