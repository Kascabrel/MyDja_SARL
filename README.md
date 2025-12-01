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
- Responsive design
- Clean and modern UI
