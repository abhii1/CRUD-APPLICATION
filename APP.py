from flask import Flask,Response,request #importing flask for creation API

import json #importing json

from bson.objectid import ObjectId #for conversion of object id

from layoutdb import layout # importing layout for more information check layoutdb>>layout

collection=layout.layout_print() #taking collection variable

print('\n')

print(collection)

print('\n')


app=Flask(__name__) #creating app



@app.route('/GET_DATA/<column>',methods=["GET"]) #Url for GET DATA by offerprice

def get_some_data(column):

    #select get data by column for example offer price value name

    try:
        input={column:request.form[column]} #taking input as form

        datas=list(collection.find(input)) #converting into list

        for data in datas:
            data['_id']=str(data['_id']) #conversion of id

        response=Response(response=json.dumps(datas),
                            status=500,
                            mimetype='application/json')

        return response #returning response variable

    except Exception as ex: #if exception arise
        print(ex)
        response=Response(response=json.dumps({'messege':'can not find data '}),
                            status=500,
                            mimetype='application/json')
        return response #return can not find data




@app.route("/PUT_DATA",methods=["POST"]) # creating url route for API

def create_data():
    # you have write the value of all the unput  in Body >> form-datas
    #if not then error on postman

    try:
        input={'name':request.form['name'],
               'brand_name':request.form['brand_name'],
               'regular_price_value':request.form['regular_price_value'],
               'offer_price_value':request.form['offer_price_value'],
               'currency':request.form['currency'],
               'classification_l1':request.form['classification_l1'],
               'classification_l2':request.form['classification_l2'],
               'classification_l3':request.form['classification_l3'],
               'classification_l4':request.form['classification_l4'],
               'image_url':request.form['image_url'],
               }

        print(input)

        dbResponse=collection.insert_one(input) #inserting data

        response=Response(response=json.dumps({'messege':'data Entered','id':f"{dbResponse.inserted_id}"}),
                            status=200,
                            mimetype='application/json')

        return response #returing response
    except Exception as ex:
        print("**************************************")
        print(ex)
        print('*****************************************')




@app.route('/Update/<id>/<update_column>',methods=['PATCH']) #url route

def update_user(id,update_column):
    # select paticular id
    # update by update_column
    try:
        #taking response of the user

        dbResponse=collection.update_one(
        {"_id": ObjectId(id)},
        {"$set":{update_column:request.form[update_column]}}
        )

        #in body form of postman

        if( dbResponse.modified_count==1): #if there is any change in data from earlier state of collection
            response=Response(response=json.dumps({'messege':' updated '}),
                                status=500,
                                mimetype='application/json')
        return response


    except Exception as ex:
        print('******************')
        print(ex)
        print('*****************')
        response=Response(response=json.dumps({'messege':'update or you used previous value'}),
                            status=500,
                            mimetype='application/json')
        return response


@app.route('/Update/by/<filter_except_id>/<update_column>',methods=['PATCH']) #url route

def update_userby(filter_except_id,update_column):
    # select column through which you want to select
    # update by update_column
    try:
        #taking response of the user

        filter={filter_except_id:request.form[filter_except_id]}
        update={"$set":{update_column:request.form[update_column]}}

        dbResponse=collection.update_one(filter,update)

        #in body form of postman

        if( dbResponse.modified_count==1): #if there is any change in data from earlier state of collection
            response=Response(response=json.dumps({'messege':' updated ','filter':filter}),
                                status=500,
                                mimetype='application/json')
        return response


    except Exception as ex:
        print('******************')
        print(ex)
        print('*****************')
        response=Response(response=json.dumps({'messege':'sorry cannot update or you used previous value'}),
                            status=500,
                            mimetype='application/json')
        return response



@app.route('/Update/ALL/by/<filter_except_id>/<update_column>',methods=['PATCH']) #url route

def updateALL(filter_except_id,update_column):
    # select column by which you want to update
    # update by update_column
    try:
        #taking response of the user

        filter={filter_except_id:request.form[filter_except_id]}
        update={"$set":{update_column:request.form[update_column]}}

        dbResponse=collection.update_many(filter,update) #update ALL

        #in body form of postman

        if( dbResponse.modified_count==1):

             #if there is any change in data from earlier state of collection
            response=Response(response=json.dumps({'messege':' updated ','filter':filter}),
                                status=500,
                                mimetype='application/json')
            return response


    except Exception as ex:

        print('******************')
        print(ex)
        print('*****************')
        response=Response(response=json.dumps({'messege':'sorry cannot update or you used previous value'}),
                            status=500,
                            mimetype='application/json')
        return response


@app.route('/DELETE/<id>',methods=['DELETE']) #delete user by id

def deletedata(id):

    try:

        dbResponse=collection.delete_one({"_id":ObjectId(id)})

        if(dbResponse.deleted_count == 1):

            response=Response(response=json.dumps({'messege':' data deleted ','id':f"{id}"}),
                                status=200,
                                mimetype='application/json')

            return response


    except Exception as ex:

        print('*****************')
        print(ex)
        print('*******************')
        response=Response(response=json.dumps({'messege':'sorry cannot delete '}),
                            status=500,
                            mimetype='application/json')

        return response

@app.route('/DELETE/by/<column_except_id>',methods=['DELETE']) #delete user by column_except_id

def deletedata_withcolumn(column_except_id):

    try:
        input={column_except_id :request.form[column_except_id]}

        dbResponse=collection.delete_one(input)

        if(dbResponse.deleted_count == 1):

            response=Response(response=json.dumps({'messege':' data deleted ','delete_data':input}),
                                status=200,
                                mimetype='application/json')

            return response


    except Exception as ex:

        print('*****************')
        print(ex)
        print('*******************')
        response=Response(response=json.dumps({'messege':'sorry cannot delete '}),
                            status=500,
                            mimetype='application/json')

        return response


@app.route('/DELETE/ALL',methods=['DELETE']) #delete all data

def deleteall(column_except_id):

    try:


        dbResponse=collection.delete_many({})

        if(dbResponse.deleted_count == 1):


            response=Response(response=json.dumps({'messege':'ALL  data deleted ','delete_data':'all data'}),
                                status=200,
                                mimetype='application/json')

            return response


    except Exception as ex:

        print('*****************')
        print(ex)
        print('*******************')
        response=Response(response=json.dumps({'messege':'sorry cannot delete '}),
                            status=500,
                            mimetype='application/json')

        return response






if __name__ =='__main__':


    app.run()
