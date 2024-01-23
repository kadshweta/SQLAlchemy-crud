from flask import Flask,request,jsonify
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db=SQLAlchemy(app)



class User(db.Model):
    id= db.Column(db.Integer,primary_key =True)
    username= db.Column(db.String(80),unique=True)
    email=db.Column(db.String(80),unique=True)



@app.route("/user_create",methods=['POST'])
def user_create():
    data= request.get_json()
    user=User(
        username=data['username'],
        email=data['email']
    )

    db.session.add(user)
    db.session.commit()
    return {'msg':"user created "}

@app.route("/read/<int:id>",methods=['GET'])
def read_data(id):
    user=User.query.get(id)

    if user:
        user_data={
            "username":user.username,
            "email":user.email
        }
        response=jsonify(user_data)
        return response
    else:
        return jsonify({"error": "User not found"}), 404
    

@app.route("/delete/<int:id>",methods=['DELETE'])
def delete_data(id):
    user=User.query.get(id)

    if user:
        db.session.delete(user)
        db.session.commit()


    return {'msg':"delete data succesfully "}  

# @app.route("/update/<int:id>",methods)  

    




if __name__ == "__main__":
    with app.app_context():            #
        db.create_all()
        app.run(debug=True)