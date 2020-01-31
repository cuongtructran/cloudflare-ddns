pipeline {
  agent any
  environment {
    DOCKER_CRED = credentials('docker-hub-creds')
  }
  stages {
    stage('Build branch') {
      when {
        not {
          buildingTag()
        }
      }
      steps {
        echo 'Login docker hub'
        sh 'docker login -u $DOCKER_CRED_USR -p $DOCKER_CRED_PSW'
        echo 'Building & tagging docker image'
        sh 'docker build -t cuongtructran/py-cloudflare-ddns:${GIT_BRANCH#*/} .'
        sh 'docker tag cuongtructran/py-cloudflare-ddns:${GIT_BRANCH#*/} cuongtructran/py-cloudflare-ddns:${GIT_BRANCH#*/}-arm'
        echo 'Pushing to docker hub'
        sh 'docker push cuongtructran/py-cloudflare-ddns:${GIT_BRANCH#*/}'
        sh 'docker push cuongtructran/py-cloudflare-ddns:${GIT_BRANCH#*/}-arm'
//        echo 'Docker manifest'
//        sh 'docker manifest create cuongtructran/py-cloudflare-ddns:${GIT_BRANCH#*/} --amend cuongtructran/py-cloudflare-ddns:${GIT_BRANCH#*/}-amd64 --amend cuongtructran/py-cloudflare-ddns:${GIT_BRANCH#*/}-arm'
//        sh 'docker manifest push cuongtructran/py-cloudflare-ddns:${GIT_BRANCH#*/}'
      }
    }

    stage('Build tag') {
      when {
        buildingTag()
      }
      steps {
        echo 'Login docker hub'
        sh 'docker login -u $DOCKER_CRED_USR -p $DOCKER_CRED_PSW'
        echo 'Building & tagging docker image'
        sh 'docker build -t cuongtructran/py-cloudflare-ddns:${TAG_NAME} .'
        sh 'docker tag cuongtructran/py-cloudflare-ddns:${TAG_NAME} cuongtructran/py-cloudflare-ddns:${TAG_NAME}-arm'
        echo 'Pushing to docker hub'
        sh 'docker push cuongtructran/py-cloudflare-ddns:${TAG_NAME}'
        sh 'docker push cuongtructran/py-cloudflare-ddns:${TAG_NAME}-arm'
        echo 'Docker manifest'
        sh 'docker manifest create cuongtructran/py-cloudflare-ddns:${TAG_NAME} --amend cuongtructran/py-cloudflare-ddns:${TAG_NAME}-amd64 --amend cuongtructran/py-cloudflare-ddns:${TAG_NAME}-arm'
        sh 'docker manifest push cuongtructran/py-cloudflare-ddns:${TAG_NAME}'
      }
    }
  }
}