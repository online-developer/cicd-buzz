pipeline {
	agent any
	stages {
		stage('Test') {
			steps {
				python -m pytest -v --cov buzz/
			}
		}
	}
