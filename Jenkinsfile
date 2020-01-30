pipeline {
  agent any
  stages {
    stage('Build branch') {
      environment {
        DOCKER_CRED = credentials('docker-hub-creds')
      }

      steps {
        echo 'Login docker hub'
        sh 'docker login -u $DOCKER_CRED_USR -p $DOCKER_CRED_PSW'
        sh 'docker build -t cuongtructran/py-cloudflare-ddns:${GIT_BRANCH#*/}-arm .'
        sh 'docker push cuongtructran/py-cloudflare-ddns:${GIT_BRANCH#*/}-arm'
      }
    }
  }
}