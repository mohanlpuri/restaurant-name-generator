import streamlit as st
#import langChainHelper
import importlib
importlib.reload(langChainHelper)


st.title('Restaurant Name Generator ')

cuisine = st.selectbox('Enter Cuisine Type', ['Indian', 'American', 'Chinese', 'Italian', 'Mexican'])
Diet = st.selectbox('Enter Diet Type', ['Vegetarian', 'Non-Vegetarian', 'Vegan'])
result = None
if st.button('Generate'):
    result = langChainHelper.combined_chain.invoke({"cuisine": cuisine, "Diet": Diet})
    #st.text_area('Generated Restaurant Name and Menu', value=result, height=400)

if result:
    st.text_area ('**************Generated Restaurant Name and Menu ****************', value=result, height=400)
    print(result)


