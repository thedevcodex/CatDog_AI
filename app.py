import streamlit as st
import tensorflow as tf
from tensorflow.keras.utils import load_img
import numpy as np

model = tf.keras.models.load_model('cat_dog_model.keras')
st.set_page_config(
    page_title=  "CatDog AI",
    page_icon = "https://img.icons8.com/?size=100&id=GzyPUsSOh1UV&format=png&color=000000" ,
    layout = "wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
.stApp{
      background: linear-gradient(135deg,
        black 10%,
        purple 100%,
        #2c5364 50%);
}
div.stButton > button {
    background-color: #FF9800;
    color: white;
    border: none;
    border-radius: 10px;
}
</style>

""",unsafe_allow_html=True)



st.title("CatDog AI 🐱🐶")
st.divider()
image_uploader = st.file_uploader(
    "Upload Cat or dog Image",
     type = ['jpg','jpeg','png','webp']
)
st.divider()

if image_uploader:
    col1 , col2,col3 = st.columns([1,2,1])
    with col2:
        st.image(image_uploader,width=700)
        st.write(" ")
        button_pred = st.button("Predict")
        if button_pred:
            img = load_img(image_uploader,target_size=(224,224))
            image_arr = np.array(img)/255.0
            image_arr = np.expand_dims(image_arr,axis=0)
            pred = model.predict(image_arr)
            if pred[0][0] > (0.5):
                st.success("Dog")
            else:
                st.success("Cat")
    st.divider()

    with st.container():
            st.markdown("""

                <style>
                
                    .card1{
                        background-color: green;
                        padding: 20px;
                        border-radius: 15px;
                        border: 1px solid black;
                        text-align: center
                    }
                </style>  
                <div class="card1">
                                <h3>Model: CNN</h3>
                                <p>This model is built using a CNN and trained on 2,000 images.</p>
                                <p><b>Task:</b> Cat vs Dog Classification</p>
                                <p><b>Input:</b> Cat/Dog Images</p>
                                <p><b>Output:</b> Cat or Dog</p>
                </div>
            """,unsafe_allow_html=True)
            st.write(" ")
            st.markdown("""
                    <div class='card1'>
                        <h3>Model Performance</h3>
                        <p>Training Accuracy: 83.20%</p>
                        <p>Validation Accuracy: 74.06%</p>
                        <p>Test Accuracy: 74.50%</p>
                    </div>

            """,unsafe_allow_html=True)
    st.divider()    
    st.caption("Note: Predictions may not always be accurate. This application is for educational purposes only.")
    st.caption("Built by thedevcodex")
    

