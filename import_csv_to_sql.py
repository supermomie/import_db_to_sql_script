import time
import pandas as pd
import sqlalchemy
import pymysql

start = time.time()
# Configuration serveur
databaseServerIP      = "localhost" #OR 127.0.0.1
databaseUserName      = "root"
databaseUserPassword  = ""

# Nom de la base de donnee et nom de la table
DB_NAME    = 'Declarations'
TABLE_NAME = 'declaration_avantage'

# Chemin du ficher CSV
PATHFILE   = ''

# Nom du fichier
NAME       = ''

ENCODING = 'utf-8'

engine = sqlalchemy.create_engine('mysql+pymysql://'+databaseUserName+':@'+databaseServerIP+'/'+DB_NAME)


connectionInstance = pymysql.connect(host=databaseServerIP, user=databaseUserName, password=databaseUserPassword,charset="utf8mb4", cursorclass=pymysql.cursors.DictCursor)
cursorInsatnce = connectionInstance.cursor()
sqlStatement = "CREATE DATABASE "+DB_NAME
cursorInsatnce.execute(sqlStatement)

print("IMPORT DATABASE")
data = pd.read_csv(PATHFILE+'/'+NAME, encoding=ENCODING, sep=';', dtype='object')
columnsName = [col for col in data.columns]
ratings = pd.read_csv(PATHFILE+'/'+NAME, sep=';', encoding=ENCODING, usecols=columnsName, dtype='object')


ratings.to_sql(TABLE_NAME, con=engine, if_exists='append', index=False, chunksize=1)

print("IMPORT TERMINER")

end = time.time()
print("import time {}".format(end-start))