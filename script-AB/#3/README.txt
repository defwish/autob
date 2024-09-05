#3. Prelucrare PDF

INFORMATII UTILE : 

1. process_invoice.py :

   script care odata rulat:
   
      - deschide documentul PDF ( invoice.pdf ) , il citeste si extrage textul de pe fiecare pagina a PDF-ului .

      - proceseaza fiecare linie si aplica o expresie pentru a gasii si extrage toate datele relevante ( cod , nume , pret , cantitate ) 

      - aduna si salveaza datele intr-o lista 

      - converteste lista intr-un data-frame si o exporta intr-un fisier CSV . 

    ( vezi procesareFactura.png sau Articole_Facturate.csv pentru rezultatul final )

1. filter_invoice.py :

   script care odata rulat:
   
      - deschide documentul PDF ( invoice.pdf ) , il citeste si extrage Nr. factura folosind regex . 

      - citeste documentul Comenzi.csv si filtreaza randurile unde numar_factura este acelasi cu cel din factura ( documentul PDF )

      - salveaza datele filtrate intr-un document nou numit Filtered_Comenzi.csv 

    ( contine linii de cod pentru debugging )

    ( vezi filtrareFactura.png sau Filtered_Comenzi.csv pentru rezultatul final )

3. requirements.txt : 

    
   importuri necesare pentru a putea rula .   


