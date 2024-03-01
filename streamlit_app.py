import streamlit as st
import pyodbc


con_str = f'Driver={{SQL Server}};Server={server};Database={database};Uid={username};Pwd={password};Encrypt=Yes;TrustServerCertificate=No;Authentication={auth};'
# Initialize connection.
# Uses st.cache_resource to only run once.
@st.cache_resource
def init_connection():
    return pyodbc.connect(con_str)
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
