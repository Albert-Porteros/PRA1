# PRA1
CDs i Vinils més venuts a través d’Amazon.

Aquest data set es tracta d’un extracte de la pagina web d’Amazon, on a la secció de més venuts, anem a cd’s i vinils i extreiem la informació principal d’aquests, tals com quin número del ranking ocupen, nom del disc, del grup, preu i puntuacions dels usuaris.

El data set creat a dia 13/04/2020 consta de les següents columnes/atributs sobre els cd i vinils més venuts a Amazon: 
-	Top: Indica en quina posició es troba dins del top 100 de més venuts a través d’amazon.
-	Disc: Indica el nom del disc en qüestió.
-	Grup: Indica el nom del creador/grup del disc en qüestió.
-	Puntuació: Indica la valoració que els usuaris d’Amazon li han donat al disc. En cas de no tenir ninguna valoració se li assigna un 0.
-	Numero_Reviews: Indica el número de reviews que ha rebut el disc en qüestió a la plataforma d’Amazon.
-	Preu_Euro: Indica el preu en Euros al qual s’està venent el cd/vinil. En cas de no tenir preu li assignarem un “No disponible”.
Per tal de recollir aquestes dades s’ha utilitzat una tècnica de web scrapping convinat amb web crawling per tal de navegar per la pàgina web d’Amazon. S’han anat llegint els productes que estaven a la secció de més venuts, sota la subsecció CDs y vinilos.
