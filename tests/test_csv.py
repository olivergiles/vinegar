import os
import pandas as pd

def test_csv():
    test_path = os.path.dirname(__file__)
    data_path = os.path.join(test_path, 'data')
    pickle_path = os.path.join(data_path, 'example_pickle.pkl')
    csv_path = os.path.join(data_path, 'example_csv.csv')
    temp_path = os.path.join(data_path, 'temp')
    os.system(f'(cd {data_path} && mkdir temp)')
    os.system(f'cp {csv_path} {temp_path}')
    os.system(f'(cd {temp_path} && vinegar example_csv.csv)')
    attempt = pd.read_pickle(f'{os.path.join(temp_path, "example_csv.pkl")}')
    os.system(f'rm -f -r {temp_path}')
    assert((3,3) == attempt.shape)
