import streamlit as st
import plotly.express as px
from backend import get_data

# Add title, text input, slider, selectbox and subheader
st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forcast Days", min_value=1, max_value=5, help="Select the number of forcasted days")

option = st.selectbox("Select data to view",
                      ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

if place:
    # Get the temperature data
    filtered_data = get_data(place, days)


    if option == "Temperature":
        # Create a temperature plot
        temperatures = [dict["main"]["temp"] for dict in filtered_data]
        dates = [dict["dt_txt"] for dict in filtered_data]
        figure = px.line(x=dates, y=temperatures, labels={"x": "Date",
                                        "y": "Temperature (C)"})
        st.plotly_chart(figure)

    if option == "Sky":
        # render image of the sky
        images = {"Clear":"Images/clear.png", "Clouds":"Images/cloud.png",
                  "Rain":"Images/rain.png", "Snow":"Images/snow.png" }
        sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
        images_path = [images[condition] for condition in sky_conditions]

        st.image(images_path, width=100)