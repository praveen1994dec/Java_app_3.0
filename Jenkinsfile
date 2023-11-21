pipeline {
    agent any

    tools {
        // Specify the Maven tool by name
        maven 'Maven-3.9'
    }
    
    stages {
        stage ("Checkout from SCM") {
            steps {
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'Github_Credens', url: 'https://github.com/Zeeshanmedlari/Java_app_3.0.git']])
            }
        }
        stage ("Generate artifacts") {
            steps {
                sh 'mvn clean package'
            }
        }
        stage ("Simple") {
            steps {
                echo ("Its a simple script")
            }
        }
    }
}
