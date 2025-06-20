# import streamlit as st
# import pandas as pd
# from supabase import create_client, Client
# import uuid
# import time
#
# # Supabase config
# SUPABASE_URL = st.secrets["supabase"]["url"]
# SUPABASE_KEY = st.secrets["supabase"]["key"]
# supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
#
# # Table names
# TABLE_NAME = "Member"
# JOBS_TABLE = "Job"
#
# # Function to fetch data from a table
# def fetch_table_data(table_name):
#     response = supabase.table(table_name).select("*").execute()
#     if response.error:
#         st.error(f"Error fetching data from {table_name}: {response.error.message}")
#         return pd.DataFrame()
#     return pd.DataFrame(response.data)
#
# # Fetch data
# member_data = fetch_table_data(TABLE_NAME)
# job_data = fetch_table_data(JOBS_TABLE)
#
# # Display data using Streamlit
# st.title("Supabase Data Viewer")
#
# st.header("Member Table")
# st.dataframe(member_data)
#
# st.header("Job Table")
# st.dataframe(job_data)
#


import streamlit as st
from supabase import create_client

SUPABASE_URL = st.secrets["supabase"]["url"]
SUPABASE_KEY = st.secrets["supabase"]["key"]

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def fetch_data():
    response = supabase.table("TABLE_NAME").select("*").execute()
    if response.error:
        st.error(f"Error: {response.error.message}")
    else:
        st.write(response.data)

fetch_data()


