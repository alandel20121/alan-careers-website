from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def hello_world():
  return render_template('home.html')

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)
  
if __name__=="__main__":
  app.run(host='0.0.0.0', debug=True)
  



