pipeline {
  agent any
  environment {
    DOCKER_CRED = credentials('docker-hub-creds')
  }
  stages {
    stage('Build branch') {
      steps {
        echo 'Login docker hub'
        sh 'docker login -u $DOCKER_CRED_USR -p $DOCKER_CRED_PSW'
        echo 'Building & tagging docker image'
        sh 'docker build -t cuongtructran/py-cloudflare-ddns:${GIT_BRANCH#*/}-arm .'
        echo 'Pushing to docker hub'
        sh 'docker push cuongtructran/py-cloudflare-ddns:${GIT_BRANCH#*/}-arm'
      }
    }

    stage('Build tag') {
      when {
        buildingTag()
      }
      steps {
        sh 'printenv '
      }
    }
  }
}