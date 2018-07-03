import pandas as pd 
import io
import sys

filepath=sys.argv[1]

df=pd.read_csv(filepath)
buf=io.StringIO()
df.info(buf=buf)
s = buf.getvalue()
with open("Output.txt", "w") as text_file:
	text_file.write(s)

buf=io.StringIO()
s=df.isnull().sum()

with open("MissingValueOutput.txt", "w") as text_file:
    text_file.write(str(s))

