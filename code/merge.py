import pandas as pd
from random import sample
import numpy as np
# given data frame df

for i in range(1,13):
    print i 
    df = pd.read_csv("../../data/trip_merged_"+str(i)+".csv")
    print i, "here"
    count = df.count()
    
    # create random index
    rindex =  np.array(sample(xrange(len(df)), int(len(df)*.01)))
    
    # get 10 random rows from df
    df_r = df.ix[rindex]
    with open('../../data/Final_mixed.csv', 'a') as f:
        df_r.to_csv(f)
    