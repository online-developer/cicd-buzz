pipeline
{
    agent any
    options {
	buildDiscarder(
		// Only keep the 10 most recent builds
		logRotator(numToKeepStr:'10'))
    }
    environment {
	VIRTUAL_ENV = "${env.WORKSPACE}/.venv"
	VIRTUAL_ENV_ACTIVATOR = "call .venv/Scripts/activate"
	TEST_DIR = "tests"
	CODE_COVERAGE_REPORT_NAME = "coverage.html"
	UNIT_TEST_REPORT = "${TEST_DIR}/unit-test.xml"
	CODE_COVERAGE_REPORT = "${TEST_DIR}/${CODE_COVERAGE_REPORT_NAME}"
	STATIC_CODE_ANALYSIS_REPORT = "${TEST_DIR}/flake8.log"
	APPLICATION_ROOT = "buzz"
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
				%VIRTUAL_ENV_ACTIVATOR%
				pip install --upgrade pip
				pip install -r requirements.txt
				pip --version
				pip list
			"""
			echo "Build Stage Finsihed"
		}
	}
	stage('Static Code Analysis') {
		steps {
			bat """
				%VIRTUAL_ENV_ACTIVATOR%
				flake8 --statistics --exit-zero --tee --output-file=%STATIC_CODE_ANALYSIS_REPORT% %APPLICATION_ROOT%
			"""
		}
	}
	stage('Unit Test') {
		steps {
			echo "Unit Tests Starting"
			bat """
				if exist "%UNIT_TEST_REPORT%" del "%UNIT_TEST_REPORT%" 
				%VIRTUAL_ENV_ACTIVATOR%
				python -m pytest -v --junitxml="%UNIT_TEST_REPORT%" --cov-report html:"%CODE_COVERAGE_REPORT%" --cov=%APPLICATION_ROOT%
			"""
			echo "Unit Tests Finished"
		}
	}
    }
    post {
	always {
		junit keepLongStdio: true, testResults: "${UNIT_TEST_REPORT}"
		recordIssues enabledForFailure: true, tool: pep8(pattern: '${STATIC_CODE_ANALYSIS_REPORT}')
		publishHTML target: [
			reportDir: '${TEST_DIR}',
			reportFiles: '${CODE_COVERAGE_REPORT_NAME}',
			reportName: 'Coverage Report - Unit Test'
		]
	}
    }
}

