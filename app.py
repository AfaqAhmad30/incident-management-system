from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///incidents.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Incident Model (Database Table)
class Incident(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    priority = db.Column(db.String(20), default='Medium')
    status = db.Column(db.String(20), default='Open') # Open, In Progress, Resolved
    assigned_to = db.Column(db.String(50), default='Unassigned')

with app.app_context():
    db.create_all()

# Web Route: Dashboard (View all incidents)
@app.route('/')
def index():
    incidents = Incident.query.all()
    return render_template('index.html', incidents=incidents)

# REST API: Create Incident
@app.route('/api/incidents', methods=['POST'])
def create_incident():
    data = request.form if request.form else request.json
    new_incident = Incident(
        title=data.get('title'),
        description=data.get('description'),
        priority=data.get('priority', 'Medium'),
        assigned_to=data.get('assigned_to', 'Unassigned')
    )
    db.session.add(new_incident)
    db.session.commit()
    return redirect(url_for('index'))

# REST API: Resolve Incident
@app.route('/api/incidents/<int:id>/resolve', methods=['POST'])
def resolve_incident(id):
    incident = Incident.query.get_or_404(id)
    incident.status = 'Resolved'
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, port=5000)
