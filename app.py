import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    """Home page route"""
    return render_template('index.html', title='MyDja SARL')

@app.route('/about')
def about():
    """About page route"""
    return render_template('about.html', title='About Us')

@app.route('/contact')
def contact():
    """Contact page route with team members"""
    # Mock data for team members
    team_members = [
        {
            'name': 'Billy Yossa',
            'role': 'Directeur Général',
            'image': 'images/team/member1.svg',
            'work': 'Ingénieur de Electrotechnicien'
        },
        {
            'name': 'Peguy Martial Djatchedje',
            'role': 'Directeur adjoint, Chef de Projet',
            'image': 'images/team/member2.svg',
            'work': 'Ingénieur de Electrotechnicien'
        },
        {
            'name': 'Steve Kamguia',
            'role': 'IT consultant & developpeur embarqué',
            'image': 'images/team/member3.svg',
            'work': ' Ingénieur de travaux informatique.'
        },
    ]
    return render_template('contact.html', title='Contact', team_members=team_members)

if __name__ == '__main__':
    # Only enable debug mode in development
    debug_mode = os.getenv('FLASK_ENV') == 'development'
    app.run(debug=debug_mode)
