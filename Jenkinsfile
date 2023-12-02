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
post {
        always {
            // This block will always be executed, regardless of the build result
            bat 'docker logout'
        }

        failure {
            emailext(
                attachLog: true,
                body: '''<html>
                        <p>The build failed. Please check the Jenkins console output for details.</p>
                        <p>Build URL: ${BUILD_URL}</p>
                        </html>''',
                subject: 'Build Failure',
                to: 'harsh.sinha20@st.niituniversity.in, om.gholap20@st.niituniversity.in',
                mimeType: 'text/html'
            )

        }

        success {
            emailext(
                attachLog: true,
                body: 'The build was successful.',
                subject: 'Build Success',
                to: 'harsh.sinha20@st.niituniversity.in, om.gholap20@st.niituniversity.in',
                mimeType: 'text/html'
            )

        }
    }
}
