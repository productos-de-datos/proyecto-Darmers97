def compute_monthly_prices():
    """Compute los precios promedios mensuales.

    Usando el archivo data_lake/cleansed/precios-horarios.csv, compute el prcio
    promedio mensual. Las
    columnas del archivo data_lake/business/precios-mensuales.csv son:

    * fecha: fecha en formato YYYY-MM-DD

    * precio: precio promedio mensual de la electricidad en la bolsa nacional



    """
    import pandas as pd
    
    
    
    data_cleanner = pd.read_csv('data_lake/cleansed/precios-horarios.csv',
                     index_col=None, header=0)
    data_cleanner['Fecha'] = pd.to_datetime(data_cleanner['Fecha'], format='%Y-%m-%d')
    df = data_cleanner.groupby(data_cleanner['Fecha'].dt.to_period('M'))[
        'Precio'].mean().reset_index()
    df['Fecha'] = pd.to_datetime(
        df['Fecha'].astype(str), format='%Y-%m')

    
    df.to_csv(
        'data_lake/business/precios-mensuales.csv', index=None)
    
    
    

if __name__ == "__main__":
    import doctest
    compute_monthly_prices()
    doctest.testmod()
