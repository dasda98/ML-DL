from utils.data.data import Data


if __name__ == '__main__':
    data = Data('./dataset/housing/housing.csv')
    df = data.load_data()
    data.information(df)

