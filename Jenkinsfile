pipeline {
  agent any
  
  
  environment {
      CONTAINER_NAME = "microblogApp1"
      IMAGE_NAME = "flaskapp"
      JOB_NAME = "Microblog Flask App"
      BUILD_URL = "http://172.20.99.186:5000/"
  }
  
  stages {
    stage('Checkout') {
      steps {
        checkout([$class: 'GitSCM', branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[credentialsId: '353d0ea9-ea5a-4012-91cc-887fcd6abfee', url: 'git@github.com:kraudym-edxio/microblog-4110.git']]])
      }
    }
    
	stage('Unit Tests') {
		steps {
			withPythonEnv('/usr/bin/python3') {
			  sh 'pip install -r requirements.txt'
			  sh 'pip install pytest'
			  sh 'pytest'
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
	
		stage('Integration tests') {
			steps {
				withPythonEnv('/usr/bin/python3') {
          sh 'behave /var/lib/jenkins/workspace/microblog_v2/tests/features/'
				}
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