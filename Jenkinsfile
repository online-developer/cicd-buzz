pipeline {
	agent any
	stages {
		stage('Test') {
			steps {
				sh 'python -m pytest -v --cov buzz/'
			}
		}
	}
