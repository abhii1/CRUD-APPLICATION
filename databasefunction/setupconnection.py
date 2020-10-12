''' I have used MangoDB atlas for the project you can use any database for the connection
------------------------------------------------------------------------------------------
    *for MangoDB connection with python required following criteria:

***************************************************************************steps
       1__ you need a account on https://www.mongodb.com/cloud/atlas(you can get free account)
       2__ Create a cluster in MangoDB atlas
       3__ create user and password and provide ip addresses
       4__ click on connection tab in cluster and click on connect your application
       5__ select driver(use python ) and version(3.11 or later)
       6__ copy  your connection string into your application code we need it later
----------------------------------------------------------------------------------------------
   ** you need to install pymongo for connection in python
    ==== steps to install pymongo ===
    1__ pip install pymongo or pip install pymongo[srv]
    for documention go through:
        https://pypi.org/project/pymongo/

    '''

## Establish a connection betwwen database and python
## Establish a connection betwwen database and python

import pymongo  #importing pymongo for database connection and operation

class connection:
    def setup_connection(self):
        import pymongo

        print('\n')

        print('Please Enter URL__________________||') #user input of URL for connection
        #how to get URI in MongoDB Atlas is mention above

        print('\n')
        print('URL = ',end='')

        connection_url=input()  #user input for connection
        print('\n')
        try:
            client=pymongo.MongoClient(connection_url)    #MongoClient is use for connection with database cluster

            print('Feel yourself comfortable we are making thing ready _____________________________')
            print('\n')
            print('\t Loading..............................................')
            print('\t Fetching User name..............................................')
            print('\t Checking Password ..............................................')
            print('\n')
            print('WHOO HOOO CONNECTED')
            print('\n')

            client.server_info() # trigger exception if cannot connect the database
        except Exception as ex:


            print('**************************')
            print(ex)
            print('****************************')
            print('ERROR - can not connect to cluster')
            print('Please try another chance or check URL or check internet connection ')


        print('--------------------------------------------')
        print('\n')
        print('\t GREAT things take time')
        print('\t Appreciate your patience')
        print('\n')


        return client
