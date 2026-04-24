# LEXSNIP: DendroDoc

## Overview

**LEXSNIP: DendroDoc** is an intelligent document clustering and semantic analysis platform that transforms how organizations process and understand large document collections. The system uses advanced machine learning techniques to automatically group similar documents, extract key insights, and generate comprehensive analysis reports.

### Project Vision

DendroDoc bridges the gap between unstructured document repositories and actionable intelligence by:
- **Semantic Understanding**: Using state-of-the-art sentence transformers to deeply understand document content
- **Hierarchical Visualization**: Presenting document relationships in an interactive dendrogram (hierarchical tree)
- **Intelligent Extraction**: Identifying and extracting relevant content based on custom keywords
- **Report Generation**: Creating professional PDF reports with structured findings

---

## Table of Contents

1. [Features](#features)
2. [Project Architecture](#project-architecture)
3. [Technology Stack](#technology-stack)
4. [Installation & Setup](#installation--setup)
5. [Project Structure](#project-structure)
6. [API Documentation](#api-documentation)
7. [Frontend Components](#frontend-components)
8. [Database Schema](#database-schema)
9. [Core Algorithms](#core-algorithms)
10. [Usage Guide](#usage-guide)
11. [Development](#development)
12. [Deployment](#deployment)

---

## Features

### Core Capabilities

- **📁 Multi-Document Upload**: Process multiple PDFs and text files simultaneously
- **🧠 Semantic Analysis**: Generate vector embeddings for deep content understanding
- **🌳 Hierarchical Clustering**: Automatically group documents using hierarchical clustering algorithms
- **📊 Interactive Visualization**: Explore document relationships through an interactive D3-based dendrogram
- **🔍 Keyword Extraction**: Extract snippets containing custom keywords with context preservation
- **📄 PDF Report Generation**: Generate professional reports with analysis results and metadata
- **💾 Session Management**: Save and retrieve analysis history
- **⚡ CORS-Enabled API**: Seamless frontend-backend communication

### Advanced Features

- **Context-Aware Extraction**: Retrieves sentences surrounding keywords for better understanding
- **Normalized Embeddings**: Prevents numerical instability with proper vector normalization
- **Hierarchical Tree Payloads**: Each leaf node contains snippet previews and topic classification
- **Batch Processing**: Efficiently processes large documents through chunking
- **Error Resilience**: Robust handling of malformed PDFs and edge cases

---

## Project Architecture

### High-Level Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                      Frontend (React)                        │
│  ┌──────────────────────────────────────────────────────┐  │
│  │ • File Upload Interface                               │  │
│  │ • D3 Tree Visualization                              │  │
│  │ • Keyword Input Form                                 │  │
│  │ • Session History View                               │  │
│  └──────────────────────────────────────────────────────┘  │
└────────────────────────┬─────────────────────────────────────┘
                         │ HTTP/REST API
                         ▼
┌─────────────────────────────────────────────────────────────┐
│                    Backend (FastAPI)                        │
│  ┌──────────────────────────────────────────────────────┐  │
│  │ • PDF Extraction (PyMuPDF)                           │  │
│  │ • Text Processing & Tokenization                    │  │
│  │ • Semantic Embedding (Sentence-Transformers)        │  │
│  │ • Hierarchical Clustering (SciPy)                   │  │
│  │ • Keyword Extraction                                │  │
│  │ • PDF Report Generation (ReportLab)                │  │
│  └──────────────────────────────────────────────────────┘  │
└────────────────────────┬─────────────────────────────────────┘
                         │ MongoDB Driver
                         ▼
┌─────────────────────────────────────────────────────────────┐
│                   MongoDB Database                          │
│  ┌──────────────────────────────────────────────────────┐  │
│  │ Collection: trees                                    │  │
│  │ • session_id, tree, extractions, keywords,          │  │
│  │ • filenames, timestamp, mode                        │  │
│  └──────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

---

## Technology Stack

### Frontend

| Technology | Purpose | Version |
|-----------|---------|---------|
| **React** | UI Framework | 19.2.4 |
| **Vite** | Build Tool & Dev Server | 8.0.1 |
| **Tailwind CSS** | Utility-First Styling | 4.2.2 |
| **React D3 Tree** | Hierarchical Visualization | 3.6.6 |
| **Lucide React** | Icon Library | 1.8.0 |
| **ESLint** | Code Quality | 9.39.4 |

### Backend

| Technology | Purpose |
|-----------|---------|
| **FastAPI** | High-Performance Web Framework |
| **PyMuPDF (fitz)** | PDF Text Extraction |
| **Sentence-Transformers** | Semantic Embeddings (all-MiniLM-L6-v2) |
| **SciPy** | Hierarchical Clustering Algorithms |
| **NumPy** | Numerical Computing |
| **ReportLab** | PDF Report Generation |
| **MongoDB** | Document Database |
| **Uvicorn** | ASGI Application Server |

### Infrastructure

- **MongoDB Cloud**: Database hosting with Atlas
- **CORS Middleware**: Cross-Origin Resource Sharing support

---

## Installation & Setup

### Prerequisites

- **Python 3.8+** (for backend)
- **Node.js 16+** (for frontend)
- **MongoDB Atlas** account (or local MongoDB instance)
- **pip** (Python package manager)
- **npm** or **yarn** (Node package manager)

### Backend Setup

#### 1. Create Python Virtual Environment

```bash
cd d:\clusty
python -m venv .venv
# On Windows
.venv\Scripts\activate
# On Unix/macOS
source .venv/bin/activate
```

#### 2. Install Dependencies

```bash
pip install fastapi uvicorn pymupdf reportlab sentence-transformers scipy numpy pymongo python-multipart
```

#### 3. Configure Environment Variables

Create a `.env` file in the root directory:

```env
MONGO_URI=mongodb+srv://username:password@cluster.mongodb.net/?retryWrites=true&w=majority&appName=YourAppName
```

#### 4. Run Backend Server

```bash
cd d:\clusty
.venv\Scripts\activate
python .venv\app.py
```

Backend will be available at `http://localhost:8000`

### Frontend Setup

#### 1. Install Dependencies

```bash
cd d:\clusty\frontend\proj
npm install
```

#### 2. Run Development Server

```bash
npm run dev
```

Frontend will be available at `http://localhost:5173` (or another port shown in console)

#### 3. Build for Production

```bash
npm run build
npm run preview
```

---

## Project Structure

### Directory Layout

```
d:\clusty/
├── README.md                          # This file
├── .venv/                             # Python virtual environment
│   └── app.py                         # Main FastAPI application
├── frontend/
│   ├── package.json                   # Frontend dependencies
│   └── proj/
│       ├── package.json               # Vite project config
│       ├── vite.config.js            # Vite configuration
│       ├── eslint.config.js          # ESLint rules
│       ├── index.html                # HTML entry point
│       ├── README.md                 # Frontend-specific docs
│       ├── public/                   # Static assets
│       └── src/
│           ├── main.jsx              # React entry point
│           ├── App.jsx               # Main React component
│           ├── index.css             # Global styles
│           └── assets/               # Images and media
```

### File Descriptions

| File | Purpose |
|------|---------|
| `.venv/app.py` | FastAPI backend with all API endpoints |
| `frontend/proj/src/App.jsx` | Main React component with UI logic |
| `frontend/proj/vite.config.js` | Build configuration |
| `frontend/proj/eslint.config.js` | Code style enforcement |

---

## API Documentation

### Overview

All API endpoints are hosted at `http://localhost:8000`

### Endpoints

#### 1. **POST /analyze**
Analyze documents and generate clustering

**Request:**
- **Content-Type**: `multipart/form-data`
- **Parameters**:
  - `files` (File[]): Multiple PDF or text files
  - `keywords` (string, optional): Comma-separated keywords for extraction

**Response:**
```json
{
  "session_id": "a1b2c3d4",
  "mode": "semantic-chunked",
  "tree": {
    "name": "root",
    "attributes": { "type": "cluster", "distance": 0.45 },
    "children": [
      {
        "name": "document.pdf",
        "attributes": {
          "type": "leaf",
          "topic": "KEYWORD",
          "hitCount": 3,
          "snippet_preview": "Sample text...",
          "dataPayload": []
        }
      }
    ]
  },
  "extractions": [
    {
      "filename": "document.pdf",
      "results": [
        {
          "keyword": "term",
          "snippet": "full context sentence",
          "score": 2
        }
      ]
    }
  ],
  "keywords": ["term"],
  "filenames": ["document.pdf"],
  "timestamp": "2026-04-24T10:30:00"
}
```

**HTTP Status Codes:**
- `200`: Success
- `400`: Validation error (< 2 documents, invalid embeddings)
- `500`: Server error

---

#### 2. **GET /download-report/{session_id}**
Download analysis report as PDF

**Parameters:**
- `session_id` (string): Session ID from analyze response

**Response:**
- **Content-Type**: `application/pdf`
- Binary PDF file download

**HTTP Status Codes:**
- `200`: PDF file
- `404`: Session not found
- `500`: Report generation error

---

#### 3. **GET /history**
Retrieve analysis history

**Query Parameters:**
- `limit` (integer, optional, default: 20): Number of records to return

**Response:**
```json
[
  {
    "session_id": "a1b2c3d4",
    "mode": "semantic-chunked",
    "filenames": ["doc1.pdf", "doc2.pdf"],
    "timestamp": "2026-04-24T10:30:00"
  }
]
```

**HTTP Status Codes:**
- `200`: Success
- `500`: Database error

---

## Frontend Components

### App.jsx Architecture

#### Key Sections

1. **Global Styles Injector**
   - Injects custom CSS animations
   - Defines custom keyframes: `pulse-ring`, `float`, `scan`, `shimmer`, `fade-up`, etc.
   - Sets up Tailwind utilities and scrollbar styling

2. **UI Layout**
   - Header with branding
   - File upload zone with drag-and-drop
   - Keyword input field
   - Interactive D3 tree visualization
   - Results panel with extraction details
   - Session history sidebar

3. **State Management**
   ```jsx
   - files: UploadFile[]
   - keywords: string
   - analysisResult: AnalysisData
   - selectedNode: TreeNode
   - history: HistoryEntry[]
   - isLoading: boolean
   - error: string | null
   ```

4. **API Interactions**
   - `POST http://localhost:8000/analyze`: Submit analysis
   - `GET http://localhost:8000/history`: Fetch history
   - `GET http://localhost:8000/download-report/{sessionId}`: Download PDF

#### Styling

- **Color Scheme**:
  - Primary: `#00e5b4` (Teal)
  - Secondary: `#00c8ff` (Cyan)
  - Background: `#05080d` (Dark Navy)
  
- **Fonts**:
  - Display: Syne (Google Fonts)
  - Mono: Space Mono (Google Fonts)

- **Animations**:
  - Fade-up entrance animations
  - Glow effects on text
  - Scale transitions on elements
  - Pulsing ring effects

---

## Database Schema

### MongoDB Collection: `trees`

#### Document Structure

```json
{
  "_id": ObjectId,
  "session_id": "a1b2c3d4",
  "mode": "semantic-chunked",
  "tree": {
    "name": "root",
    "attributes": { "type": "cluster" | "leaf", ... },
    "children": [...]
  },
  "extractions": [
    {
      "filename": "doc.pdf",
      "results": [
        {
          "keyword": "term",
          "snippet": "context",
          "score": 2
        }
      ]
    }
  ],
  "keywords": ["term1", "term2"],
  "filenames": ["doc1.pdf", "doc2.pdf"],
  "timestamp": ISODate("2026-04-24T10:30:00Z")
}
```

#### Indexing Recommendations

```javascript
db.trees.createIndex({ "session_id": 1 }, { unique: true })
db.trees.createIndex({ "timestamp": -1 })
db.trees.createIndex({ "filenames": 1 })
```

---

## Core Algorithms

### 1. Document Embedding Generation

**Purpose**: Convert documents into numerical vectors for semantic comparison

**Algorithm**:
```
1. Split text into chunks (300 words each)
2. Generate embedding for each chunk using Sentence-Transformer
3. Average embeddings across chunks
4. Normalize vector to unit length (L2 norm)
5. Handle edge cases: NaN/Inf values, zero norms
```

**Implementation Details**:
- Model: `all-MiniLM-L6-v2` (384-dimensional embeddings)
- Chunk size: 300 words (prevents token limits)
- Normalization: L2 normalization to prevent distance metric errors
- Robustness: Random noise injection for empty/invalid texts

### 2. Hierarchical Clustering

**Purpose**: Build a tree structure showing document similarity relationships

**Algorithm**:
```
1. Calculate distance matrix using cosine distance
2. Apply hierarchical clustering (Average Linkage)
3. Build dendrogram from linkage matrix
4. Recursively construct tree from root
```

**Key Properties**:
- **Distance Metric**: Cosine distance (suitable for normalized embeddings)
- **Linkage Method**: Average (balanced tree structure)
- **Complexity**: O(n² log n) for n documents

### 3. Keyword Extraction with Context

**Purpose**: Find keyword occurrences and extract surrounding context

**Algorithm**:
```
1. Split text into sentences
2. For each keyword:
   a. Search all sentences (case-insensitive)
   b. Extract surrounding sentences (±context_window)
   c. Record match count as relevance score
3. Remove duplicate snippets
4. Sort by relevance score
```

**Parameters**:
- `context_sentences`: 3 (default) - sentences before/after match
- `case_insensitive`: True
- `deduplication`: First 150 characters of snippet

### 4. PDF Report Generation

**Purpose**: Create professional reports from analysis results

**Structure**:
1. Title page with session metadata
2. Section per document with keyword hits
3. Tabular layout: Keyword | Snippet
4. Consistent styling and formatting

**Technologies**:
- **ReportLab**: PDF generation
- **A4 Page Size**: Standard document format
- **Table Layout**: Optimized for readability (1.5" keyword | 5.5" snippet)

---

## Usage Guide

### Basic Workflow

#### Step 1: Start Services

```bash
# Terminal 1: Backend
cd d:\clusty
.venv\Scripts\activate
python .venv\app.py

# Terminal 2: Frontend
cd d:\clusty\frontend\proj
npm run dev
```

#### Step 2: Upload Documents

1. Navigate to `http://localhost:5173`
2. Drag-and-drop PDF/text files into upload zone
3. Files must total at least 2 documents

#### Step 3: Enter Keywords (Optional)

1. Type comma-separated keywords
2. Example: `contract, agreement, liability`
3. Leave blank to skip extraction

#### Step 4: Submit Analysis

1. Click "Analyze" button
2. Wait for backend processing (30s-2min depending on document size)
3. View dendrogram visualization
4. Click nodes to explore details

#### Step 5: Download Report

1. Click "Download Report" button
2. PDF will contain structured findings
3. Includes keyword hits with context snippets

### Advanced Usage

#### Viewing Analysis History

- Scroll "History" panel on right sidebar
- Click any session to reload analysis
- Timestamps show when analysis was created

#### Interpreting the Dendrogram

- **Leaf Nodes**: Individual documents
- **Internal Nodes**: Clusters of similar documents
- **Branch Length**: Distance between clusters (higher = more different)
- **Node Color**: Indicates document topic from keyword extraction
- **Preview**: Hover over leaves to see snippet preview

---

## Development

### Frontend Development

#### Commands

```bash
cd d:\clusty\frontend\proj

# Development server with hot reload
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview

# Lint code for issues
npm lint
```

#### Dependencies Update

```bash
npm update
npm audit fix
```

#### Directory Structure

```
src/
├── App.jsx              # Main component (1500+ lines)
├── main.jsx            # React DOM render
├── index.css           # Global styles
└── assets/             # Images/media
```

### Backend Development

#### Code Organization

```
.venv/app.py
├── Imports & Setup
├── FastAPI Configuration
├── MongoDB Connection
├── Utility Functions
│   ├── extract_text_from_pdf()
│   ├── get_document_embedding()
│   ├── extract_by_keywords()
│   └── build_tree()
├── Report Generation
│   └── generate_extracted_pdf()
└── API Endpoints
    ├── POST /analyze
    ├── GET /download-report/{session_id}
    └── GET /history
```

#### Common Tasks

```bash
# Test API endpoint
curl -X POST http://localhost:8000/analyze \
  -F "files=@document.pdf" \
  -F "keywords=test,example"

# Check API docs (auto-generated)
# Visit: http://localhost:8000/docs

# View MongoDB connection
# Update MONGO_URI in code or .env
```

#### Debugging

1. **PDF Extraction Issues**:
   - Check file format and encoding
   - Verify PyMuPDF installation

2. **Embedding Generation**:
   - Monitor model download (~120MB for first run)
   - Check available GPU memory for faster processing

3. **MongoDB Errors**:
   - Verify connection string
   - Check IP whitelist in MongoDB Atlas
   - Ensure network access

---

## Deployment

### Prerequisites for Deployment

- Cloud hosting platform (Azure, AWS, Heroku)
- MongoDB Atlas account (for production database)
- Environment variable management

### Frontend Deployment

#### Option 1: Vercel (Recommended)

```bash
npm install -g vercel
vercel deploy
```

#### Option 2: Netlify

```bash
npm run build
# Drag-and-drop dist/ folder to Netlify
```

#### Option 3: Docker

```dockerfile
FROM node:18-alpine
WORKDIR /app
COPY . .
RUN npm install && npm run build
EXPOSE 5173
CMD ["npm", "run", "preview"]
```

### Backend Deployment

#### Option 1: Azure Container Instances

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY .venv/app.py .
EXPOSE 8000
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
```

#### Option 2: Heroku

```bash
heroku create your-app-name
git push heroku main
heroku config:set MONGO_URI="your-mongodb-uri"
```

#### Option 3: Docker Compose

```yaml
version: '3.8'
services:
  backend:
    build: .
    ports:
      - "8000:8000"
    environment:
      - MONGO_URI=${MONGO_URI}
  
  frontend:
    build: ./frontend/proj
    ports:
      - "5173:5173"
```

### Environment Configuration

**Production `.env` file**:
```env
MONGO_URI=mongodb+srv://prod_user:prod_pass@prod-cluster.mongodb.net/?retryWrites=true&w=majority
API_BASE_URL=https://api.yourdomain.com
CORS_ORIGINS=https://yourdomain.com,https://www.yourdomain.com
```

---

## Performance Optimization

### Backend Optimization

1. **PDF Processing**: Use streaming for large files
2. **Embeddings**: Cache embeddings for repeated documents
3. **Database**: Index on `session_id` and `timestamp`
4. **Async Operations**: Use `asyncio` for concurrent document processing

### Frontend Optimization

1. **Code Splitting**: Lazy load D3 tree component
2. **Image Optimization**: Compress PNG/SVG assets
3. **Bundle Size**: Tree-shake unused Tailwind utilities
4. **Caching**: Browser cache for static assets

---

## Troubleshooting

### Common Issues

| Issue | Solution |
|-------|----------|
| PDF extraction fails | Check file is valid PDF, increase upload size limit |
| Embeddings contain NaN | Verify text encoding, check for malformed documents |
| MongoDB connection error | Check MONGO_URI, verify IP whitelist in Atlas |
| Frontend won't connect to backend | Ensure CORS is enabled, check API_BASE URL |
| Slow clustering for large files | Increase chunk size for embeddings, reduce keyword count |

### Debug Mode

```bash
# Backend with verbose logging
python .venv/app.py --debug

# Frontend with React DevTools
npm run dev -- --debug
```

---

## Contributing

### Code Style

- **Python**: PEP 8 (use `black` for formatting)
- **JavaScript**: ESLint configuration in `eslint.config.js`

### Testing

```bash
# Backend unit tests
pytest .venv/

# Frontend tests
npm test
```

### Pull Request Process

1. Create feature branch: `git checkout -b feature/description`
2. Commit changes: `git commit -m "clear message"`
3. Push: `git push origin feature/description`
4. Create PR with description

---

## License

This project is proprietary. All rights reserved.

---

## Support & Contact

For issues, questions, or contributions:
- **Issues**: Create a GitHub issue
- **Documentation**: See `/docs` folder
- **API Reference**: `http://localhost:8000/docs` (Swagger UI)

---

## Changelog

### Version 1.0.0 (Current)
- ✅ Document upload and analysis
- ✅ Semantic clustering with hierarchical dendrogram
- ✅ Keyword extraction with context
- ✅ PDF report generation
- ✅ Session history management
- ✅ Interactive D3 tree visualization

---

**Last Updated**: April 24, 2026
**Status**: Active Development
**Maintainer**: Development Team
