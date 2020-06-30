import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt 
# import seaborn_altair as salt  # https://github.com/Kitware/seaborn_altair
sns.set_style("whitegrid")


def plot_histograms(data):
    # cols = list(data.columns)
    # for i in cols:
    #     g = sns.distplot(data[i])
    # #g = sns.FacetGrid(data)
    
    return sns.distplot(data)

def plot_timeseries(data, t_col, selection):
    # 
    # g.map(plt.scatter, alpha=0.2)
    # g.add_legend()
    
    g = sns.lineplot(x = data[t_col], y = data.loc[selection], data = data)
    #g = data.plot(x = t_col, y = selection)
    
    return plt.plot(x = data[t_col], y = data[selection])

# def plot_timeseries_altair(data, t_col, selection):
#     chart = alt.Chart(data).mark_point().encode(
#     x='t_col:T', y = 'selection:Q')    # 'data.loc[:, selection]'
#     return chart

# data.loc[:, data.columns != t_col]

def plot_pairgrid(data, colour_by):
    cols = list(data.columns)
    g = sns.PairGrid(data, vars=cols, hue = colour_by)
    g.map(plt.scatter, alpha=0.2)
    g.add_legend()
    return g

# def plot_distribution(data, t_col, colour_by):
#     if ts_choice == 'Yes':
#         pass
#     else:
#         pass
# TODO: detect categorical variables and pass them to hue,
# whilst not plotting their values in the pairgrid
#     g = sns.PairGrid(data, vars=[data.columns,
#                  hue=categorical_choice, palette='RdBu_r')


