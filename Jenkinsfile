pipeline
{
    agent any
    environment {
	VIRTUAL_ENV = "${env.WORKSPACE}\\venv"
	UNIT_TEST_REPORT = "${env.WORKSPACE}\\tests\\unit-test.xml"
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
			bat """
				if exist ".venv" rd /q /s ".venv"
				virtualenv .venv
				call .venv/Scripts/activate
				pip install --upgrade pip
				pip install -r requirements.txt
				pip --version
				pip list
			"""
			echo "Build Stage Finsihed"
		}
	}
	stage('Unit Test')
	{
		steps {
			echo "Unit Tests Starting"
			bat """
				if exist "tests/unit-test.xml" del "tests/unit-test.xml" 
				call .venv/Scripts/activate
				python -m pytest -v --junitxml="tests/unit-test.xml" 
			"""
			echo "Unit Tests Finished"
		}
		post {
			always {
				junit keepLongStdio: true, testResults: "tests/unit-test.xml" 
			}
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

