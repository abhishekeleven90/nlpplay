from flask import Flask, g

app = Flask(__name__)

app.config.from_object('config')

# Request handlers -- these two hooks are provided by flask and we will use them
# to create and tear down a database connection on each request.
@app.before_request
def before_request():
    ##you can any way handle all the session here
    ##you can keep a dict of route urls
    ##you need to get which url from some custom object flask may provide
    ##raise permission denied error
    print 'app hi'

@app.after_request
def after_request(response):
    print 'app bye'
    return response

from app import views

