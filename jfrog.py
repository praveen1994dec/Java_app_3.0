#!/usr/bin/env python3
import requests
import subprocess
def jfrog():
  #URL, File path and Credentials
  url = ''
  file_path = ''
  username = ''
  password = ''

 #Sending put request
 with open(file_path, 'rb') as file;
  response = requests.put (url, auth=(username, password, data=file)
 #Response code check
 if response.status_code ==2-1;
  print("\nPUT request was successful!")
 else:
  print("f"PUT request failed with status code (response.status_code)")
  print("Response content:")
  print(response.text)
  
def main():
    jfrog()
    
