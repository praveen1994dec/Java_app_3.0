#!/usr/bin/env python3

import requests
import subprocess

def jfrogUpload():
    url = 'http://54.153.105.80:8082/artifactory/example-repo-local/kubernetes-configmap-reload-0.0.1-SNAPSHOT.jar'
    file_path = '/home/ubuntu/Java_app_3.0/target/kubernetes-configmap-reload-0.0.1-SNAPSHOT.jar'
    username = 'admin'
    password = 'Mohit@14072002'

    with open(file_path, 'rb') as file:
        response = requests.put(url, auth=(username, password), data=file)

    if response.status_code == 201:
        print("\nPUT request was successful!")
    else:
        print(f"PUT request failed with status code {response.status_code}")
        print("Response content:")
        print(response.text)


def mvnBuild():

    maven_command = "mvn clean install -DskipTests"

    try:
        subprocess.run(maven_command, check=True, text=True, shell=True)
        print("\nMaven build completed successfully.")

    except subprocess.CalledProcessError as e:
        print(f"Error: Maven build failed with exit code {e.returncode}")


def main():
    mvnBuild()
    jfrogUpload()

#########################################################    
if  __name__  == "__main__":
    main()
