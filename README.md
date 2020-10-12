# CRUD APP

>Application help user to create ,read ,delete and update data in database with choice of action in the python command line 

Application will ask user to enter there connection String in the command line interface to connect with the desired cluster in MangoDB Atlas. **Connection string** will help user to choose any database in cluster and help the user to create new database and collection or collection within existing database . After connection a selection of database user can perform **CRUD operation the database through selected API end point** .


## Table of contents


* [Link](#Link)
* [Features](#Features)
* [Installation](#screenshots)
* [Quickstart](#Quickstart)
* [Languages_and_API](#Languages_and_API)
* [End_point](#End_point)
* [Contact](#contact)
* [License](#License)


## Link

<img src="https://avatars1.githubusercontent.com/u/9919?s=200&v=4" width="42" height="42">

- [X] GitHub : https://github.com/abhii1/CRUD-APP



## Features


- [X] User can easily connect to the MongoDb atlas just with one step .User only need connection string of pymongo to connect with cluster .


- [X] User can check database name and collection(table) exist in database


<img src="https://user-images.githubusercontent.com/49953175/95673653-29591200-0bc8-11eb-9ec8-02fb9f2d0b07.PNG" >



- [X] User can create new database and collection in the database 


<img src="https://user-images.githubusercontent.com/49953175/95673770-6ffb3c00-0bc9-11eb-8c2c-fdade20dc2f7.gif" >


- [X] User can create new collection in existing database 


<img src="https://user-images.githubusercontent.com/49953175/95673915-4ee71b00-0bca-11eb-8554-5af63bd3ba30.gif" >

- [X] User can select existing database and collection(table)

<img src="https://user-images.githubusercontent.com/49953175/95674035-31668100-0bcb-11eb-964e-b3694452b255.gif" >


- [X] User can put data through end point mention in [End_points](#End_points).

- [X] User can update data by id or any columns in selected database .

- [X] User can delete data by id or any column in selected database .

- [X] User can get data by any column except id.


## Installation

>  **download repo  and Need docker in the system **

     
     
```

docker build -t crudapp(or any name):latest .

#you should be in same directory as Dockerfile exits 

```



## Quickstart

>AFTER INSTALLATION USER NEED TO RUN THIS COMMAND IN COMMAND PROMPT OR POWERSHELL

```
docker run -it crudapp(or name you have created)

```




**PUT data to database with simple steps**
  

<img src="https://user-images.githubusercontent.com/49953175/95742293-61865080-0cad-11eb-8ecd-83badd0a210d.gif" >


**GET data from the selected database ,filter can be any column except _id**

>first user need to select database and collection or create new database and collection



<img src="https://user-images.githubusercontent.com/49953175/95743894-19b4f880-0cb0-11eb-96b0-ced545e85a29.gif" >


**Update data in database with _id as filter**

> you can choose which column or field to update in database for first enter _id and field name you want to update 



<img src="https://user-images.githubusercontent.com/49953175/95744370-cd1ded00-0cb0-11eb-8a34-55530cc33138.gif" >



**Search by any filter for example name and update selected field**

>user need to enter filter by (name,offer_price etc) then field want ot update and it will delete first document 



<img src="https://user-images.githubusercontent.com/49953175/95744913-ce034e80-0cb1-11eb-83e1-6c0a74e18c7c.gif" >


**Delete user by _id**

>user can delete data from database from selected database by searching through _id

<img src="https://user-images.githubusercontent.com/49953175/95745492-cf814680-0cb2-11eb-8c5a-e6387124959f.gif" >


**delete user by filter**

>user can choose through which they want to search in database and delete first document of the retrive data


<img src="https://user-images.githubusercontent.com/49953175/95745682-24bd5800-0cb3-11eb-8b47-b81c1a9eab40.gif" >


                           

## Languages_and_API


<img src="https://miro.medium.com/max/2496/1*uYcRdZDho2AicwI9k84kpw.jpeg">



<img src="https://files.realpython.com/media/flask.3aee85149243.png">








## End_point

```
#PUT DATA 
   
localhost/PUT_DATA

#user need to enter the column name and value in the body>form-data

   ```
   
```
#GET DATA 

localhost/GET_DATA/<column>

#in place select desire column name 

```

```
#update by id 

localhost//Update/<id>/<update_column>

#user need to select id and then column to update and value of updated field in body>>form-data


```

```
#update by filter 

localhost/Update/by/<filter_except_id>/<update_column>

#user need to select filter and column to update in filter_except_id and update_column



```

```
delete by id

localhost/DELETE/<id>

#user specify id 


```

```
#Delete ALL data retrive from column

localhost/Update/ALL/by/<filter_except_id>/<update_column>


# user need to specify <filter_except_id>/<update_column>

```


## Contact


Created by Abhishek pratap singh

[<img src="https://cdns.iconmonstr.com/wp-content/assets/preview/2012/240/iconmonstr-linkedin-3.png" width="42" height="42">](https://www.linkedin.com/in/abhishek-pratap-singh-44a96816b/)

[<img src="https://9to5google.com/wp-content/uploads/sites/4/2016/08/gmail-logo.png?w=1280" width="42" height="42">](abhisheklumiamicro@gmail.com)


## License

This package is distributed under the `MIT license`.
