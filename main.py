import streamlit as st
import tensorflow as tf
import numpy as np

#Tensorflow model Prediction
def model_prediction(test_image):
    model = tf.keras.models.load_model('trained_model.keras')
    image = tf.keras.preprocessing.image.load_img(test_image,target_size=(128,128))
    input_arr = tf.keras.preprocessing.image.img_to_array(image)
    input_arr = np.array([input_arr]) #convert single image to a batch
    prediction = model.predict(input_arr)
    result_index = np.argmax(prediction)
    return result_index

#Sidebar of the UI
st.sidebar.title("Dashboard")
app_mode = st.sidebar.selectbox("Select Page",["Home","Disease Detection","About"])

#home page
if(app_mode=="Home"):
    st.header("PLANT DISEASE DETECTION SYSTEM")
    home_img = "home_page.jpg"
    st.image(home_img,use_column_width=True)
    st.markdown("""
        ## 🌿 Plant Disease Prediction Web App

Welcome to the **Plant Disease Prediction System**!  
This application helps you identify plant diseases by analyzing leaf images using a trained machine learning model.

---

###  How to Use the System

Follow these simple steps:

#### 1️ Upload an Image
- Click on the **"Upload Image"** button.
- Select a clear image of a plant leaf from your device.
- Supported formats: `.jpg`, `.jpeg`, `.png`.

#### 2️ Image Preview
- Once uploaded, the image will be displayed on the screen.
- Make sure the leaf is clearly visible for accurate prediction.

#### 3️ Run Prediction
- Click on the **"Predict"** button.
- The system will process the image using the trained model.

#### 4️ View Results
- The predicted **disease name** will be displayed.
- Additional information such as **confidence score** may also be shown.

---

###  Important Tips
- Use **high-quality images** for better accuracy.
- Ensure the leaf is **not blurred or cropped too much**.
- Avoid images with **multiple leaves or complex backgrounds**.

---

###  Example Workflow
1. Upload leaf image  
2. Click predict  
3. View disease result  

---

###  Features
- Fast and accurate predictions  
- Easy-to-use interface  
- Supports multiple plant diseases  

---

**Happy Farming! 🌱**
    """)


#About page
elif(app_mode=="About"):
    st.header("About")
    st.markdown("""
    #### About Dataset : 
    This dataset is recreated using offline augmentation from the original dataset. The original dataset can be found on this github repo. This dataset consists of about 87K rgb images of healthy and diseased crop leaves which is categorized into 38 different classes. The total dataset is divided into 80/20 ratio of training and validation set preserving the directory structure. A new directory containing 33 test images is created later for prediction purpose.
                
    #### Content : 
    1. Train (70K+ Images)
    2. Valid (17K+ Images)
    3. Test (33 Images)
""")
    

#Detection Page
elif(app_mode == "Disease Detection"):
    st.header("Disease Detection")
    test_image = st.file_uploader("Select an Image: ")
    if(st.button("Show Image")):
        st.image(test_image,use_column_width=True)

    #detect button
    if(st.button("Detect")):
        st.snow()
        st.write("Our Prediction : ")
        result_index = model_prediction(test_image)
        #defining class
        class_name = ['Apple___Apple_scab',
 'Apple___Black_rot',
 'Apple___Cedar_apple_rust',
 'Apple___healthy',
 'Blueberry___healthy',
 'Cherry_(including_sour)___Powdery_mildew',
 'Cherry_(including_sour)___healthy',
 'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot',
 'Corn_(maize)___Common_rust_',
 'Corn_(maize)___Northern_Leaf_Blight',
 'Corn_(maize)___healthy',
 'Grape___Black_rot',
 'Grape___Esca_(Black_Measles)',
 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)',
 'Grape___healthy',
 'Orange___Haunglongbing_(Citrus_greening)',
 'Peach___Bacterial_spot',
 'Peach___healthy',
 'Pepper,_bell___Bacterial_spot',
 'Pepper,_bell___healthy',
 'Potato___Early_blight',
 'Potato___Late_blight',
 'Potato___healthy',
 'Raspberry___healthy',
 'Soybean___healthy',
 'Squash___Powdery_mildew',
 'Strawberry___Leaf_scorch',
 'Strawberry___healthy',
 'Tomato___Bacterial_spot',
 'Tomato___Early_blight',
 'Tomato___Late_blight',
 'Tomato___Leaf_Mold',
 'Tomato___Septoria_leaf_spot',
 'Tomato___Spider_mites Two-spotted_spider_mite',
 'Tomato___Target_Spot',
 'Tomato___Tomato_Yellow_Leaf_Curl_Virus',
 'Tomato___Tomato_mosaic_virus',
 'Tomato___healthy']
        st.success("It is a {}".format(class_name[result_index]))


