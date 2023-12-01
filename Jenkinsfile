pipeline {
    agent any
    options {
        skipDefaultCheckout(true)
    }

    stages {
        stage('Git Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/AryanApte1408/Handwritten-Digit-Recognition.git'
            }
        }

        stage('Build Images') {
            steps {
                script {
                    bat 'docker build -t omgholap/mnist-capstone-new:code .'
                }
            }
        }

        stage('Push Images to Hub') {
            steps {
                withDockerRegistry([ credentialsId: "omgholap-dockerhub", url: "" ]) {
                    bat 'docker push omgholap/mnist-capstone-new:code'
                }
            }
        }
    }

}
