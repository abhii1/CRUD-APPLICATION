'''

                   Cluster module is used for printing the all the usefull informaton about Cluster and Collection present in database

class clusterinformation( no parameter ) -- conatains all the function

                               Functions:
                                        print_select_list_of_databases(client)
                                                     ** client is connection object recive by providing URI (go to setupuconnection module for more information)
                                                     it will print all the present database in the cluster caution !
                                                     if you created cluster and do not entered any data in database collection then those database
                                                     will not be in cluster

                                                     it will also use select database from the list of databases and return database

                                      print_select_list_of_collection(client):
                                                     ** client is connection object recive by providing URI (go to setupuconnection module for more information)
                                                     it will print all the collecton present in the selected database
                                                     return selected collection



                                     print_list_of_databases_with_collection(client)
                                                          **** client is connection object recive by providing URI (go to setupuconnection module for more information)


                                                          function print all database and collection with in





'''



class clusterinformation():

    def __init__(self,client):
        self.client=client


    # function wiith client as parameter for client go to setupconnection module
    def print_select_list_of_databases(self):

        #printing and select database
        for name in self.client.list_database_names(): #printing all the database present in cluster
            print(name,end=' ')
            print('|__',end=' ')

        print('\n')
        print('Please select any Database from above list ')
        print('\n')
        select_database=input()  #taking input for database connection

        if( select_database in self.client.list_database_names() ): #if user input database and it is present in list of database then it return the object

             selected_database=self.client[select_database]
             print('You have selected {} database from cluster'.format(select_database)) #printing selected database


             return selected_database
        else: #if database name is not present then it will warn you with case senstive or not present

            print('Case Senstive or database not present')
            print('\n')
            print('Do you want to try again !')
            print('\n')
            print('yes or (no will exit you from app) ')
            print('\n')
            print('! case senstive other input will cause you out of app')
            print('\n')
            print('   ! CAUTION   '*4 )
            user_input=input()
            if(user_input == 'yes'): #if yes again back to fuction starting part

                return self.print_select_list_of_databases()

            else: #out of app
                print('\n')
                print('exiting from app bye buddy')






    def print_select_list_of_collection(self): #function body from here

        selected_database=self.print_select_list_of_databases()


        for collection_name in selected_database.list_collection_names():# printing all the collection name in a database
            print('\n')
            print('list of collection name.......|')
            print("\t"+collection_name,end=' ')
            print('|',end=' ')


        print('\n')
        print("Please Enter collection(table) from above list ___")
        print('\n')

        selected_collection=input() #user input for slection of collection
        print('\n')
        if(selected_collection in selected_database.list_collection_names()): #if collection present return collection object

            return selected_database[selected_collection]


        else:

            print('Case senstive or  collection not present ')
            print('\n')
            print('Do you want to try again !')
            print('\n')
            print('yes will again ask for database selection  or no will exit you from app')
            print('\n')
            print('! case senstive other input will cause you out of app')
            print('\n')
            print('   ! CAUTION   '*4 )
            user_input=input() #user input asking for yes or no
            if(user_input == 'yes'):

                return self.print_select_list_of_collection() #go starting of function body

            else:

                exit()






    def print_list_of_databases_with_collection(self): # staring of Function

        for database_name in self.client.list_database_names():
            #printing all database name in cluster
            print("Database - ",database_name)

            for collection_name in self.client.get_database(database_name).list_collection_names():
                #print all collection within database

                print('\t',end=' ')
                print(collection_name)

            print('---------------------------------------')
