import requests
from bs4 import BeautifulSoup  # type: ignore
import pandas as pd
import re
import unicodedata
import mysql.connector  # type: ignore

def getConn():
    """Établit la connexion à la base de données et la retourne."""
    return mysql.connector.connect(
        host='mysql',
        user='root',
        password='root',
        database='cours_data',
        port=3306
    )

def getDataFromDb(table):
    """Récupère les données de la table spécifiée."""
    conn = getConn()
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {table}")
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return data

if __name__ == '__main__':
    try:
        links = getDataFromDb('links')
    except Exception as e:
        print(f"Erreur lors de la récupération des données de la DB : {e}")

    baseUrl = "https://www.numbeo.com/pollution/"
    col0, col1, col2, col3 = [], [], [], []

    conn = getConn()
    cursor = conn.cursor()

    for index, link in enumerate(links, start=1):
        print(link[1], '(', index, 'pays sur', len(links), ')')
        country = link[1]

        response = requests.get(baseUrl + link[2])
        soup = BeautifulSoup(response.content, 'html.parser')

        table = soup.select_one('table.data_wide_table')
        if table is None:
            print(f"Aucune table trouvée pour {country}")
            continue

        for tr in table.select('tr'):
            if tr.select('td'):
                td_desc = tr.select_one('td').text.strip()
                value_text = tr.select_one('td.indexValueTd').text.strip() if tr.select_one('td.indexValueTd') else "N/A"

                match = re.match(r"([\d,.]+)\s*(.*)", value_text)

                if match:
                    value = float(match.group(1).replace(',', '.'))
                    unit = match.group(2).strip() if match.group(2) else "N/A"
                else:
                    value = "N/A"
                    unit = "N/A"


                col0.append(country)
                col1.append(td_desc)
                col2.append(value)
                col3.append(unit)

    result = {
        "country": col0,
        "description": col1,
        "value": col2,
        "unit": col3
    }

    df = pd.DataFrame(result)

    for index, row in df.iterrows():
        sql = "INSERT INTO data_pollution (country, description, value, unit) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (row['country'], row['description'], row['value'], row['unit']))

    conn.commit()
    cursor.close()
    conn.close()
    print("Données insérées avec succès !")
