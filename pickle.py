import pickle
import streamlit as st
 
# loading the trained model
pickle_in = open("C:\\Users\\Nidhi Sheth\\Downloads\\classifier.pkl", 'rb') 
classifier = pickle.load(pickle_in)
 
@st.cache()
  
# defining the function which will make the prediction using the data which the user inputs 
def prediction(input1,input2,input3,input4,input5,input6,input7,input8,input9,input10,input11,input12,input13,input14,input15,input16,input17,input18,input19,input20):   
    
    # Making predictions 
    prediction = classifier.predict( 
        [[input1,input2,input3,input4,input5,input6,input7,input8,input9,input10,input11,input12,input13,input14,input15,input16,input17,input18,input19,input20]])
     
    if prediction == 0.0:
        pred = 'Unsafe'
    else:
        pred = 'Safe'
    return pred
      
  
# this is the main function in which we define our webpage  
def main():       
    # front end elements of the web page 
    html_temp = """ 
    <div style ="background-color:blue;padding:13px"> 
    <h1 style ="color:white;text-align:center;">Water Quality Test</h1> 
    </div> 
    """
      
    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True) 
      
    # following lines create boxes in which user can enter data required to make prediction 
    Amount1 = st.number_input("Total aluminium amount")
    Amount2 = st.number_input("Total ammonia amount")
    Amount3 = st.number_input("Total arsenic amount")
    Amount4 = st.number_input("Total barium amount")
    Amount5 = st.number_input("Total cadmium amount")
    Amount6 = st.number_input("Total chloramine amount")
    Amount7 = st.number_input("Total chromium amount")
    Amount8 = st.number_input("Total copper amount")
    Amount9 = st.number_input("Total flouride amount")
    Amount10 = st.number_input("Total bacteria amount")
    Amount11 = st.number_input("Total viruses amount")
    Amount12 = st.number_input("Total lead amount")
    Amount13 = st.number_input("Total nitrates amount")
    Amount14 = st.number_input("Total nitrites amount")
    Amount15 = st.number_input("Total mercury amount")
    Amount16 = st.number_input("Total perchlorate amount")
    Amount17 = st.number_input("Total radium amount")
    Amount18 = st.number_input("Total selenium amount")
    Amount19 = st.number_input("Total silver amount")
    Amount20 = st.number_input("Total uranium amount")
    result =""
      
    # when 'Predict' is clicked, make the prediction and store it 
    if st.button("Predict"): 
        result = prediction(Amount1,Amount2,Amount3,Amount4,Amount5,Amount6,Amount7,Amount8,Amount9,Amount10,Amount11,Amount12,Amount13,Amount14,Amount15,Amount16,Amount17,Amount18,Amount19,Amount20) 
        st.success('Water Sample is {}'.format(result))
if __name__=='__main__': 
    main()