# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 20:24:51 2020

@author: alber
"""
from selenium import webdriver
import pandas as pd
from bs4 import BeautifulSoup
import re


max_num_pages = 2

driver = webdriver.Chrome('C:/Users/porteros/Anaconda3/Lib/site-packages/selenium/webdriver/chrome/chromedriver.exe')
driver.get("https://www.amazon.es/")

nextPage = driver.find_element_by_link_text('Los Más Vendidos')
nextPage.click()
nextPage = driver.find_element_by_link_text('Ver más Los más vendidos en CDs y vinilos')
nextPage.click()



# Initialize dataframe
df = pd.DataFrame([])    
# creas listas que irás relenando con datos
numero = []
Tipo = []
Grupo = []
Disco = []
Precio = []
rating = []
imagen = []
numReview = []
for i in range(1,(max_num_pages+1)):
               
        # number of page your are exploring
        print(i)
        
        # sometimes website takes long time to reload and you scrape the old page
        # Check that the number of the page is different from the page you have previously analyze    
        old_page = True
        while old_page:
            try:
                if(int(driver.find_element_by_class_name("a-selected").text) == i):
                    old_page = False
            except:
                pass

        # scrape info and save 
        html_txt = driver.page_source
        
        soup = BeautifulSoup(html_txt,"lxml") 
            

            
        # Parseas el código html extrayendo la información de interés
        for sec in soup.find_all(class_="zg-item-immersion"):
                
            # restaurant numero
            numer = sec.find(class_="zg-badge-text").get_text(strip=True) # extraccion
            numer = re.findall('\d*\,?\d+',numer)[0].replace(',','.')
            numero.append(numer)
            
            # rating
            if sec.find(class_="a-icon-alt") is not None:
                rat = sec.find(class_="a-icon-alt").get_text(strip=True) # extraccion
                rat = re.findall('\d*\,?\d+',rat)[0].replace(',','.') #manipulation to get the number
            else:
                rat = 0
            rating.append(rat)
            
            # number or reviews
            if sec.find(class_="a-size-small a-link-normal") is not None:
                reviews = sec.find(class_="a-size-small a-link-normal").get_text(strip=True).replace('.',',') # extraccion
            else:
                reviews = 0
            numReview.append(reviews)
            
            # Grupo
            if sec.find(class_="a-size-small a-color-base") is not None:
                Grup = sec.find(class_="a-size-small a-color-base").get_text(strip=True)  
            else:
                Grup = "Unknown"
            Grupo.append(Grup)
            
            # Grupo
            if sec.find(class_="a-size-small a-color-secondary") is not None:
                Tip = sec.find(class_="a-size-small a-color-secondary").get_text(strip=True)  
            else:
                Tip = "Unknown"
            Tipo.append(Tip)
            # Disco
            if sec.find(class_="p13n-sc-truncated") is not None:
                Disc = sec.find(class_="p13n-sc-truncated").get_text(strip=True)  
            else:
                Disc = "Unknown"
            Disco.append(Disc)        
            # Precio
            if sec.find(class_="p13n-sc-price") is not None:
                Preci = sec.find(class_="p13n-sc-price").get_text(strip=True)
                Preci = re.findall('\d*\,?\d+',Preci)[0].replace(',','.')
            else:
                Preci = "No disponible"
            Precio.append(Preci)     
           
            
            
            
            df = pd.DataFrame({'Disc':Disco,"Puntuacio":rating,
                               "Numero_Reviews":numReview, "Preu_Euro":Precio,
                              'Format':Tipo, "Grup":Grupo, "Top":numero, "Imagen":imagen},          
                    columns = ["Top","Disc","Grup","Puntuacio","Numero_Reviews","Format","Preu_Euro"])
        # go to the bottom of the webpage (to avoid a new popup box hide the button)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
       
        # Check the page is the last one
        if not driver.find_elements_by_class_name('a-last'):
            break
        
         # click next page
        nextPage = driver.find_element_by_class_name('a-normal')
        nextPage.click()
        
    
   
df = df.reset_index(drop=True)
df.to_csv('RawData.csv') 
driver.close()
