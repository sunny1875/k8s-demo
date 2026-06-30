pipeline {
    agent any

    environment {
        GIT_SSH_COMMAND = "ssh -o StrictHostKeyChecking=no -i /var/jenkins_home/.ssh/id_rsa_git"
    }

    stages {
        stage('信息收集') {
            steps {
                sh '''
                    echo "========================================="
                    echo "  构建 #${BUILD_NUMBER}"
                    echo "========================================="
                    echo "分支: $(git branch --show-current)"
                    echo "提交: $(git log --oneline -1)"
                    echo "作者: $(git log -1 --format='%an <%ae>')"
                    echo "时间: $(git log -1 --format='%ad')"
                    echo "说明: $(git log -1 --format='%s')"
                    echo "========================================="
                '''
            }
        }

        stage('查看项目文件') {
            steps {
                sh 'ls -la'
                sh 'cat app.py'
            }
        }

        stage('完成') {
            steps {
                echo "构建完成"
            }
        }
    }
}
