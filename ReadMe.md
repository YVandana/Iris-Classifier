# Iris Flower Classification API

A machine learning service that classifies iris flowers into three species using Random Forest, served via FastAPI.

## 🌟 Features
- Trained Random Forest classifier on the classic Iris dataset
- REST API endpoint for predictions
- Docker container support for easy deployment
- Client script to test the API

## 🛠️ Technologies Used
- Python 3.11
- scikit-learn (RandomForestClassifier)
- FastAPI (web framework)
- joblib (model persistence)
- Docker (containerization)

## 🚀 Getting Started

### Prerequisites
- Python 3.11+
- Docker

### Installation

1. Clone the repository:
```bash
git clone https://github.com/YVandana/Iris-Classifier.git
cd Iris-Classifier
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

### Running the API Server

Start the FastAPI server:
```bash
uvicorn server:app --reload
```

The API will be available at `http://localhost:8000`

### Using the Client

Run the client script to test predictions:
```bash
python client.py
```

### API Endpoints

- `GET /`: Returns a welcome message
- `POST /predict`: Accepts feature data and returns predictions

Example prediction request:
```json
{
    "features": [5.1, 3.5, 1.4, 0.2]
}
```

Example response:
```json
{
    "prediction": "setosa"
}
```

## 🐳 Docker Deployment

Build the Docker image:
```bash
docker build -t iris-classifier .
```

Run the container:
```bash
docker run -d -p 8000:8000 iris-classifier
```

## 📂 Project Structure
```
Iris-Classifier/
├── app/
│   ├── server.py        # FastAPI server code
│   ├── client.py        # Example client code
│   └── model.joblib     # Trained model
├── Dockerfile           # Docker configuration
├── requirements.txt     # Python dependencies
└── README.md            # This file
```

## 🤝 Contributing
Contributions are welcome! Please open an issue or submit a pull request.

## 📜 License
[GNU](https://choosealicense.com/licenses/gnu/)

## 📬 Contact
For questions or feedback, please contact Vandana Yalla at vandanayalla321@gmail.com.
```
