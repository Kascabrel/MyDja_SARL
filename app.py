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
            'name': 'Jean Dupont',
            'role': 'Directeur Général',
            'image': 'images/team/member1.svg'
        },
        {
            'name': 'Marie Kouassi',
            'role': 'Chef de Projet',
            'image': 'images/team/member2.svg'
        },
        {
            'name': 'Paul Ndongo',
            'role': 'Ingénieur Électricien',
            'image': 'images/team/member3.svg'
        },
        {
            'name': 'Sophie Kamara',
            'role': 'Technicienne Sécurité',
            'image': 'images/team/member4.svg'
        },
        {
            'name': 'Ahmed Hassan',
            'role': 'Spécialiste Réseaux',
            'image': 'images/team/member5.svg'
        },
        {
            'name': 'Fatima Diallo',
            'role': 'Responsable BTP',
            'image': 'images/team/member6.svg'
        }
    ]
    return render_template('contact.html', title='Contact', team_members=team_members)

if __name__ == '__main__':
    # Only enable debug mode in development
    debug_mode = os.getenv('FLASK_ENV') == 'development'
    app.run(debug=debug_mode)
