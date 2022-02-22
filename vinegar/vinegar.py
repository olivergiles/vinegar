from operator import index
import click
import pandas as pd
import sys, os

@click.command()
@click.argument('file')
def vinegar(file):
    filetypes = ('.csv')
    if not file.endswith(filetypes):
        return 'Invalid filetype'
    if file.endswith('.csv'):
        df = pd.read_csv(file,index_col=0)
        pd.to_pickle(df, file.replace('.csv', '.pkl'))
    #print(to_convert)

if __name__ == '__main__':
    vinegar()
