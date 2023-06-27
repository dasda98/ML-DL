import io
import pandas as pd
from utils.logs.logs import log


class Data:
    def __init__(self, dataset_path: str):
        self.dataset_path = dataset_path

    def load_data(self) -> pd.DataFrame:
        return pd.read_csv(self.dataset_path)

    def information(self, dataset: pd.DataFrame):
        head = dataset.head()

        log.userLogger.debug(head)

        buf = io.StringIO()
        dataset.info(buf=buf)
        info = buf.getvalue()

        log.userLogger.debug(info)
