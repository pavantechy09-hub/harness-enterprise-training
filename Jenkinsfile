// This is the legacy Jenkins pipeline we migrate FROM on Day 3
// Kept for reference to show side-by-side comparison
// Compare with: .harness/pipelines/day3-jenkins-migration.yaml
pipeline {
  agent any

  environment {
    AWS_REGION = 'us-east-1'
  }

  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }

    stage('Security Scan') {
      steps {
        sh 'pip install checkov'
        sh 'checkov -d infra/ --framework terraform --quiet'
      }
    }

    stage('Test payments-service') {
      steps {
        sh '''
          cd src/payments-service
          pip install -r requirements.txt
          pytest app/tests/ -v
        '''
      }
    }

    stage('Manual Approval') {
      when { branch 'main' }
      steps {
        input message: 'Deploy to dev?', ok: 'Deploy'
      }
    }

    stage('Deploy to Dev') {
      when { branch 'main' }
      steps {
        sh 'kubectl apply -f k8s/payments-service/ -n payments'
        sh 'kubectl rollout status deployment/payments-service -n payments'
      }
    }
  }

  post {
    failure {
      slackSend channel: '#alerts',
        message: "FAILED: ${env.JOB_NAME} - ${env.BUILD_URL}"
    }
    success {
      slackSend channel: '#deployments',
        message: "DEPLOYED: ${env.JOB_NAME}"
    }
  }
}
