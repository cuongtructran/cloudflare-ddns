pipeline {
  agent {
    docker {
      image 'docker:dind'
      args '-u root -v /var/run/docker.sock:/var/run/docker.sock'
    }
  }
  environment {
    DOCKER_CRED = credentials('docker-hub-creds')
  }
  stages {
    stage('Build branch') {
      when {
        branch 'master'
        not {
          buildingTag()
        }
      }
      steps {
        echo 'Enable experimental features'
        sh 'mkdir $HOME/.docker'
        sh 'echo \'{ "experimental": "enabled" }\' >> $HOME/.docker/config.json'
        echo 'Login docker hub'
        sh 'docker login -u $DOCKER_CRED_USR -p $DOCKER_CRED_PSW'
        echo 'Building & tagging docker image'
        sh 'docker build -t cuongtructran/py-cloudflare-ddns:latest-arm .'
        echo 'Pushing to docker hub'
        sh 'docker push cuongtructran/py-cloudflare-ddns:latest-arm'
        echo 'Docker manifest'
        sh 'docker manifest create cuongtructran/py-cloudflare-ddns:latest --amend cuongtructran/py-cloudflare-ddns:latest-arm --amend cuongtructran/py-cloudflare-ddns:latest-amd64'
        sh 'docker manifest push cuongtructran/py-cloudflare-ddns:latest'
      }
    }

    stage('Build tag') {
      when {
        buildingTag()
      }
      steps {
        echo 'Enable experimental features'
        sh 'mkdir $HOME/.docker'
        sh 'echo \'{ "experimental": "enabled" }\' >> $HOME/.docker/config.json'
        echo 'Login docker hub'
        sh 'docker login -u $DOCKER_CRED_USR -p $DOCKER_CRED_PSW'
        echo 'Building & tagging docker image'
        sh 'docker build -t cuongtructran/py-cloudflare-ddns:${TAG_NAME}-arm .'
        echo 'Pushing to docker hub'
        sh 'docker push cuongtructran/py-cloudflare-ddns:${TAG_NAME}-arm'
        echo 'Docker manifest'
        sh 'docker manifest create cuongtructran/py-cloudflare-ddns:${TAG_NAME} --amend cuongtructran/py-cloudflare-ddns:${TAG_NAME}-amd64 --amend cuongtructran/py-cloudflare-ddns:${TAG_NAME}-arm'
        sh 'docker manifest push cuongtructran/py-cloudflare-ddns:${TAG_NAME}'
      }
    }
  }
}