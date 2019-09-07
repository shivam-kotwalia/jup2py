#!/usr/bin/env python
# coding: utf-8
import pandas as pd
import numpy  as np
import matplotlib.pyplot as plt
import sklearn
from sklearn.datasets import load_iris
data = load_iris()
data.keys()
df = pd.DataFrame(data["data"], columns=data["feature_names"])
df["target_names"] = data["target"] 
df.head()
# #### Some Graphs 
df.plot(figsize=(15, 8), title="Flower attributes")
df.target_names.astype("O").value_counts().plot.pie()