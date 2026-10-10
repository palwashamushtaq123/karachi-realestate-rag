
# 🏢 AI Real Estate Intelligence Platform

An end-to-end, production-ready AI-powered real estate web application built specifically for the Karachi property market, which seamlessly integrates comprehensive data analysis, machine learning price prediction, tailored property recommendations, and a FastAPI-driven backend supported by an intelligent RAG knowledge assistant and Generative AI chatbot for expert buying guidance and legal advice.

## 🚀 Live Demo & Architecture
* **Live Application**: [https://ai-real-estate-karachi.vercel.app](https://ai-real-estate-karachi.vercel.app)
* **Deployment Platform**: Vercel Serverless 

* Framework: FastAPI   Database & Vector Store: ChromaDB (Local persistent vector database)
* **AI Engine**: Groq Cloud (`llama-3.3-70b-versatile`)

---
## 🛠️ Project Folder Structure
d-line interface for testing pipeline
├── ingest.py             # Script to ingest knowledge base into ChromaDB[cite: 12]
├── README
## 📂 Project Directory Structure

```text
AI Real Estate Intelligence Platform/
│
├── api/                   # Vercel serverless API handlerss / Frontend template/ API endpoints 
|   ├── index.htm
│   └── index.py     
|          
├── app/                   # Core application modules & services
│   ├── __init__.py
    ├──chunker.py          # Document text chunking logic
│   ├── config.py          # Application configurations & environment variables
│   ├── document_loader.py # PDF & text document loader
│   ├── embedding_service.py # Text embedding generator
│   ├── groq_service.py    # Groq LLM integration
│   ├── ingest_service.py  # Vector store ingestion pipeline
│   ├── rag_service.py     # Retrieval-Augmented Generation logic
│   └── vector_store.py    # ChromaDB connection & management
│
├── assets/                # UI screenshots
│   ├── market_analysis.png
│   ├── price_predictor.png
│   ├── propertry_finder.png
│   └── propertry_legal_guide.png
│
├── chorama_db/            # ChromaDB vector database storage[cite: 11, 12, 13]
├── data/                  # Raw and cleaned Datasets (Zameen.com Karachi filtered data)[cite: 9]
├── knowledge_base/        # PDFs & documents for RAG (Guides, Legal Tips)[cite: 13]
├── models/                # Trained ML models (.pkl)[cite: 11, 13]
├── notebooks/             # Jupyter Notebooks for EDA & ML training[cite: 9, 13]
├── static/                # CSS and static assets[cite: 13]
├── .evn.example           # Template for environment variables[cite: 12]
├── .gitignore             # Git ignore rules[cite: 12]
├── cli.py                 # Command-line interface utilities
├── ingest.py              # Document ingestion script for RAG[cite: 13]
├── requirements.txt       # Python dependencies[cite: 13]
├── vercel.json            # Deployment configuration[cite: 13]
└── README.md              # Project Documentation[cite: 13]
```





## 📊 Key Features & Implementation Details

**1. Data Analysis & PreprocessingDataset:**

- Collected raw real estate listings from Zameen.com (Total rows: 168,446). 
- Filtering & Cleaning: Filtered specifically for Karachi city properties (df['city'] == 'karachi'), resulting in a clean dataset of 59,357 records. Handled missing values, removed duplicates, and filtered extreme price outliers using interquartile ranges (1st to 99th percentile). 
- Visualizations: Generated insightful plots including Area Size vs Price Relationship and Top 10 Locations in Karachi (saved in assets/ and notebooks/).





**2. Machine Learning Price Prediction**

Trained and compared three regression models using features like bedrooms, baths, area size, latitude, and longitude: 
- Linear Regression 
- Decision Tree Regressor 
- Random Forest Regressor (Selected as Best Model) 
- Evaluation & Confusion Matrix: Evaluated models using MAE, RMSE, and $R^2$ Score. Built a binned price category Confusion Matrix (Budget, Mid-Range, Luxury) to evaluate classification-style accuracy on price bands. Saved the best performing pipeline using joblib into models/best_karachi_price_model.pkl.

**3. Property Recommendation System**

Built a custom recommendation engine (api/index.py) that filters properties matching user constraints (maximum budget, minimum bedrooms, and location) and automatically generates natural language explanations for why each property fits the user's criteria.


**4. GenAI Chatbot & RAG Knowledge Assistant**

- RAG Pipeline: Integrated ChromaDB vector store with Groq LLM API. Loaded expert PDFs from knowledge_base/ (Investment guide.pdf, Legal Due Diligence Check.pdf, Property Buying Guide.pdf), chunked them, embedded them, and stored vectors locally in chorama_db/. 
- Contextual Answers: The assistant accurately answers legal, buying, and investment queries using retrieved chunks from the uploaded documents.


## 🛠️ Installation & Local Setup

**1. Clone the Repository:**

git clone [https://github.com/palwasha1/ai-knowledge-assistant.git](https://github.com/palwasha1/ai-knowledge-assistant.git)
cd ai-knowledge-assistant

**2. Create Virtual Environment & Install Dependencies:**

- python -m venv venv


- source venv/bin/activate              # On Windows: venv\Scripts\activate


**3. Install dependencies:**

- pip install -r requirements.txt

**4. Configure Environment Variables:**

Create a .env file in the root directory and add your API keys:

- GROQ_API_KEY=your_groq_api_key_here

**5. Run the Application:**

- uvicorn api.index:app --reload

## 🖼️ Screenshots & Visuals

- Price Categorization Confusion Matrix:  notebooks/confusion_matrix.png
- Market Analysis Karachi EDA:   notebooks/karachi_eda.png
