pipeline {

    agent any

 

    stages 

    {

        stage('Hello') 

        {

            steps 
            {
                echo "Hi"
            }

            steps 

            {

                bat 'docker-compose up --build -d'

            }

        }

        

       


    }

}