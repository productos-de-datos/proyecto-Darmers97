def transform_data():
    """Transforme los archivos xls a csv.
    Transforme los archivos data_lake/landing/*.xls a data_lake/raw/*.csv. Hay
    un archivo CSV por cada archivo XLS en la capa landing. Cada archivo CSV
    tiene como columnas la fecha en formato YYYY-MM-DD y las horas H00, ...,
    H23.
    """
    import pandas as pd

    for f in range(1995, 2022):
        if f in range(1995, 2000):
            read_f = pd.read_excel(
                'data_lake/landing/{}.xlsx'.format(f), header=3)
            read_f.to_csv(
                'data_lake/raw/{}.csv'.format(f), index=None)
        elif f in range(2000, 2018):
            if f in [2016, 2017]:
                read_f = pd.read_excel(
                    'data_lake/landing/{}.xls'.format(f), header=2)
                read_f.to_csv(
                    'data_lake/raw/{}.csv'.format(f), index=None)
            else:
                read_f = pd.read_excel(
                    'data_lake/landing/{}.xlsx'.format(f), header=2)
                read_f.to_csv(
                    'data_lake/raw/{}.csv'.format(f), index=None)
        else:
            read_f = pd.read_excel(
                'data_lake/landing/{}.xlsx'.format(f), header=0)
            read_f.to_csv(
                'data_lake/raw/{}.csv'.format(f), index=None)



#raise NotImplementedError("Implementar esta función")

def test_date_validation():

    import pandas as pd

    for f in range(1995, 2022):
        read_f = pd.read_csv(
                'data_lake/raw/{}.csv'.format(f))
        assert ["Fecha"] == [read_f.columns.values[0]]

        
        
if __name__ == "__main__":
    import doctest
    transform_data()
    doctest.testmod()
