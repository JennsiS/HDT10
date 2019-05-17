# HDT10
To be able to use hospital. py you most do the following steps:

1) Visit https://neo4j.com/download/ and download Neo4J
2) After downloading Neo4J install the Neo4j Python Driver
	For windows:
		pip install neo4j
3)Open Neo4J desktop and create a new graph, set the name and password
	Check that the uri of the database is :bolt://localhost:7687
	
	1. Click Start
	2. Click Manage
	3. Click Open Browser
	4. Run :server connect in Neo4J Browser Shell
	5. URL should be bolt://localhost:7687

	If the URL is not bolt://localhost:7687

	1. Open the repository folder HDT10
	2. Go to Database.py
	3. Change first parameter in code line 16 with the URI of the graph
4. Create a new User

	1. On Neo4J browser shell run the following command :server user add
	2. Create a new user named 	"Default" with the following password "password", be sure that admin and editor roles are added to this user
5. Run hospital.py
	
	1. Open a new cmd window and go to the HDT10 folder
	2. Open HDT10
	3. write the following command python hospital.py	