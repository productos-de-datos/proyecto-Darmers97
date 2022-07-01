def train_daily_model():
    """Entrena el modelo de pronóstico de precios diarios.
    Con las features entrene el modelo de proóstico de precios diarios y
    salvelo en models/precios-diarios.pkl
    """
    from sklearn.linear_model import LinearRegression
    from sklearn.metrics import r2_score
    import pandas as pd
    import pickle

    file = pd.read_csv(
        'data_lake/business/features/precios-diarios.csv', index_col=None, header=0)

    file['Fecha'] = pd.to_datetime(file['Fecha'], format='%Y-%m-%d')
    file['year'], file['month'], file['day'] = \
        file['Fecha'].dt.year, file['Fecha'].dt.month, file['Fecha'].dt.day

    x_total = file.copy().drop('Fecha', axis=1)
    y_total = x_total.pop('Precio')

    x_train = x_total[:round(x_total.shape[0]*0.75)]
    x_test = x_total[round(x_total.shape[0]*0.75):]
    y_train = y_total[:round(x_total.shape[0]*0.75)]
    y_test = y_total[round(x_total.shape[0]*0.75):]

    reg = LinearRegression()
    reg.fit(x_train, y_train)

    r2_score(y_test,reg.predict(x_test))

    pickle.dump(reg, open('src/models/precios-diarios.pkl', 'wb'))

#raise NotImplementedError("Implementar esta función")


if __name__ == "__main__":
    import doctest
    train_daily_model()
    doctest.testmod()
