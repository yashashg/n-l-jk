from flask import Flask
from flask_restful import Resource, Api, reqparse
import csv 

import utilities as ut
from botmodel import BotModel


app = Flask(__name__)
api = Api(app)

botmodel = BotModel()
botmodel.initialize()

class Users(Resource):
    # methods go here
    
    def post(self):
        
        parser = reqparse.RequestParser()  # initialize
        parser.add_argument('user_query', required=True)  # add args
        args = parser.parse_args()  # parse arguments to dictionary

        user_query=args['user_query']
        user_query = user_query.strip().lower()
        bot_responses, served = [], False
        ag, conf, resp = botmodel.response(user_query)
        if conf < 0.3:
            # Too low confidence of the intent classifier 
            bot_responses.append("Sorry. I did not understand your query.")
        else :
                bot_responses.extend(resp)
        
        return {'userId': bot_responses}, 200  # return data with 200 OK
        
        
api.add_resource(Users, '/')  # '/users' is our entry point
    
if __name__ == '__main__':
    app.run()  # run our Flask app
