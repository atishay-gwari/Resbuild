pipeline {

    agent any

 

    stages 

    {
        stage('Github') 

        {

            steps 

            {
                
                sh "git clone https://github.com/atishay-gwari/Resbuild.git"

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