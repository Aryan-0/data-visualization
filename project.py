import pandas as pd
import plotly.graph_objects as go
import numpy
import matplotlib.pyplot as plt
#read_csv converts the data into data frame
df = pd.read_csv("data.csv")
dfPart = df.loc[df["student_id"]==  "TRL_xsl"]
gg = dfPart.groupby("level")["attempt"].mean()
print(gg)

pf = go.Bar(y = gg, x = ["level 1","level 2","level 3","level 4"], orientation = "v")
tt = go.Figure(pf)
tt.show()