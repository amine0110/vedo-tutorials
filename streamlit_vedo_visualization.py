import streamlit as st
from vedo import load, show
import os
import uuid
from pathlib import Path
from multiprocessing import Process, Queue
import time

def load_show(stl_path: str, queue: Queue):  # Function to load and show the 3D object
    mesh = load(stl_path).color('#ffc800')  # Loading the 3D object and setting its color
    show(mesh, bg='black')  # Displaying the 3D object with a black background
    queue.put('done')  # Indicating that the process is done by putting 'done' in the queue

if __name__ == "__main__":  # Ensuring the script is being run directly and not imported
    st.set_page_config(page_title='Vedo Visualization', layout='wide')  # Setting the page configuration
    st.title('Vedo Visualization in Streamlit')  # Setting the title of the page

    uploaded_file = st.file_uploader("Choose an STL file", type="stl")  # Creating a file uploader for STL files
    if uploaded_file is not None:  # Checking if a file has been uploaded
        unique_id = str(uuid.uuid4())  # Generating a unique identifier

        os.makedirs(f'./data/{unique_id}', exist_ok=True)  # Creating a new directory for the uploaded file
        file_path = f'./data/{unique_id}/file.stl'  # Setting the path for the uploaded file
        
        with open(file_path, 'wb') as f:  # Opening the file in write mode
            f.write(uploaded_file.getbuffer())  # Writing the uploaded file to the new path

        st.success("File uploaded and saved in directory: " + str(file_path))  # Displaying a success message with the file path

        if st.button('Show Mesh'):  # Creating a button for displaying the 3D object
            queue = Queue()  # Creating a queue for parallel processing
            p = Process(target=load_show, args=(file_path, queue))  # Creating a process for loading and showing the 3D object
            p.start()  # Starting the process
            while True:  # Creating an infinite loop
                if not queue.empty():  # Checking if the queue is not empty
                    break  # Breaking the loop if the queue is not empty
                time.sleep(0.1)  # Pausing the loop for 0.1 seconds

