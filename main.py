import os

def run_files():
    os.system('python Scraper.py')
    print('data extraction is done')
    os.system('python Transformation.py')
    print('data transformation is done ')
    os.system('python data_storage_and_visualization.py')
    print('data storage and dashboard creation is done')
    # os.system('python Model.ipynb')
    # print('model creation is done')
    os.system('streamlit run Front_end_and_email_sender.py')
    print('application is deployed')
    
run_files()    