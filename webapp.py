import streamlit as st
import pandas as pd
import analysis
from pandas_profiling import ProfileReport 

st.title("Auto-EDA")
st.write('A tool for exploratory data analysis')
#uploaded_file = st.file_uploader("Choose a dataset", type="csv")
uploaded_file = "/home/robert/Documents/Auto_EDA/housing.csv"
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

    if ts_choice == 'Yes':
        t_col = st.sidebar.selectbox('Select time/date column', cols)
        st.sidebar.title('Select Plot Variables')
        selection = st.sidebar.selectbox('Select Variable', cols)
        st.pyplot(analysis.plot_timeseries(data, t_col, selection)) 
        #st.altair_chart(analysis.plot_timeseries(data, t_col, selection))
        # add overlay time series button

    else:
        # plot histograms of variables
        
        # st.title('Histograms')
        # st.pyplot(analysis.plot_histograms(data))
        # selectbar for selecting target variables
        st.sidebar.title('Select Target Variable')
        target = st.sidebar.multiselect('Target', cols) 

        # sidebar for selecting categorical variables
        st.sidebar.title('Deselect Plot Variables')
        deselection = st.sidebar.multiselect('Deselection', cols)

        st.sidebar.title('Colour By Variable')
        colour_by = st.sidebar.selectbox('colour by', cols)    
        
        #plotting a pair grid
        st.title('Pair Grid')
        #st.pyplot(analysis.plot_pairgrid(data.loc[:, cols != deselection], colour_by))
        st.pyplot(analysis.plot_histograms(data.loc[:, cols != deselection]))
        
        
        # Plotting correlation plot of variables with specified R^2 cutoff

        # plotting pairs of variables of interest
        # st.title('Explore Pairwise')
        # st.write('Select variables')
        # st.altair_chart(selection)
    
