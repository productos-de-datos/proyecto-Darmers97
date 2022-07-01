def clean_data():
    """Realice la limpieza y transformación de los archivos CSV.

    Usando los archivos data_lake/raw/*.csv, cree el archivo data_lake/cleansed/precios-horarios.csv.
    Las columnas de este archivo son:

    * fecha: fecha en formato YYYY-MM-DD
    * hora: hora en formato HH
    * precio: precio de la electricidad en la bolsa nacional

    Este archivo contiene toda la información del 1997 a 2021.


    """

    import pandas as pd
    import glob

    path = glob.glob(r'data_lake/raw/*.csv')

    for i, file in enumerate(path):
        if i == 0:
            inicial = pd.read_csv(file, index_col=None, header=0)
            hours = inicial.iloc[:, :25]
            hours.columns = ['Fecha']+[('0'+str(i))[-2:] for i in range(24)]
            inicial_transform = hours.melt(
                id_vars='Fecha', var_name='Hora', value_name='Precio')
            final = inicial_transform
        else:
            inicial = pd.read_csv(file,
            index_col=None, header=0)
            hours = inicial.iloc[:, :25]
            hours.columns = ['Fecha']+[('0'+str(i))[-2:] for i in range(24)]
            inicial_transform = hours.melt(
                id_vars='Fecha', var_name='Hora', value_name='Precio')
            final = pd.concat([final, inicial_transform])
    final.to_csv('data_lake/cleansed/precios-horarios.csv', index=None)
#raise NotImplementedError("Implementar esta función")
def test_final_columns():

    import pandas as pd
    read_f = pd.read_csv(
                'data_lake/cleansed/precios-horarios.csv')
    assert ["Fecha","Hora","Precio"] == list(read_f.columns.values)

if __name__ == "__main__":
    import doctest
    clean_data()
    doctest.testmod()
