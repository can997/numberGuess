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
         sh 'docker build -t guessNumber'
       }
    }
    stage('tag image'){
      steps{
        sh 'docker tag  guessNumber can997/guessNumber'
      }
    }
    stage('push image to DockerHub'){
      steps{
        sh 'cat $dockerhub_PSW | docker push can997/guessNumber:$(env.BUILD_NUMBER} -u $dockerhub_USR --password-stdin'
      }
    }
  }
}
