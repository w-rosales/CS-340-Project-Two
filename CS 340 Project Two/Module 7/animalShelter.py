from pymongo import MongoClient
from bson.objectid import ObjectId
from bson.json_util import dumps

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """
    
    def __init__(self, USER, PASS):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB data bases and collections.
        # This is hard-wired to use the aac database, the 
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        # 
        # Connection Variables
        #USER = 'aacuser'
        #PASS = 'SNHU'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 30524
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]
        
    # Complete this create method to implement the C in CRUD.
    def create(self, data):
        # Checks if data is not None
        if data is not None:
            try:
                # Inserts data into collection
                insert_result = self.collection.insert_one(data)
                # Returns true if data was added
                return insert_result.acknowledged
            except Exception as e:
                # Prints error message for failure
                print(f"Error inserting document: {e}")
                return False
        else: 
            # Raises exception if paramater is empty
            raise Exception("Nothing to save, because data paramter is empty")
                
    # Create method to implement the R in CRUD.
    def read(self, searchData):
        # Checks if searchData is provided
        if searchData:
            # Find documents mathcing with searchData
            data = self.database.animals.find(searchData, {})
        else:
            # Find all documents if no searchData is provided
            data = self.database.animals.find( {}, {})
        # Return the dataset else let the error flow up
        return data
    
    # Create method to implement the U in CRUD.
    def update(self, searchData, updateData):
        # Checks if searchData is not None
        if searchData is not None:
            try:
                # Update documents matching the searchData with updateData
                result = self.database.animals.update_many(searchData, {"$set": updateData })
                # Returns True if update was successful
                return result.acknowledged
            except Exception as e:
                # Prints error message if update fails
                print(f"Error updating documents: {e}")
                return False
        else:
            # Returns empty string if no searchData is provided
            return "{}"
        # Return the dataset else let the error flow up
        return result.raw_result
        
    # Create method to implement the D in CRUD/
    def delete(self, deleteData):
        # Check if deleteData is not None
        if deleteData is not None:
            try: 
                # Delete documents matching the deleteData
                result = self.database.animals.delete_many(deleteData)
                # Return True if deletion was successful
                return result.acknowledged
            except Exception as e:
                # Print error message if deletion fails
                print(f"Error deleting documents: {e}")
                return False
        else:
            # Raises exception if not delete criteria is provided
            raise Exception("No delete criteria provided")
            
        # Return the dataset else let the error flow up
        return result.raw_result