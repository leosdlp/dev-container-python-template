import pandas as pd
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

def clean_data(table_name, clean_table_name):
    """Nettoie les données d'une table et les insère dans une nouvelle table."""
    conn = getConn()
    cursor = conn.cursor()

    query = f"SELECT * FROM {table_name}"
    df = pd.read_sql(query, conn)

    df = df.dropna()
    df = df.drop_duplicates()
    df = df[~df.applymap(lambda x: '?' in str(x)).any(axis=1)]
    df = df[pd.to_numeric(df['value'], errors='coerce').notna()]

    cursor.execute(f"DELETE FROM {clean_table_name}")
    conn.commit()

    for _, row in df.iterrows():
        sql = f"INSERT INTO {clean_table_name} VALUES ({', '.join(['%s'] * len(row))})"
        cursor.execute(sql, tuple(row))

    conn.commit()
    cursor.close()
    conn.close()
    print(f"Données nettoyées et insérées dans {clean_table_name} !")

if __name__ == '__main__':
    clean_data("data_pollution", "clean_data_pollution")
    clean_data("data_crime", "clean_data_crime")
    clean_data("data_cost_of_life", "clean_data_cost_of_life")
