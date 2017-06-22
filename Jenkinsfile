#!groovy

@Library('pipeline-library') _

def img

node {
    stage('build') {
        checkout(scm)
        img = buildApp(name: 'hypothesis/via')
    }

    stage('test') {
        testApp(image: img, runArgs: '-u root') {
            sh 'HTTP_PROXY= HTTPS_PROXY= pip install pytest'
            sh 'python -m pytest tests'
        }
    }

    onlyOnMaster {
        stage('release') {
            releaseApp(image: img)
        }
    }
}

onlyOnMaster {
    milestone()
    stage('qa deploy') {
        lock(resource: 'via-qa-deploy', inversePrecedence: true) {
            milestone()
            deployApp(image: img, app: 'via', env: 'qa')
        }
    }

    milestone()
    stage('prod deploy') {
        input(message: "Deploy to prod?")
        lock(resource: 'via-prod-deploy', inversePrecedence: true) {
            milestone()
            deployApp(image: img, app: 'via', env: 'prod')
        }
    }
}
