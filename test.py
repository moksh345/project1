import os
import unittest
 
# from project1 import applicatn, udb
from applicatn import app,db
 
 
TEST_DB = 'test.db'
# class RoutingTests(unittest.TestCase):
#     # function to set up testing connection
#     def set_up():
#          app.config["TESTING"] = True
#          app.config["DEBUG"] = True
#          self.app = app.test_client()
#          self.assertEqual(app.debug,False)
#     # function to teardown connection after testing
#     def tear_down():
#          pass
    
#     def testindex(self):
#         response = self.app.get('/', follow_redirects=True)
#         self.assertEqual(response.status_code, 200)
    



 
 
class BasicTests(unittest.TestCase):
 
    ############################
    #### setup and teardown ####
    ############################
 
    # executed prior to each test
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
     #    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
     #        os.path.join(app.config['BASEDIR'], TEST_DB)
        self.app = app.test_client()
        # db.drop_all()
        # db.create_all()
 
        # Disable sending emails during unit testing
        # mail.init_app(app)
        # self.assertEqual(app.debug, False)
 
    # executed after each test
    def tearDown(self):
        pass
 
 
###############
#### tests ####
###############
 
    def test_main_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
    def test_register(self):
        response = self.app.get('/register', follow_redirects=False)
        self.assertEqual(response.status_code, 200)
        response = self.app.post('/register', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

 
 
if __name__ == "__main__":
    unittest.main()