import csv
import re
from marvel import Marvel
from keys import PUBLIC_KEY, PRIVATE_KEY

marvel = Marvel(PUBLIC_KEY=PUBLIC_KEY, PRIVATE_KEY=PRIVATE_KEY)
#llamamos al contenido de Marvel
characters = marvel.characters

my_char = characters.all(nameStartsWith="Thor")["data"]["results"]

# Se crea el archi CSV
with open('Comic_Info.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Titulo', 'Año', 'URL Cover']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for char in my_char:
        char_name = char["name"]
        print(char_name)

        for comic in char["comics"]["items"]:
            comic_title = comic["name"] #Nombre del titulo del comic

            #Como el nombre del comic y el anio aparecen juntos, se extrae el anio del titulo
            match = re.search(r'\((\d{4})\)', comic_title)
            publication_year = match.group(1) if match else "N/A"

            comic_cover_url = comic["resourceURI"]  # URL

            # Imprime en pantalla
            print(f"Titulo: {comic_title}")
            print(f"Año: {publication_year}")
            print(f"URL Cover: {comic_cover_url}")

            # Escribe en el archivo CSV
            writer.writerow({'Titulo': comic_title, 'Año': publication_year, 'URL Cover': comic_cover_url})

        print("---------------------")
