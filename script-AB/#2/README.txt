#2. Web Scrapping 

INFORMATII UTILE : 

1. scraper.py :

   script care odata rulat:

      -extrage de pe website [ Denumirea , Pretul , Disponibilitate , Producator ] pentru produsul cu codul F 026 400 068 . 

      -exporta informatiile extrase intr-un fisier xlsx ( excel ) ce este salvat in folderul de unde ruleaza scriptul.

      ( Vezi scrappedProductInfoResultsExcel.png sau product_data_F_026_400_068.xlsx pentru rezultat )


2. app.py : 
     
      ( Vezi webApp.png pentru a vedea cum arata aplicatia in cazul in care nu se doreste rularea ) 

   aplicatie web construita cu ajutorul Flask , bazata pe scraper.py care :

      - extrage de pe website [ Denumirea , Pretul , Disponibilitate , Producator ] pentru ORICE produs ( pe baza codului de produs care este inserat de user in browser )

      - exporta informatiile extrase intr-un fisier xlsx ( excel ) , numit dupa codul produsului , ce poate fii downloadat din browser de userul ce face cautarea/extragerea .  
      
      ( Vezi scrappedProductInfoResultsExcel.png sau product_data_F_026_400_068.xlsx pentru rezultat )

3. requirements.txt : 

    
   importuri necesare pentru a putea rula . 



Extra: Aplicatia si Scriptul se ocupa de "login" prin cookies .

ATENTIE! : din motive de securitate am sters datele folosite , pentru a rula aplicatia pe plan local :
      
      - trebuie updatate cookies , headers si params cu cele din browser ( copy bash curl -> convert in py code )
      
      - am pus comentarii prin cod-ul app.py se poate vedea usor ce trebuie inlocuit .