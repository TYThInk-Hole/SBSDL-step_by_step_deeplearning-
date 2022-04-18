import pandas as pd
import numpy as np
import os
from tkinter import filedialog
from tkinter import *

root = Tk()
root.directory = filedialog.askdirectory()
print(root.directory)

df_ppg=pd.DataFrame()

column_index=["SBP","DBP"]

for i in range(999):
    column_index.append(str(i))

for filename in os.listdir(root.directory):
    if filename.endswith('.csv'):
        data_load = pd.read_csv(os.path.join(root.directory,filename))
        ppg=np.array(data_load.iloc[1:-1,1]).tolist()
        df=pd.DataFrame(ppg).T
        s=pd.Series(ppg,index = df.columns)
        df_ppg=df_ppg.append(s,ignore_index=True)

directory="./" #new directory of feather file
fn=filename[0:-4] # extract same file name without '.csv'
ftype="ftr" #file type(feather)

new_filename=directory+fn+ftype

df_ppg.loc[0:-1].reset_index().to_feather(new_filename)