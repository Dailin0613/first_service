from flask import Flask, render_template, request
from route import FileRoute

app = Flask(__name__)

#Manage routes


if __name__ == '__main__':
    
    #Blueprint route
    app.register_blueprint(FileRoute.main, url_prefix='/api/files')
    app.run(debug=True)
  