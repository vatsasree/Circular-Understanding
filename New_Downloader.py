import os
import requests
import pandas as pd
import logging

log_file = "download_log5.txt"
logging.basicConfig(filename=log_file, level=logging.ERROR, format='%(asctime)s - %(levelname)s: %(message)s')

def download_pdf_new(url, save_folder):
    try:
        # headers = {'Content-Type': 'application/pdf'}  # Specify content type
        response = requests.get(url, verify = False)
        print(response.status_code)
        print(url)
        if response.status_code == 200:
            # Extract the filename from the URL
            if url.endswith('.pdf') == False:
                # print(url)
                # filename = url.split("/")[-1]
                filename = os.path.basename(url)+'.pdf'
                print(filename)
            else:
                filename = url.split("/")[-1]  
                print(filename) 
            if len(filename) >= 100:
                filename = filename[:75]+'.pdf'
                print(filename)
                 
                     
            # If FileName is too Large then clip it to 30 characters
             
            try:
                # Create the full save path
                save_path = os.path.join(save_folder, filename)
                with open(save_path, 'wb') as file:
                    file.write(response.content)
            except Exception as e:
                print("Failed to save {} because of {}".format(filename, e))

            print("PDF downloaded and saved to {}".format(save_path))
        else:
            print("Failed to download PDF")
            logging.error("Failed to download PDF from URL: {}".format(url))
    except requests.exceptions.SSLError as ssl_error:
        print("Failed to establish SSL connection for URL: {} due to {}".format(url, ssl_error))
        logging.error("Failed to establish SSL connection for URL: {} due to {}".format(url, ssl_error))
    except Exception as e:
        print("Failed to download {} because of {}".format(filename, e))
        logging.error("Failed to download {} from URL: {} due to {}".format(filename, url, e))

# def download_pdf_new(url, save_folder):
#     try:
#         response = requests.get(url)
#         if response.status_code == 200:
#                    # Extract the filename from the URL
#             filename = url.split("/")[-1]

#             # If FileName is too Large then clip it to 30 characters
#             if len(filename) > 100:
#                 filename = filename[:100]

#             try:
#                 # Create the full save path
#                 save_path = os.path.join(save_folder, filename)
#                 with open(save_path, 'wb') as file:
#                     file.write(response.content)
#             except Exception as e:
#                 print(f"Failed to save {filename} because of {e}")

#             print(f"PDF downloaded and saved to {save_path}")
#         else:
#             print("Failed to download PDF")
#             logging.error(f"Failed to download PDF from URL: {url}")
#     except requests.exceptions.SSLError as ssl_error:
#         print(f"Failed to establish SSL connection for URL: {url} due to {ssl_error}")
#         logging.error(f"Failed to establish SSL connection for URL: {url} due to {ssl_error}")
#     except Exception as e:
#         print(f"Failed to download {filename} because of {e}")
#         logging.error(f"Failed to download {filename} from URL: {url} due to {e}")




########################
save_folder = "/home/ndli19/home2/sreevatsa/CircularData3"  

if not os.path.exists(save_folder):
    os.makedirs(save_folder)

df = pd.read_csv('/home/ndli19/home2/sreevatsa/Circulars-Data-Sheet8(1).csv')
links_list = list(df['PDF URL'])

for index, row in df.iterrows():
    new_save_folder = os.path.join(save_folder, row[1])

    if not os.path.exists(new_save_folder):
        os.makedirs(new_save_folder)

    try:
        download_pdf_new(row[0], new_save_folder)
    except:
        pass  # Skip the URL that caused an exception

# download_pdf_new('https://tshc.gov.in/2018/janvacation2018.pdf', '/home/ndli19/home2/sreevatsa/')
