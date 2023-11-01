pipeline {

    agent any

 

    stages 

    {

        stage('Hello') 

        {

            steps 

            {

                echo 'Hello World'

            }

        }

        

        stage('build') 

        {

            steps 

            {

                echo 'build'

            }

        }

        

       stage('test') 

       {

            steps 

            {

                echo 'test..'

            }

        }

 

        stage('deploy') 

           {

            steps 

            {

                echo 'deploy..'

            }

          }

          stage('LS') 

           {

            steps 

            {

                bat 'dir'

            }

          }

    }

}