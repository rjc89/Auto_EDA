#https://www.youtube.com/watch?v=zK4Ch6e1zq8
import streamlit as st
import pandas as pd
from pandas.api.types import is_numeric_dtype
import analysis
from pandas_profiling import ProfileReport
import altair as alt
import matplotlib.pyplot as plt
import seaborn as sns 

st.title("Auto-EDA")
st.write('A tool for exploratory data analysis')
st.write('https://github.com/rjc89/Auto_EDA/blob/master/README.md')

uploaded_file = st.file_uploader("Choose a dataset .csv", type="csv")
#uploaded_file = "/home/robert/Documents/Auto_EDA/Q3-data.csv"
#uploaded_file = "/home/robert/Documents/Auto_EDA/housing.csv"
# provide housing.csv as a test dataset
if uploaded_file is not None:
    st.sidebar.title('Is this a time series dataset?')
    ts_choice = st.sidebar.selectbox('Time Series', ('Yes', 'No'))
    
    data = pd.read_csv(uploaded_file)
    st.write(data.head())

    # include pandas profile_report html output link to new page?
    # profile = ProfileReport(data, title="Pandas Profiling Report")
    # profile_html = profile.to_html()
    # st.markdown(profile_html, unsafe_allow_html=True)
    
    # extract the column names
    cols = list(data.columns)
    cols.append(None)

# TIME SERIES ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    if ts_choice == 'Yes':
        t_col = st.sidebar.selectbox('Select time/date column', cols)
        st.sidebar.title('Select Plot Variables')
        selection = st.sidebar.multiselect('', cols[:-1])

        st.sidebar.title('Group and Color By')
        colour_by = st.sidebar.selectbox('', cols)
        st.title('Time Series')
        st.subheader('Selection Overlay')    
        st.line_chart(data[selection])
         
        if colour_by == None:
            st.subheader('Group and Color By')
            st.write('***<---Select variable to group and color by***') 
            
        else:
            st.subheader('Group and Color By') 
            for i in selection:
                if i == t_col:
                    pass
                else:
                    c = alt.Chart(data).mark_line().encode(x = t_col+':Q', y = i+':Q',
                    tooltip = cols[:-1], color = colour_by+':N').interactive()
                    st.altair_chart(c, use_container_width=True)
        
# OTHER DATA ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    else:
        # selectbar for selecting target variables
        st.sidebar.title('Select Target Variable')
        target = st.sidebar.multiselect('Target', cols) 

        # sidebar for selecting categorical variables
        st.sidebar.title('Select Plot Variables')
        selection = st.sidebar.multiselect('', cols)

        st.sidebar.title('Colour By')
        colour_by = st.sidebar.selectbox('', cols)    
        
        #st.title('Distributions')

        show_dists = st.checkbox('Explore Distributions')
        if show_dists:
            st.subheader('Histograms')
            # plot histograms of selected variables
            plot_all = st.checkbox('Plot All Data')
            if plot_all:
                selection = cols[:-1]
            for i in selection:
                #bin_slider = st.slider('bin size')
                if is_numeric_dtype(data[i]):
                    c = alt.Chart(data).mark_bar().encode(alt.X(i+":Q",
                     bin=alt.Bin(extent=[0, data[i].max()], step=data[i].max()/50)),
                    y='count()',).interactive()
                    st.altair_chart(c, use_container_width=True)
                else:
                    pass
        else:
            pass

        show_pairwise = st.checkbox('Explore Pair Plots')
        if show_pairwise:
            st.subheader('Explore Pairwise')
