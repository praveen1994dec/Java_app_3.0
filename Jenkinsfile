pipeline{
    agent any
    parameters{

        choice(name: 'action', choices: 'create\ndelete', description: 'Choose create/Destroy')
    }
    stages{
               stage ('Pushing Jfrog File'){
         when { expression {  params.action == 'create' } }
         steps{
           script{
                sh 'curl -X PUT -u admin:Password1 -T  /var/lib/jenkins/workspace/Java_app_3.0/target/kubernetes-configmap-reload-0.0.1-SNAPSHOT.jar "http://18.144.83.52:8082/artifactory/example-repo-local/kubernetes-configmap-reload-0.0.1-SNAPSHOT.jar"'
               }
           }
       }
          
    }
}
