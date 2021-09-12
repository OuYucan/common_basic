import os
import streamlit.components.v1 as components
from streamlit import *
import streamlit as st
import numpy as np
import time
import pandas as pd

class Training:
    def __init__(self):
        st.set_page_config(
            page_title = "Ex-stream-ly Cool App",
            page_icon = "🧊",
            layout = "wide",
            initial_sidebar_state = "expanded",
        )

    def train(self):

        # embed streamlit docs in a streamlit app
        components.iframe("https://docs.streamlit.io/en/latest")

    def train12(self):
        def form_callback():
            st.write(st.session_state.my_slider)
            st.write(st.session_state.my_checkbox)
            help(st.session_state.my_slider)

        with st.form(key='my_form'):
            slider_input = st.slider('My slider', 0, 10, 5, key='my_slider')
            checkbox_input = st.checkbox('Yes or No', key='my_checkbox')
            submit_button = st.form_submit_button(label='Submit', on_click=form_callback)

    def train11(self):
        st.session_state['name'] = "value21"
        # Initialization
        if 'key' not in st.session_state:
            st.session_state['key'] = 'value'

        # Session State also supports attribute based syntax
        if 'key' not in st.session_state:
            st.session_state.key = 'value'

        st.write(st.session_state.key)

    def train10(self):
        df1 = pd.DataFrame(
            np.random.randn(5, 5),
            columns=('col %d' % i for i in range(5))
        )
        df2 = pd.DataFrame(
            np.random.randn(5, 5),
            columns=('col %d' % i for i in range(5))
        )
        my_table = st.table(df1)
        my_table.add_rows(df2)
        my_chart = st.line_chart(df1)
        my_chart.add_rows(df2)



    def train09(self):
            placeholder = st.empty()
             # Replace the placeholder with some text:
            placeholder.text("Hello")
             # Replace the text with a chart:
            placeholder.line_chart({"data": [1, 5, 2, 6]})
             # Replace the chart with several elements:
            with placeholder.container():
                st.write("This is one element")
                st.write("This is another")
             # Clear all those elements:
            # placeholder.empty()

    def train08(self):
        st.help(pd.DataFrame)
    
    def train07(self):
        with st.spinner('Wait for it2'):
            time.sleep(5)
        st.success('Done!')
        # write(21)
        st.balloons()

    def train06(self):
        my_bar = st.progress(0)
        for percent_complete in range(100):
            time.sleep(0.1)
            my_bar.progress(percent_complete + 1)


    def train05(self):
        def get_user_name():
            return 'John'

        with st.echo():
            # Everything inside this block will be both printed to the screen
            # and executed.

            def get_punctuation():
                return '!!!'

            greeting = "Hi there, "
            value = get_user_name()
            punctuation = get_punctuation()

            st.write(greeting, value, punctuation)

        # And now we're back to _not_ printing to the screen
        foo = 'bar'
        st.write('Done!')

    def train04(self):
        with st.echo():
            st.write('This code will be printed1')
            'without st.write'

    def train03(self):
        st.line_chart({"data": [1, 5, 2, 6, 2, 1]})
        with st.expander("See explanation"):
            st.write("""
               The chart above shows some numbers I picked for you.
               I rolled actual dice for these, so they're *guaranteed* to
               be random.""")
        st.image("https://static.streamlit.io/examples/dice.jpg")

    def train02(self):
        col1, col2 = st.columns([3, 1])
        data = np.random.randn(10, 1)

        col1.subheader("A wide column with a chart")
        col1.line_chart(data)

        col2.subheader("A narrow column with the data")
        col2.write(data)

    def train01(self):
        write("Training")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.header("A cat")
            st.image("https://static.streamlit.io/examples/cat.jpg")
        with col2:
            st.header("A dog")
            st.image("https://static.streamlit.io/examples/dog.jpg")
        
        with col3:
            st.header("An owl")
            st.image("https://static.streamlit.io/examples/owl.jpg")


if __name__ == "__main__":
    t = Training()
    t.train()
