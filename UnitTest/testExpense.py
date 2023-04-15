try:
    import sys 
    sys.path.append('.')
    import unittest
    from App import app
    
except Exception as e:
    print("Module not found{}".format(e)) 
    
class flasktest(unittest.TestCase):
    
    def setUp(self):
        app.testing = True
        self.app = app.test_client(self)
        
     
    #Test Case 1: Testing the succession of the response     
    def testStatusCode(self):
        response = self.app.get('/expense/list')
        self.assertEqual(response.status_code, 200)
        
    #Test Case 2: Testing the formate of the text i.g json or html or xml etc 
    def testFormat(self):
        response = self.app.get('/expense/list')
        self.assertEqual(response.content_type, "application/json")
        
   
        
        
if __name__ == '__main__':
    unittest.main()        
                   