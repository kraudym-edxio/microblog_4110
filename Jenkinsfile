pipeline {
  agent any
  
  
  environment {
      CONTAINER_NAME = "microblogApp1"
      IMAGE_NAME = "flaskapp"
      JOB_NAME = "Microblog Flask App"
      BUILD_URL = "http://127.0.0.1:5000/"
  }
  
  stages {
    stage('Checkout') {
      steps {
        checkout([$class: 'GitSCM', branches: [[name: '*/v2']], extensions: [], userRemoteConfigs: [[credentialsId: '7931395e-9774-4856-96ac-a8be7159a77e', url: 'git@github.com:kraudym-edxio/microblog-4110.git']]])
      }
    }
        stage('Unit Tests') {
            steps {
                withEnv(["PATH=/usr/local/bin:$PATH"]) {
                  sh 'pwd'
                    sh 'pytest --rootdir=/path/to/rootdir'
                }
            }
        }

    stage('Integration tests') {
        steps {
          echo 'Integration tests'
        }
    }


    stage('Build') {
      steps {
          echo 'Building'
          sh 'sudo docker build --tag $IMAGE_NAME .'
      }
    }
    /**

     stage('SonarQube analysis') {
    
      steps {

    		withSonarQubeEnv(installationName: 'SonarQube') {
				sh "/usr/local/bin/sonar-scanner -Dsonar.projectKey=projectkey -Dsonar.sources=."    		    
    		}
      }
    }*/
    stage('Deploy') {
      steps {
          echo 'Deploying'
          sh 'sudo docker stop $CONTAINER_NAME || true'
          sh 'sudo docker rm $CONTAINER_NAME || true'
          sh 'sudo docker run -d -p 5000:5000 --name $CONTAINER_NAME flaskapp'
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