from flask import Flask, render_template, jsonify, make_response

app = Flask(__name__)

JOBS = [{
  'id': 1,
  'title': "Data Analyst",
  'location': 'Dublin, Ireland',
  'salary': '£80,000'
}, {
  'id': 2,
  'title': "Data Scientist",
  'location': 'Brisbane, Australia',
}, {
  'id': 3,
  'title': "Network Manager",
  'location': 'Capetown, South Africa',
  'salary': 'ZAR 800,000'
}, {
  'id': 4,
  'title': "Golang Developer",
  'location': 'Brisbane, Australia',
  'salary': 'AU$150,000'
}]


@app.route("/")
def hello_world():
  return render_template("home.html", jobs=JOBS, company_name="Mapfumo")


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


print(__name__)
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
