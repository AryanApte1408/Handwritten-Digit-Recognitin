pipeline {
    agent any
    options {
        skipDefaultCheckout(true)
    }

    stages {
        stage('Git Checkout') {
            steps {
                git branch: 'master', url: 'https://github.com/AryanApte1408/Handwritten-Digit-Recognition.git'
            }
        }
    }

    stage('Build Images') {
            steps {
                script {
                    bat 'docker build -t om/mnist-capstone-new:code mnist'
                }
            }
        }
}
