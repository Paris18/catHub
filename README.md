# catHub
&nbsp;&nbsp;&nbsp;This is the application to maintain the product catelogue ,each product is categoried by the groups.

# Installation and Execution
#### Basic Requirements

	Python 3
	Virtualenv

#### step 1: create environment with virtualenv

#### step 2: install the requirements with requirements.txt file located in project folder

       pip install -r requirements.txt
       
#### step 3: Create migration file with makemigration command

      python manage.py makemigrations

#### step 4:apply the migrations to db with migrate command
    
     python manage.py migrate
     
#### step 5:run the application

     python manage.py runserver
 
## api's Request and response
#### Create new Group. 

	curl -X POST \
	  http://127.0.0.1:8000/api/v1/groups/addgroup/ \
	  -H 'Content-Type: application/json' \
	  -d '{
		"name":"Groupn"
	}'

	Response:
	{
	    "id": "d7f4e846-04a2-4d53-a2fb-c9a6333a4e51",
	    "created_at": "2019-12-15T17:39:49.594519Z",
	    "is_active": true,
	    "updated_at": "2019-12-15T17:39:49.594581Z",
	    "name": "Groupn",
	    "description": ""
	}

#### List the Groups.

	curl -X GET \
	  http://127.0.0.1:8000/api/v1/groups/grouplist/ \
	  -H 'Content-Type: application/json'

	Response:

	{
	    "count": 6,
	    "next": "http://127.0.0.1:8000/api/v1/groups/grouplist/?page=2",
	    "previous": null,
	    "results": [
	        {
	            "id": "4e955437-5f6f-4d4b-84d7-dc5172689c78",
	            "created_at": "2019-12-15T16:23:18.527637Z",
	            "is_active": true,
	            "updated_at": "2019-12-15T20:37:13.561166Z",
	            "name": "Group01",
	            "description": ""
	        },
	        .
	        .
	        .
	        ]
	}

#### Update the group on group_id.

	curl -X PUT \
	  http://127.0.0.1:8000/api/v1/groups/updategroup/ \
	  -H 'Content-Type: application/json' \
	  -d '{
	            "id": "4e955437-5f6f-4d4b-84d7-dc5172689c78",
	            "name": "Group01"
	        }'

	Response:
	 {
	    "id": "4e955437-5f6f-4d4b-84d7-dc5172689c78",
	    "name": "Group01",
	    "description": "",
	    "is_active": true
	 }

#### Delete the Group given group_id.

	curl -X DELETE \
	  'http://127.0.0.1:8000/api/v1/groups/deletegroup/?id=d7f4e846-04a2-4d53-a2fb-c9a6333a4e51' \
	  -H 'Content-Type: application/json'

	Response:
	 {
    	"status": "group has been deactivated"
	 }

	 Note: if given group is not exists then it will response an Bad Request.

#### Create the Product.

	curl -X POST \
	  http://127.0.0.1:8000/api/v1/products/addproduct/ \
	  -H 'Content-Type: application/json'
	  -d '{
		"name":"product3",
		"group":"Group4",
		"price":300
		}'

	Response:
	 {
	    "id": "4c44959a-442c-4479-914f-c9be93691e37",
	    "created_at": "2019-12-15T20:59:31.280306Z",
	    "group": "Group5",
	    "is_active": true,
	    "updated_at": "2019-12-15T20:59:31.280500Z",
	    "name": "product3",
	    "description": "",
	    "price": 300
	 }

	 Note:If given group is not exist then it will create the new group.

#### List the Product list.
	
	curl -X GET \
	  http://127.0.0.1:8000/api/v1/products/productlist/ \
	  -H 'Content-Type: application/json' 

	Response:

	{
    "count": 7,
    "next": "http://127.0.0.1:8000/api/v1/products/productlist/?page=2",
    "previous": null,
    "results": [
        {
            "id": "b268469a-7808-427a-b18b-9de419134a6a",
            "created_at": "2019-12-15T16:36:22.501134Z",
            "group": "Group01",
            "is_active": false,
            "updated_at": "2019-12-15T17:36:05.535619Z",
            "name": "product1",
            "description": "",
            "price": 100
        },
        .
        .
        .
    	]
    }

#### Update the Price and group of given product.

	curl -X PUT \
	  http://127.0.0.1:8000/api/v1/products/updateproduct/ \
	  -H 'Content-Type: application/json' \
	  -d ' {
	    "id": "a5804420-ae7e-4edd-b152-94a1d5d8d5c3",
		"price":600
		}'

	Response: Updated Price
	 {
	    "id": "a5804420-ae7e-4edd-b152-94a1d5d8d5c3",
	    "name": "product1",
	    "description": "",
	    "price": 600,
	    "is_active": true,
	    "group": "Group2"
	 }

	Update the Group of the product

	curl -X PUT \
	  http://127.0.0.1:8000/api/v1/products/updateproduct/ \
	  -H 'Content-Type: application/json' \
	  -d ' {
	    "id": "a5804420-ae7e-4edd-b152-94a1d5d8d5c3",
		"group":"Group5"
		}'

	Response:

	{
	    "id": "a5804420-ae7e-4edd-b152-94a1d5d8d5c3",
	    "name": "product1",
	    "description": "",
	    "price": 600,
	    "is_active": true,
	    "group": "Group5"
	}

	Note:We can update the price and group at same time,as group and product name are unique together so while updating need to follow otherwise it will response an Bad Request.

#### Deactivate the product of id given

	curl -X DELETE \
	  'http://127.0.0.1:8000/api/v1/products/deleteproduct/?id=b268469a-7808-427a-b18b-9de419134a6a' \
	  -H 'Content-Type: application/json'

	Response:
	 {
    	"status": "product has been deactivated"
	 }

	 Note: if given product is not exists then it will response an Bad Request.

#### Product groupwise analysis report.

	curl -X GET \
	  http://127.0.0.1:8000/api/v1/products/groupanalysis/ \
	  -H 'Content-Type: application/json'

	Response:
	 [
	    {
	        "group__name": "Group4",
	        "group_count": 1,
	        "group_value": 300
	    },
	    .
	    .
     ]
