#practice pandas

income_table={'source':['rgnrn','rnt','wrtng'],'amount':[6200,600,1000]}
import pandas as pd

income_table_df=pd.DataFrame(income_table)
print(sum(income_table_df['amount']))
