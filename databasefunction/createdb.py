'''
                                        Create moule will help you to create a new database and collection or create new collection with in existing database

                                Class Create:
                                             constructor:
                                                        ***self.client   client is connection object recive by providing URI (go to setupuconnection module for more information)

                                            member function:
                                                          create_database(self):
                                                                             create database if name of database is not present in the cluster


                                                           create_collection(self):
                                                                                  create collection
                                                                                                 ask user for input NEW(to create new database and new collection within) EXISTING(create collection in existing database)

                                                                                                 CAUTION!  if you not input any database and collecton is not created








  '''





class create:
    def __init__(self,client):
        self.client=client



    def create_database(self): #body of function start from here
        try:
            print('\n')
            print(' \t Enter the database name here______________')

            database_name=input() # Asking for name of database

            while(database_name in self.client.list_database_names() ): #if name of database exist ask  again for input with alert database exist
                print('\n')
                print('database exist please! try another name ')

                return self.create_database() #returning back to start of function body

            print('\n')
            print(' \t Please! enter database name again _______')

            database_name_again=input()  #Asking again for input of database name which you type above (for checking to fix name )

            while(database_name != database_name_again   ): # checking weather name is same or not
                print('\n')
                print('\t you write it worong')
                database_name_again=input() #asking again for input

                continue #continue loop again for checking name of database

            print('\n')

            print('You are in the world of data and you call this world {}  Impresive! Budy '.format(database_name))

            print('\n')
            return self.client[database_name_again] #returning database

        except Exception as ex: #for Exception
                print('***************************')
                print(ex)
                print('****************************')






    def create_collection(self): #starting body of function

          try:

              print('\t Creation of collection in new database or in EXISTING database')
              print('\n')
              print('Enter NEW or EXISTING')

              user_input=input() #user input for NEW and EXISTING

              if(user_input == 'NEW'): #if user wants new database

                  databaseobj=self.create_database() # calling create_database function from Create class for more information check documentation

                  print('\t Please Enter collection(table) name')
                  print('\n')
                  collection_name=input() #user input for collection name



                  return databaseobj[collection_name]

              elif(user_input == 'EXISTING'): #user want Existing database for new collection_name
                  print('\n')
                  print('\t Please enter Existing database name')
                  database_name=input() #for user input database name

                  while((database_name in self.client.list_database_names()) == False): #checking weather database exist or not  if exist ask again for input

                      print('\t you write it wrong ')
                      print('\t Given database does not exist ')
                      print('\t TRY AGAIN')

                      database_name=input() #again asking for input

                      continue #coontinue to while loop

                  database=self.client[database_name] #selecting database for collection_name

                  print('Enter collection name')
                  collection_name=input() #user input for name of collection

                  while((collection_name in database.list_collection_names()) == True): #checking weather collection exist or not if exist ask agin for name

                      print('Collection Exist in Database ')
                      print('Try AGAIN')
                      collection_name=input() #asking agin for user_input

                      continue #continue to while loop

                  collectionobj=database[collection_name] # creating collection
                  print('\n')
                  print('You are in the world of data and you call this world {} database --- {} collection Impresive! Budy '.format(database_name,collection_name))

                  return collectionobj #returning collection

              else: #if its not from NEW or EXISTING
                  print('\n')
                  print('Please Enter right value ')

                  return self.create_collection()



          except Exception as ex:

            print('**************************')
            print(ex)
            print('***************************')
