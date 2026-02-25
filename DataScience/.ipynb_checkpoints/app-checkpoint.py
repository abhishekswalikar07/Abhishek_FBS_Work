import streamlit as st
import pickle
import numpy as np

st.set_page_config(
    page_title="Viral Post Predictor",
    layout="wide"
)

st.markdown("""
    <style>
    .main {
        background-color: #f5f7fa;
    }
    .stButton>button {
        background-color: #ff4b4b;
        color: white;
        font-size: 18px;
        border-radius: 10px;
        height: 3em;
        width: 100%;
    }
    .stButton>button:hover {
        background-color: #ff1a1a;
    }
    </style>
""", unsafe_allow_html=True)

with open("viral_model.pkl", "rb") as f:
    model = pickle.load(f)


platform_map = {
    "Instagram": 0,
    "TikTok": 1,
    "X": 2,
    "YouTube Shorts": 3
}

content_map = {
    "Carousel": 0,
    "Image": 1,
    "Text": 2,
    "Video": 3
}

topic_map = {
    "Education": 0,
    "Entertainment": 1,
    "Lifestyle": 2,
    "Politics": 3,
    "Sports": 4,
    "Technology": 5
}

language_map = {
    "English": 0,
    "Spanish": 1,
    "French": 2,
    "Hindi": 3,
    "Urudu": 4
}

region_map = {
    "Brazil": 0,
    "India": 1,
    "Pakistan": 2,
    "UK": 3,
    "US": 4
}


st.title(" Social Media Viral Post Predictor")
st.markdown("Predict whether your Social Media Post will go Viral..!")

st.sidebar.header("📌 Enter Post Details")

platform = st.sidebar.selectbox(
    "Platform",
    ["Select Platform"] + list(platform_map.keys())
)

content_type = st.sidebar.selectbox(
    "Content Type",
    ["Select Content Type"] + list(content_map.keys())
)

topic = st.sidebar.selectbox(
    "Topic",
    ["Select Topic"] + list(topic_map.keys())
)

language = st.sidebar.selectbox(
    "Language",
    ["Select Language"] + list(language_map.keys())
)

region = st.sidebar.selectbox(
    "Region",
    ["Select Region"] + list(region_map.keys())
)


st.sidebar.markdown("📊 Engagement Stats")

views = st.sidebar.number_input("Views", min_value=0)
likes = st.sidebar.number_input("Likes", min_value=0)
comments = st.sidebar.number_input("Comments", min_value=0)
shares = st.sidebar.number_input("Shares", min_value=0)
engagement_rate = st.sidebar.number_input("Engagement Rate", format="%.4f")
sentiment_score = st.sidebar.number_input("Sentiment Score", format="%.4f")

st.markdown("---")

col1, col2, col3, col4 = st.columns(4)

col1.metric("👁 Views", views)
col2.metric("👍 Likes", likes)
col3.metric("💬 Comments", comments)
col4.metric("🔁 Shares", shares)

st.markdown("---")

if st.button("🚀 Predict "):

    with st.spinner("Analyzing post..."):
        
        platform_val = platform_map[platform]
        content_val = content_map[content_type]
        topic_val = topic_map[topic]
        language_val = language_map[language]
        region_val = region_map[region]

        user_data = np.array([[platform_val, content_val, topic_val,
                               language_val, region_val,
                               views, likes, comments, shares,
                               engagement_rate, sentiment_score]])

        prediction = model.predict(user_data)


        st.markdown("## 📢 Prediction Result")

        if prediction[0] == 1:
            st.success("🔥 This Post is Likely to Go Viral!")
            st.balloons()
        else:
            st.error("❌ This Post is Not Likely to Go Viral")
            # st.snow()
            # st.toast("😢 Better luck next time!")