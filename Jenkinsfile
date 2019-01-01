pipeline
{
    agent any
    environment {
	VIRTUAL_ENV = "${env.WORKSPACE}/venv"
	PATH = "{env.PATH}"
    }

    stages
    {
    	stage('Checkout') {
		steps {
			echo "Checkout Source Code"
			checkout scm
		}
	}
 	stage('Print Info') {
		steps {
			echo "Branch Name: ${env.BRANCH_NAME}"
			echo "BUILD_NUMBER : ${env.BUILD_NUMBER}"
			echo "BUILD_ID : ${env.BUILD_ID}"
			echo "JOB_NAME: ${env.JOB_NAME}"
			echo "BUILD_TAG : ${env.BUILD_TAG}"
			echo "EXECUTOR_NUMBER : ${env.EXECUTOR_NUMBER}"
			echo "NODE_NAME: ${env.NODE_NAME}"
			echo "NODE_LABELS : ${env.NODE_LABELS}"
			echo "WORKSPACE : ${env.WORKSPACE}"
			echo "JENKINS_HOME : ${env.JENKINS_HOME}"
		}
	}
	stage('Build') {
		steps {
			echo "Build Stage Starting"
			echo env.PATH
			bat """
				SET PATH=%PATH%
				if exist 'venv' rd /q /s 'venv'
				virtualenv venv
				pip install --upgrade pip
				pip install -r requirements.txt 
			"""
		}
	}
	stage('Unit tests')
	{
		steps {
			echo "Unit tests"
		}
	}
	stage('Deploy')
	{
		steps {
			echo "Deploy"
		}
	}
        stage('Integration tests')
        {
		steps {
			echo "Integration tests"
		}
        }
    }
}

