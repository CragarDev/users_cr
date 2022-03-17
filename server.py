import imp
from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = "iwuaerfpaiushgpiausdghp;uhpouh[u8"
from user import User





#* ===========================================
#? RENDER / Users
#* ===========================================
@app.route('/users')
def users():
    all_users = User.get_all_users()
    print("What...")
    return render_template("users.html", all_users=all_users)



#* ===========================================
#? RENDER / Create
#* ===========================================

@app.route('/create')
def create():
    print("What...")
    return render_template("create.html")





#t- ===========================================
#? PROCESS FORM - /
#t- ===========================================

@app.route('/create/new', methods=["POST"])
def create_new():
    
    query_data = {
        "first_name" : request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"]
    }
    
    new_user_id = User.create_new_user(query_data)
    
    print(f"Return after inserting: {new_user_id}")
    print("What...")
    return redirect("/users")





# ! MUST BE AT THE BOTTOM ---------------
if __name__ == "__main__":
    app.run(debug=True)
