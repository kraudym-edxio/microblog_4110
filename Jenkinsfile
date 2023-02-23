pipeline {
  agent any
  
  
  environment {
      CONTAINER_NAME = "microblogApp1"
      IMAGE_NAME = "flaskapp"
      JOB_NAME = "Microblog Flask App"
      BUILD_URL = "http://172.22.127.61:5000/"
  }
  
  stages {
    stage('Checkout') {
      steps {
        checkout([$class: 'GitSCM', branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[credentialsId: '7931395e-9774-4856-96ac-a8be7159a77e', url: 'git@github.com:kraudym-edxio/microblog-4110.git']]])
      }
    }
    stage('Build') {
      steps {
          echo 'Building'
          sh 'sudo docker build --tag $IMAGE_NAME .'
      }
    }
     stage('SonarQube analysis') {
    
      steps {

    		withSonarQubeEnv(installationName: 'SonarQube') {
				sh "/usr/local/bin/sonar-scanner"    		    
    		}
      }
    }
    stage('Deploy') {
      steps {
          echo 'Deploying'
          sh 'sudo docker stop $CONTAINER_NAME || true'
          sh 'sudo docker rm $CONTAINER_NAME || true'
          sh 'sudo docker run -d -p 5000:5000 --name $CONTAINER_NAME flaskapp'
      }
    }
    stage('Integration tests') {
        steps {
          echo 'Integration tests'
        }
    }
  }

    post {
        always {
          echo 'Finished'
        }
      success {
          echo 'Pipeline succeeded'
      }
      failure {
          echo 'Pipeline failed'
          //discordSend description: "Failure", footer: "COMP-4110", link: env.BUILD_URL, result: currentBuild.currentResult, title: JOB_NAME, webhookURL: "https://ptb.discord.com/api/webhooks/1075565484306608198/BVAdPnc8ZMuDZG9neaEnIBekuNErtmd9FRQPMV66LS3eEfxZI3OLR87izK096ILhnejJ"

      }
    }
}