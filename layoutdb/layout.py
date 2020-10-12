'''
Its is a layout of app means how should app page look like and features added to its some feature are



        hello Buddy your connection is setup with your database(your world)



                       Some functionality of app are:
                                            case_1: Want to check all list of database and collection
                                            case_2:Want to create a database and collection
                                            case_3:Want to select Existing database
                                            case_4:Exit from app


'''


from databasefunction import setupconnection , commanprint ,cluster, createdb #importing all desireable module  for more information check module or documentaion

def layout_print(): #start

    commanprint.comman().main_app() #print a comman text for more check databasefunction >> commanprint

    client=setupconnection.connection().setup_connection() # setupconnection with the database for more information databasefunction >> setupconnection

    commanprint.comman().main_app() ##print a comman text for more check databasefunction >> commanprint

    print('Enter the case number from above list ')

    print('\n')
    print('Case__ ',end='')

    user_input=input() #user input for selection for one of features

    if(user_input=='1'):

        cluster.clusterinformation(client).print_list_of_databases_with_collection() #listing all database and collection name for more databasefunction >> cluster

        return layout_print() #returing to start of function body

    elif(user_input == '2'): # if case == 2

        createobj=createdb.create(client)

        collection=createobj.create_collection() #creating collection for more information databasefunction >> createdb

        print('\n')
        print('You have created collection ')

        return collection #returning the collection

    elif(user_input=='3'):

        clusterobj=cluster.clusterinformation(client)
        collection=clusterobj.print_select_list_of_collection() #selecting collection from existing database and collection for more databasefunction >> cluster

        return collection # returning collection

    elif(user_input=='4'):

        exit() # exit from application

    else:
        print('Accept any of these value ')
        layout_print() # again start if not valid input
