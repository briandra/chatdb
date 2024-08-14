import os 
import streamlit as st 
import mysql.connector
import pandas as pd

# App framework
st.set_page_config(page_title='ChatToDB', layout = 'centered', page_icon = 'logo.png', initial_sidebar_state = 'auto')
with st.sidebar:
    st.header("About")
    st.markdown(
        """
        This chatbot to answer questions about the financial data, regulation,
        and transactiob in the ministry of finance of Indonesia system.
        """
    )

#Using Try Catch
try:
    #Connecting to the Database
    connection = mysql.connector.connect(
    #host=os.environ["db_host"],
    #user=os.environ["db_user"],
    #password=os.environ["db_password"],
    #database=os.environ["db_name"],
    host='sql12.freesqldatabase.com',
    user='sql12725382',
    password='XaNwncKXdH',
    database='sql12725382'
)
    # Create a cursor object to interact with the database
    cursor = connection.cursor()

    # Define the SQL query you want to execute
    # query = f"SELECT * FROM {table_name} LIMIT 50"
    query = f"SELECT * FROM transactions LIMIT 50"

    # Execute the query
    cursor.execute(query)

    # Fetch all the rows returned by the query
    rows = cursor.fetchall()

    # Get column names from the cursor description
    column_names = [desc[0] for desc in cursor.description]

    # Close the cursor
    cursor.close()

    # Close the connection
    connection.close()

    # Convert the fetched rows into a DataFrame
    df = pd.DataFrame(rows, columns=column_names)

    # Print the DataFrame
    st.dataframe(df)
    
except Exception as e:
    st.write("⚠️ Sorry, Couldn't establish a connection to the Database")

finally:
    # Close the connection
    if connection.is_connected():
        connection.close()
