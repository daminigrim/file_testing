import pandas as pd
df1 = pd.read_csv(r"compair_file\2022-12-06.csv")
df2 = pd.read_csv(r"compair_file\2022-12-07.csv")
c_result = df2[~df2.apply(tuple,1).isin(df1.apply(tuple,1))]
file = pd.DataFrame(c_result)
file.to_csv(r"compair_file\Domain_file(07).csv",index=False,header=False)
print("Done!")