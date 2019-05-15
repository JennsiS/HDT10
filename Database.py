"""
Class Database will be util to make conection with Neo4J 
Project Generator
Universidad del Valle de Guatemala
Saul Contreras
Michele Benvenuto
Jennifer Sandoval
"""

from neo4j import GraphDatabase, basic_auth

class Database(object):

    """Set database driver"""
    def __init__(self, uri,user,password):
        self._driver = GraphDatabase.driver(uri, auth=(user, password))        

    """Close database"""
    def close(self):
        self._driver.close()

    """
    This method is used to write a node in database and receives 3 arguments:
    _id: is the identifier that you want to be saved on database, should be an string without spaces
    nodeType: Is the type of node that you want, it must be a String, its first letter must be Uppercase
    arguments: It containds the atributes of the node. It must be a dictionary where the key is the name of the atribute and the value must be the value of the atribute"""
    def write(self,_id,nodeType,arguments):
        result = ""
        argumentsList = []
        if(nodeType!=None):
            result = result + "CREATE (" + _id + ":" + nodeType + ")\n"
            counter = 0
            for variable in arguments:
                argumentsList.append(arguments[variable])
                result = result + "SET " +  _id + "." + variable + " = $arguments[" + str(counter)  + "]\n"
                counter = counter+1
        with self._driver.session() as session:
            session.write_transaction(self._create,argumentsList,result)

    """
    This method is used to make a conection between two nodes and receives 7 parameters:
    type1 and type2: Type of node 1 and 2 and must be an string, its first letter must be Uppercase      
    VariableName1 and VariableName2: It has the name of the key to be checked of the nodes. It must be a string withoud spaces
    variable1  and variable2: contains the value of the Variables setted above, must be a string
    linkName: it has the name that will have the link. Must be an string without spaces.""" 
    def link(self,type1,type2,variableName1,variable1,VariableName2,variable2,linkName):
        result = "MATCH (a:" + type1 + "),(b:" + type2 + ")\nWHERE a." + variableName1 + "= $variable1 AND b."+ VariableName2 + "= $variable2\nCREATE (a)-[:"+linkName+"]->(b)"
        with self._driver.session() as session: 
            session.write_transaction(self._connect,result,variable1,variable2)
    
    """
    This method is for delete an specific node it has 3 parameters
    nodeType: it receives the type of node you want to delete, must be an string and its first letter must be uppercase
    key: it receives a key or a reference that the node has. 
    value: it recives de value of the reference key."""
    def delete(self,nodeType,key,value):
        result = "MATCH (a:" + nodeType + ")\nWHERE a." + key + "= $value\nDETACH DELETE (a)"
        with self._driver.session() as session: 
            session.write_transaction(self._delete,result,value)

    """
    This method is for delete a relationship between nodes it has 7 parameters
    type1 and type2: Type of node 1 and 2 and must be an string, its first letter must be Uppercase      
    VariableName1 and VariableName2: It has the name of the key to be checked of the nodes. It must be a string withoud spaces
    variable1  and variable2: contains the value of the Variables setted above, must be a string
    linkName: it has the name that will be deleted. Must be an string without spaces.""" 
    def deleteLink(self,type1,type2,variableName1,variable1,VariableName2,variable2,linkName):
        result = "MATCH (a:" + type1 + "),(b:" + type2 + ")\nWHERE a." + variableName1 + "= $variable1 AND b."+ VariableName2 + "= $variable2\nMATCH (a)-[r:"+linkName+"]->(b)\nDELETE r"
        with self._driver.session() as session: 
            session.write_transaction(self._deleteLink,result,variable1,variable2)

    """
    This method is for upgrade an specific atribute on a node it has 3 parameters
    nodeType: it receives the type of node you want to upgrade, must be an string and its first letter must be uppercase
    key: it receives a key or a reference that the node has. 
    value: it recives de value of the reference key.
    newValue: it recieves de value that will be setted"""
    def upgrade(self,nodeType,key,value,newValue):
        result = "MATCH (a:" + nodeType + ")\nWHERE a." + key + "= $value\nSET a." + key + "= $newValue"
        with self._driver.session() as session: 
            session.write_transaction(self._upgrade,result,value,newValue)

    """
    This method is used to get a node it has three parameters
    nodeType: it receives the type of node where you want to get information, must be an string and its first letter must be uppercase
    key: it receives a key or a reference that the node has. 
    value: it recives de value of the reference key.
    It will return a StatementResult type, that behaives like a java-map, you have to make an iterator to get informations"""
    def getNode(self,nodeType,key,value):
        result = "MATCH (a:" + nodeType + ")\nWHERE a." + key + "=$value\nRETURN a"
        with self._driver.session() as session: 
            return session.write_transaction(self._getNode,result,value)        

    """This method is useful to get all nodes that are connected by the same link to a node m connected with the same link to a node of reference
    nodeType: it receives the type of node of reference, must be an string and its first letter must be uppercase
    key: it receives a key or a reference that the node has. 
    value: it recives de value of the reference key.
    link: receives the link name, must be a string without spaces
    """
    def getNodesByOther(self,nodeType,key,value,link):
        result= "MATCH (a:" + nodeType + ")\nWHERE a." + key + "=$value\nMATCH (a)-[:" + link + "]->(m)<-[:" + link + "]-(r)\nRETURN r"
        with self._driver.session() as session: 
            return session.write_transaction(self._getNodes,result,value)

    """This method is useful to get all nodes connect to one of reference with an specific link
    nodeType: it receives the type of node of reference, must be an string and its first letter must be uppercase
    key: it receives a key or a reference that the node has. 
    value: it recives de value of the reference key.
    link: receives the link name, must be a string without spaces"""
    def getNodesByLink(self,nodeType,key,value,link):
        result= "MATCH (a:" + nodeType + ")\nWHERE a." + key + "=$value\nMATCH (a)-[:" + link + "]->(m)\nRETURN m"
        with self._driver.session() as session: 
            return session.write_transaction(self._getNodes,result,value)

    """This method is used two now if there ara nodes on the database.
    It will return None the database is empty"""
    def getDefault(self):
        result = "MATCH (n) return n"
        with self._driver.session() as session: 
            resultado = session.write_transaction(self._Default,result)        
            return resultado

    """This method is used two set the default database, you should change the string result two change it. The cod must be in Cypher"""
    def setDefault(self):
        if (self.getDefault().single()==None):#We check if the database is empty
            result = """
            CREATE (ProjectGenerator:Project {title: "Project Generator",description:"This project is about the creation of a software to generate projects. You need to know how to code.", time:11, complexity:"medium", integrants:2 })
            CREATE (SunRotation:Project {title: "Sun Rotation",description:"Calculate the angular velocity of the sun, coding", time:7, complexity:"low", integrants:3 })
            CREATE (Behaviorism:Project {title: "Behaviorism",description:"Experiment with people and theory of behaviorism", time:210, complexity:"easy", integrants:1})
            CREATE (Gestalt:Project {title: "Gestalt",description:"Experiment to avoid extintion", time:2102400000, complexity:"hard", integrants:55})
            CREATE (Avengers:Project {title: "Avengers",description:"Social experiment where a superhero is near of you", time:210, complexity:"hard", integrants:5})
            CREATE (CACAP:Project {title: "CACAP",description:"Centro de Administracion y Control Automatico de Papel", time:210, complexity:"hard", integrants:5})
            CREATE (Computer:Resource {title: "Computer", specifications: "A computer with an ide to code"})
            CREATE (Fruit:Resource {title: "fruit", specifications: "A fresh fruit"})
            CREATE (Vegetable:Resource {title: "vegetable", specifications: "A fresh vegetable"})
            CREATE (Subjects:Resource {title: "subjects", specifications: "Humans for investigation"})
            CREATE (Custom:Resource {title: "custom", specifications: "a custom or suit"})
            CREATE (Raspberry:Resource {title: "raspberry", specifications: "a mini-computer with raspberry"})
            CREATE (DataStructure:Course {title: "Data Structure",Departament: "Computer Science"})
            CREATE (Physics2:Course {title: "Physics 2",Departament: "Physics"})
            CREATE (Psicology:Course {title: "Basic psicology",Departament:"Psicology"})
            CREATE (Humanity:Course {title: "Humanity Sciences",Departament:"Social studies"})
            CREATE (Code:Course {title: "Basic coding",Departament:"Computer Sciences"})
            CREATE (User:User {name: "Default",password: "password"})
            
            CREATE
                (User)-[:HAS_DONE]->(ProjectGenerator),
                (User)-[:HAS_DONE]->(Gestalt),
                (User)-[:HAS_LIKED]->(SunRotation),
                (User)-[:HAS_LIKED]->(ProjectGenerator),
                (User)-[:HAS_VIEWED]->(Gestalt),
                (User)-[:HAS_VIEWED]->(CACAP),
                (User)-[:HAS_VIEWED]->(ProjectGenerator),
                (User)-[:HAS_VIEWED]->(SunRotation), 
                (ProjectGenerator)-[:PROJECT_FOR]->(DataStructure),
                (SunRotation)-[:PROJECT_FOR]->(Physics2),
                (SunRotation)-[:PROJECT_FOR]->(DataStructure),
                (SunRotation)-[:PROJECT_FOR]->(Code),
                (Gestalt)-[:USE_A]->(Computer),
                (Gestalt)-[:PROJECT_FOR]->(Humanity),
                (SunRotation)-[:USE_A]->(Computer),
                (Gestalt)-[:USE_A]->(Subjects),
                (ProjectGenerator)-[:USE_A]->(Computer),
                (Behaviorism)-[:PROJECT_FOR]->(Psicology),
                (Behaviorism)-[:USE_A]->(Vegetable),
                (Behaviorism)-[:USE_A]->(Fruit),
                (Behaviorism)-[:USE_A]->(Subjects),
                (Avengers)-[:USE_A]->(Subjects),
                (Avengers)-[:PROJECT_FOR]->(Psicology),
                (Avengers)-[:USE_A]->(Custom),
                (CACAP)-[:USE_A]->(Raspberry),
                (CACAP)-[:PROJECT_FOR]->(Code)"""
            with self._driver.session() as session: 
                return session.write_transaction(self._Default,result)
            
            def getRecomendations(self,user,especialidad):
		recomendations = []
		firstNodes = self.db.getNodesByLink("User","name",user,especialidad)
		for node in firstNodes:
			nodeResources = self.db.getNodesByLink("Hospital","title",node[0]["title"],"is_friend_with")         #Get resources of the project
			resources = []
			for resource in nodeResources:
				resources.append(Resource(resource[0]["title"],resource[0]["specifications"]))
			topicOfProject = self.db.getNodesByLink("Project","title",node[0]["title"],"PROJECT_FOR")	 #Get topic of the project
			topic = []
			for top in topicOfProject:
				topic.append(Topic(top[0]["title"],resource[0]["Departament"]))
			currentProject = Project(node[0]["title"],node[0]["description"],"id",resources,topic)       #Instantiate a Project with the DATA
			ADDNODE = True  #This variable will help us two take add the node, if it is false is pecause it is already in recomendations
			for allRecomendation in recomendations:
				if(allRecomendation.compare(currentProject)): #If the project is already recommended
					ADDNODE = False
					allRecomendation.value = allRecomendation.value + 25          #Relation project - 10
			if(ADDNODE):                                     #If the project is not already recommended
				relation = Relation(currentProject,25)		 #The relation will be Project - 10
				recomendations.append(relation)
		for recomedation in recomendations:                                                             #For each project that the user has viewed we will get some other projects based on resources
			ProjectsBasedOnTopic = self.db.getNodesByOther("Project","title",recomedation.project.title,"PROJECT_FOR")
			for node in ProjectsBasedOnTopic:
				nodeResources = self.db.getNodesByLink("Project","title",node[0]["title"],"USE_A")         #Get resources of the project
				resources = []
				for resource in nodeResources:
					resources.append(Resource(resource[0]["title"],resource[0]["specifications"]))
				topicOfProject = self.db.getNodesByLink("Project","title",node[0]["title"],"PROJECT_FOR")	 #Get topic of the project
				topic = []
				for top in topicOfProject:
					topic.append(Topic(top[0]["title"],resource[0]["Departament"]))
				currentProject = Project(node[0]["title"],node[0]["description"],"id",resources,topic)       #Instantiate a Project with the DATA
				ADDNODE = True  #This variable will help us two take add the node, if it is false is pecause it is already in recomendations
				for allRecomendation in recomendations:
					if(allRecomendation.compare(currentProject)): #If the project is already recommended
						ADDNODE = False
						allRecomendation.value = allRecomendation.value + 10          #Relation project - 10
				if(ADDNODE):                                     #If the project is not already recommended
					relation = Relation(currentProject,10)		 #The relation will be Project - 10
					recomendations.append(relation)
		for recomedation in recomendations:                                                             #For each project that the user has viewed we will get some other projects based on resources
			ProjectsBasedOnResource = self.db.getNodesByOther("Project","title",recomedation.project.title,"USE_A")
			for node in ProjectsBasedOnResource:
				nodeResources = self.db.getNodesByLink("Project","title",node[0]["title"],"USE_A")         #Get resources of the project
				resources = []
				for resource in nodeResources:
					resources.append(Resource(resource[0]["title"],resource[0]["specifications"]))
				topicOfProject = self.db.getNodesByLink("Project","title",node[0]["title"],"PROJECT_FOR")	 #Get topic of the project
				topic = []
				for top in topicOfProject:
					topic.append(Topic(top[0]["title"],resource[0]["Departament"]))
				currentProject = Project(node[0]["title"],node[0]["description"],"id",resources,topic)       #Instantiate a Project with the DATA
				ADDNODE = True  #This variable will help us two take add the node, if it is false is pecause it is already in recomendations
				for allRecomendation in recomendations:
					if(allRecomendation.compare(currentProject)): #If the project is already recommended
						ADDNODE = False
						allRecomendation.value = allRecomendation.value + 5          #Relation project - 5
				if(ADDNODE):                                     #If the project is not already recommended
					relation = Relation(currentProject,5)		 #The relation will be Project - 5
					recomendations.append(relation)	
		recomendations = self.sort(recomendations)
		toReturn = []
		for recomedation in recomendations:                                                             #For each project that the user has viewed we will get some other projects based on resources
			toReturn.append(recomedation.project.title)
		return toReturn         
   

  def getProject(self,key,value):
        return self.db.getNode("Hospital",key,value)	

  def sort(self,recomendationsList):
		recomendations=recomendationsList
		toReturn = []
		while(len(recomendations)!=0):
			highter = recomendations[0]
			for node in recomendations:
				if(node.value>highter.value):
					highter = node
			recomendations.remove(highter)
			toReturn.append(highter)
		return toReturn

    @staticmethod
    def _Default(tx,result):
        return tx.run(result)

    @staticmethod
    def _getNodes(tx,result,value):
        return tx.run(result,value=value)

    @staticmethod
    def _getNode(tx,result,value):
        return tx.run(result,value=value)

    @staticmethod
    def _upgrade(tx,result,value,newValue):
        result = tx.run(result,value=value,newValue=newValue)

    @staticmethod
    def _deleteLink(tx,result,variable1,variable2):
        result = tx.run(result,variable1=variable1,variable2=variable2) 

    @staticmethod
    def _delete(tx,result,value):
        result = tx.run(result,value=value)            

    @staticmethod
    def _connect(tx,result,variable1,variable2):
        result = tx.run(result,variable1=variable1,variable2=variable2) 

    """This method is used by write"""
    @staticmethod
    def _create(tx,arguments,result):
result = tx.run(result,arguments=arguments)
