# streamlit run "C:\Users\cveas\OneDrive - ACEROS AZA S.A\OneDrive_v1\Escritorio\GITUPLOADS\streamlit_mysql_connection\streamlit_app.py"


import streamlit as st
import pyodbc

# ServerName = st.secrets["server"]
# MSQLDatabase = st.secrets["database"]
# username = st.secrets["username"]
# password = st.secrets["password"]

# Initialize connection.
# Uses st.cache_resource to only run once.
@st.cache_resource
def init_connection():
    return pyodbc.connect(
        "DRIVER={ODBC Driver 10 for SQL Server};SERVER="
        + st.secrets["server"]
        + ";DATABASE="
        + st.secrets["database"]
        + ";UID="
        + st.secrets["username"]
        + ";PWD="
        + st.secrets["password"]
    )

conn = init_connection()

# Perform query.
# Uses st.cache_data to only rerun when the query changes or after 10 min.
@st.cache_data(ttl=600)
def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()

rows = run_query("SELECT * from [SN2_COLADAAQ];")

# Print results.
for row in rows:
    st.write(f"{row[0]} has a :{row[1]}:")
