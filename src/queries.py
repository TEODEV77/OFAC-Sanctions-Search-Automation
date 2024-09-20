def records_query():
    query = '''
    SELECT p."idPersona", p."nombrePersona", dp.direccion, dp.pais 
    FROM "Personas" p 
    INNER JOIN "MaestraDetallePersonas" dp 
    ON p."idPersona" = dp."idPersona" 
    WHERE p."aConsultar" = %s
    '''
    params=('Si',)
    return {
        "query": query,
        "params": params
    }

def save_results_query(record, results_found, transaction_status):
    
    person_id, person_name, _, country = record 
    query = '''
    INSERT INTO "Resultadosuser8329" 
    ("idPersona", "nombrePersona", pais, "cantidadDeResultados", "estadoTransaccion") 
    VALUES (%s, %s, %s, %s, %s)
    '''
    values = (person_id, person_name, country, results_found, transaction_status)
    return {
        "query": query,
        "params": values
    }
    
def results_user8329():
    query = '''
    SELECT *
    FROM "Resultadosuser8329"
    '''
    params=()
    return {
        "query": query,
        "params": params
    }
    
def delete_results_user8329():
    query = '''
    DELETE FROM "Resultadosuser8329"
    '''
    params=()
    return {
        "query": query,
        "params": params
    }