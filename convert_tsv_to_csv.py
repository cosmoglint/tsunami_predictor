import numpy as np
import pandas as pd
import sklearn
import re



tsv_f = open('tsunami_data.tsv', 'r')
csv_f = open('tsunami_data.csv', 'w')

for content in tsv_f:
    content = re.sub("\t",",",content)
    csv_f.write(content)

csv_f.close()
tsv_f.close()
