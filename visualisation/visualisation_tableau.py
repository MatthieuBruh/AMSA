import pandas as pd
import pygwalker as pyg

# TODO : pour la lecture des CSV
df = pd.read_csv('csv_path')

walker = pyg.walk(df)