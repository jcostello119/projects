import streamlit as st
from PIL import Image
import io

# setup for page, title, layouts, etc.
st.set_page_config(page_title="My Portfolio", layout="wide")

#load in images needed
img_profile = Image.open("Profile.jpg")
img_Job_Project = Image.open("jobs_project.PNG")
img_coffee_shop = Image.open("coffee_shop.PNG")
img_sales_data = Image.open("sales_data.PNG")

# header section
with st.container():
    st.title("Welcome to my Portfolio Page")
    st.subheader("My name is Jordan")
    st.write(
        """
        I recently graduated from Indiana University, I am currently looking for a full-time entry level position in the field of data/business analytics. 
        This is my portfolio for you to be able to see some of the projects I have worked on.
        """
    )

    st.write("[LinkedIn Page](https://www.linkedin.com/in/jordan-costello/)")


# more description
with st.container():
    st.write("---")
    left_col, right_col = st.columns(2)
    with left_col:
        st.header("More about what I do")
        st.write("##")
        st.write(
            """
            I studied Business Informatics while in school and graduated with a Bachelors of Science degree.

            While studying Informatics I learned these languages: Python, SQL, VBA, HTML, and CSS
            
            I also learned various applications like Excel, Access, Tableau, and PowerBI.

            I have experience in extracting, transforming, and loading data to create both powerful and meaningful data stories.
            """ 
        )
    
    with right_col:
        st.image(img_profile, caption="This is me, hello!", width=450)

with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")

    image_col, text_col = st.columns((1, 2))
    with image_col:
        st.image(img_Job_Project)

    with text_col:
        st.subheader("Jobs Out of College Dashboard - Excel")
        st.write(
            """
            This is one of my Excel projects that I worked on. It provides insights on the 2022 Kelley School of Business graduation class and where/how many people were getting jobs.
            You will find various graphs and slicers that you can change to look at different data. This is a dynamic dashboard so all of the graphs will change when you change the inputs.
            You can click on the link to see a recording of me showing the project.
            """
        )
        st.markdown("[Here is a video](https://youtu.be/W96hZcWo2RM)")

with st.container():
    image_col, text_col = st.columns((1,2))
    with image_col:
        st.image(img_coffee_shop)

    with text_col:
        st.subheader("Coffee Sales Data - Excel")
        st.write(
            """
            This is another one of my Excel projects that I worked on. It provides insights on sales data for a specific coffee shop.
            You will find various graphs and slicers that you can change to look at different data. This is a dynamic dashboard so all of the graphs will change when you change the inputs.
            You can click on the link to see a recording of me showing the project.
            """
        )
        st.markdown("[Here is a video](https://youtu.be/aImykM0Auug)")
        
with st.container():
    image_col, text_col = st.columns((1,2))
    with image_col:
        st.image(img_sales_data)

    with text_col:
        st.subheader("Sales EDA - Python")
        st.write(
            """
            This is the first EDA Pandas project that I have started to work on. This is some sales data for a company for the years 2003-2005.
            I got a good start on in by cleaning and transforming the data to create visualizaitons I wanted to see. 
            I plan on adding more in depth analysis to this project but I am happy where I am so far.
            """
        )
        st.markdown("[Here is the link](https://github.com/jcostello119/projects/blob/main/Sales_Data.ipynb)")
