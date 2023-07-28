pipeline{
  agent any
  environment{
    dockerhub=credentials('ce41d77d-920f-483d-8a33-50da3ade1d01')
  }
  stages{
    stage('check out scm'){
      steps{
        git branch: 'main',
            url: 'https://github.com/can997/numberGuess.git',
            credentialsId: '8bf4c9f9-3f5c-4604-87e0-be60898c30d5'
      }
    }
    stage('build image'){
       steps{
         sh 'sudo docker build -t guessnumber:$BUILD_NUMBER .'
       }
    }
    stage('tag image'){
      steps{
        sh 'sudo docker tag  guessnumber:$BUILD_NUMBER can997/guessnumber:$BUILD_NUMBER'
      }
    }
    stage('push image to DockerHub'){
      steps{
        sh 'echo  $dockerhub_PSW | sudo docker push can997/guessnumber:$BUILD_NUMBER --uusername $dockerhub_USR --password-stdin'
      }
    }
  }
}
