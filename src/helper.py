def createTable(tableName, cursor, k):
    query = f'CREATE TABLE IF NOT EXISTS {tableName}('
    for x in k:
        query = f'{query}{x} TEXT'
        if(k[-1] != x):
            query = f'{query},'
    query = f'{query})'
    cursor.execute(query)