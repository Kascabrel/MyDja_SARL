# MyDja_SARL
Site web of the myDja_SARL, a society locate in central Africa

## About
This is a Flask web application for MyDja SARL, a company based in Central Africa.

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Kascabrel/MyDja_SARL.git
cd MyDja_SARL
```

2. Create a virtual environment (recommended):
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

### Local Development

To run the Flask application in development mode with debug enabled:

```bash
export FLASK_ENV=development  # On Windows: set FLASK_ENV=development
python app.py
```

Or run in production mode (default):

```bash
python app.py
```

The application will be available at `http://127.0.0.1:5000/`

### Docker

To run the application using Docker:

1. Build the Docker image:
```bash
docker build -t mydja-sarl .
```

2. Run the container:
```bash
docker run -d -p 5200:5200 --name mydja-sarl mydja-sarl
```

The application will be available at `http://127.0.0.1:5200/`

## Project Structure

```
MyDja_SARL/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── templates/          # HTML templates
│   ├── base.html      # Base template
│   ├── index.html     # Home page
│   └── about.html     # About page
└── static/            # Static files
    └── css/
        └── style.css  # Stylesheet
```

## Features

- Home page with company information
- About page
- Contact page with team carousel
- Responsive design
- Clean and modern UI
- Active navigation state highlighting

## Deployment

The application is automatically deployed to a production server using GitHub Actions when changes are pushed to the `main` branch. The deployment workflow:

1. Builds a Docker image
2. Pushes the image to Docker Hub
3. Deploys to the production server via SSH
4. Runs the application on port 5200

### Required Secrets

To enable automatic deployment, configure the following secrets in your GitHub repository settings:

- `DOCKERHUB_USERNAME`: Your Docker Hub username
- `DOCKERHUB_TOKEN`: Your Docker Hub access token
- `SERVER_IP`: The IP address of your deployment server
- `SERVER_USER`: SSH username for the server
- `SERVER_SSH_KEY`: SSH private key for server access
