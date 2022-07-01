def make_forecasts():
    """Construya los pronosticos con el modelo entrenado final.
    Cree el archivo data_lake/business/forecasts/precios-diarios.csv. Este
    archivo contiene tres columnas:
    * La fecha.
    * El precio promedio real de la electricidad.
    * El pronóstico del precio promedio real.
    """
    import pandas as pd
    import pickle
    from sklearn.metrics import r2_score

    file = pd.read_csv(
        'data_lake/business/features/precios-diarios.csv', index_col=None, header=0)
    data_base = file.copy()

    file['Fecha'] = pd.to_datetime(file['Fecha'], format='%Y-%m-%d')
    file['year'], file['month'], file['day'] = \
        file['Fecha'].dt.year, file['Fecha'].dt.month, file['Fecha'].dt.day

    x_total = file.copy().drop('Fecha', axis=1)
    y_total = x_total.pop('Precio')

    reg = pickle.load(open('src/models/precios-diarios.pkl', 'rb'))
    prediction = reg.predict(x_total)

    r2_score(y_total,reg.predict(x_total))

    data_base['Prediction'] = prediction

    data_base.to_csv(
        'data_lake/business/forecasts/precios-diarios.csv', index=None)
#raise NotImplementedError("Implementar esta función")


if __name__ == "__main__":
    import doctest
    make_forecasts()
    doctest.testmod()
