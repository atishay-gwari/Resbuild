pipeline {

    agent any

 

    stages 

    {
        stage('LS') 

        {

            steps 

            {
                
                sh "ls"

            }

        }




        stage('Docker') 

        {

            steps 

            {
                
                sh "docker-compose up --build"

            }

        }


     

 

        

    }

}