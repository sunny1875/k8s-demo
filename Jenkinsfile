pipeline {
    agent any

    environment {
        IMAGE_NAME = "k8s-demo"
        IMAGE_TAG = "${BUILD_NUMBER}"
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

        stage('Docker 构建镜像') {
            steps {
                sh 'docker build -t ${IMAGE_NAME}:${IMAGE_TAG} .'
                sh 'docker tag ${IMAGE_NAME}:${IMAGE_TAG} ${IMAGE_NAME}:latest'
                echo "镜像构建完成: ${IMAGE_NAME}:${IMAGE_TAG}"
            }
        }

        stage('验证镜像') {
            steps {
                sh '''
                    echo "--- 查看构建的镜像 ---"
                    docker images ${IMAGE_NAME}
                    echo ""
                    echo "--- 测试容器启动 ---"
                    docker run -d --name test-${BUILD_NUMBER} -p 8888:8080 ${IMAGE_NAME}:${IMAGE_TAG}
                    echo ""
                    echo "--- 等待服务启动并访问测试 ---"
                    for i in 1 2 3 4 5; do
                        sleep 2
                        RESULT=$(curl -s http://localhost:8888 2>/dev/null)
                        if [ -n "$RESULT" ]; then
                            echo "访问成功: $RESULT"
                            break
                        fi
                        echo "等待中... ($i/5)"
                    done
                    docker rm -f test-${BUILD_NUMBER} || true
                '''
            }
        }

        stage('完成') {
            steps {
                echo "🎉 全部阶段执行成功！"
                echo "镜像: ${IMAGE_NAME}:${IMAGE_TAG}"
                echo "运行: docker run -d -p 8888:8080 ${IMAGE_NAME}:${IMAGE_TAG}"
            }
        }
    }

    post {
        failure {
            sh 'docker rm -f test-${BUILD_NUMBER} || true'
            echo "❌ 构建失败，请检查日志"
        }
    }
}
