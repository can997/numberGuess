pipeline{
  agent any
  stages{
    stage('check out scm'){
      steps{
        git branch: 'main',
            url: 'https://github.com/can997/numberGuess.git'
            credentialsId: '8bf4c9f9-3f5c-4604-87e0-be60898c30d5'
      }
    }
    stage('build image'){
       steps{
         sh 'docker build -t guessNumber:${BUILD_NUMBER} .'
       }
    }
    stage('tag image'){
      steps{
        sh 'docker tag can997/guessNumber:${BUILD_NUMBER} guessNumber:${BUILD_NUMBER}'
      }
    }
    stage('push image to DockerHub){
      steps{
        sh 'cat $dockerhub_pass | docker push can997/guessNumber:$(BUILD_NUMBER} -u $dockerhub_user --password-stdin'
      }
    }
  }
}
