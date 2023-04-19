pipeline {
  agent any
  
  
  environment {
      CONTAINER_NAME = "microblogApp1"
      IMAGE_NAME = "flaskapp"
      JOB_NAME = "Microblog Flask App"
      BUILD_URL = "http://localhost:5000/"
  }
  
  stages {
stage('Checkout') {
  steps {
    checkout([$class: 'GitSCM', branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/miguelgrinberg/microblog.git']]])
  }
}

    

	stage('Unit Tests') {
		steps {
			withPythonEnv('/usr/bin/python3') {
			    sh 'sed -i "s/greenlet.*/greenlet>=1.2.0a1/" requirements.txt' 
			  sh 'pip install -r requirements.txt'
			}
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
				sh "/usr/local/bin/sonar-scanner -Dsonar.projectKey=projectkey -Dsonar.sources=."    		    
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