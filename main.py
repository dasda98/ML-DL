import logs
import pandas as pd

LOG = logs.LOG()


class Data:
    def __init__(self, dataset_path: str):
        self.dataset_path = dataset_path

    def load_data(self) -> pd.DataFrame:
        return pd.read_csv(self.dataset_path)

    def information(self, dataset: pd.DataFrame):
        head = dataset.head()
        LOG.log.info(head)


data = Data('./dataset/housing/housing.csv')
df = data.load_data()
data.information(df)