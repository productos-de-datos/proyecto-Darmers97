"""
Construya un pipeline de Luigi que:

* Importe los datos xls
* Transforme los datos xls a csv
* Cree la tabla unica de precios horarios.
* Calcule los precios promedios diarios
* Calcule los precios promedios mensuales

En luigi llame las funciones que ya creo.


"""
import luigi

from luigi import Task, LocalTarget


class DataIngestion(Task):
    """
    Uses the ingest_data function
    """
    def output(self):
        return LocalTarget('data_lake/landing/result.txt')

    def run(self):
        from ingest_data import ingest_data
        with self.output().open('w') as files_ingested:
            ingest_data()


class DataTransformation(Task):
    """
    Uses the transform_data function
    """
    def requires(self):
        return DataIngestion()

    def output(self):
        return LocalTarget('data_lake/raw/results2.txt')

    def run(self):
        from transform_data import transform_data
        with self.output().open('w') as files_transformed:
            transform_data()


class PricingScheduleTableCreation(Task):
    """
    Uses the clean_data function
    """
    def requires(self):
        return DataTransformation()

    def output(self):
        return LocalTarget('data_lake/cleansed/result3.txt')

    def run(self):
        from clean_data import clean_data
        with self.output().open('w') as table_created:
            clean_data()


class MeanDailyPrices(Task):
    """
    Uses the compute_daily_prices function
    """
    def requires(self):
        return PricingScheduleTableCreation()

    def output(self):
        return LocalTarget('data_lake/business/result4.txt')

    def run(self):
        from compute_daily_prices import compute_daily_prices
        with self.output().open('w') as daily_prices:
            compute_daily_prices()


class MeanMonthlyPrices(Task):
    """
    Uses the compute_monthly_prices function
    """
    def requires(self):
        return MeanDailyPrices()

    def output(self):
        return LocalTarget('data_lake/business/result5.txt')

    def run(self):
        from compute_monthly_prices import compute_monthly_prices
        with self.output().open('w') as monthly_prices:
            compute_monthly_prices()


if __name__ == "__main__":

    luigi.run(['MeanMonthlyPrices', '--local-scheduler'])
    
#raise NotImplementedError("Implementar esta función")



if __name__ == "__main__":
    import doctest

    doctest.testmod()
