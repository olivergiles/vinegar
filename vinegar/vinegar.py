from operator import index
import click
import pandas as pd
import sys, os

@click.command()
@click.argument('file')
@click.option('-i','--indexc', is_flag=True)
def vinegar(file, indexc=None):
    index = None
    if indexc:
        index = 0
    filetypes = ('.csv')
    if not file.endswith(filetypes):
        return 'Invalid filetype'
    if file.endswith('.csv'):
        df = pd.read_csv(file,index_col=index)
        pd.to_pickle(df, file.replace('.csv', '.pkl'))

if __name__ == '__main__':
    vinegar()
