from flask import Flask,render_template,request,url_for
from flask_restful import Api,Resource
from sqlalchemy import null

app = Flask(__name__)
api = Api(app)

templateData ={
    "Subject":{},
    "Skill":{},
    "Major":{}
}

#Design
class majorComputer(Resource):
    def get(self,score):
        result = ""  
        return {"data":"Hello " + result}
    
class mainPage(Resource):
    def get(self):
        return '<h1>Hello Project</h1>'


#Call
api.add_resource(mainPage,"/")
api.add_resource(majorComputer,"/Subject/<string:score>")

if __name__ == "__main__":
    app.run()