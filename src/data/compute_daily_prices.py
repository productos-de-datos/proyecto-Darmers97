def compute_daily_prices():
    """Compute los precios promedios diarios.

    Usando el archivo data_lake/cleansed/precios-horarios.csv, compute el prcio
    promedio diario (sobre las 24 horas del dia) para cada uno de los dias. Las
    columnas del archivo data_lake/business/precios-diarios.csv son:

    * fecha: fecha en formato YYYY-MM-DD

    * precio: precio promedio diario de la electricidad en la bolsa nacional



    """
    import pandas as pd
    
    
    
    data_cleanner = pd.read_csv('data_lake/cleansed/precios-horarios.csv',
                     index_col=None, header=0)
    data_cleanner['Fecha'] = pd.to_datetime(data_cleanner['Fecha'], format='%Y-%m-%d')
    df = data_cleanner.groupby(data_cleanner['Fecha'])[
        'Precio'].mean().reset_index()

    df.to_csv(
        'data_lake/business/precios-diarios.csv', index=None)
    
    
    
#raise NotImplementedError("Implementar esta función")


def test_save_no_format():

    import pandas as pd
    read_f = pd.read_csv(
                'data_lake/business/precios-diarios.csv')
    assert str(read_f['Fecha'].dtypes) == "object"
    
    
    
    
if __name__ == "__main__":
    import doctest
    compute_daily_prices()
    doctest.testmod()
