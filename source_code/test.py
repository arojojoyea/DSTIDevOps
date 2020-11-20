from app import app
import unittest

class FlaskTest (unittest.TestCase):
    #check for response 200 on base entry page
    def test_base(self):
        ant_test = app.test_client(self)
        response = ant_test.get("/")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

        #check for response 200 on purchase_record
    def test_user_routes(self):
        ant_test = app.test_client(self)
        response = ant_test.get("/purchase_record")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
    
    #check if item return is json 
    def test_user(self):  
        ant_test = app.test_client(self)
        response = ant_test.get("/purchase_record")
        self.assertEqual(response.content_type, "application/json")

    #check content of entry page
    def test_index_data(self):
        ant_test = app.test_client(self)
        response = ant_test.get("/")
        self.assertTrue(b'Status' in response.data)


#if _name_ == "_main_":
if __name__ == "__main__":
    unittest.main()