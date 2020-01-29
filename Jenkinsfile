pipeline {
  agent any
  stages {
    stage('Build branch') {
      environment {
        DOCKER_USER = credentials('docker-hub-cred-user')
        DOCKER_PASS = credentials('docker-hub-cred-password')
      }

      steps {
        echo 'Login docker hub'
        sh 'docker login -u $DOCKER_USER -p $DOCKER_PASS'
      }
    }
  }
}