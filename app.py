from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

# Your Pexels API key
PEXELS_API_KEY = ""
PEXELS_BASE_URL = "https://api.pexels.com/v1"
PEXELS_VIDEOS_URL = "https://api.pexels.com/videos"


@app.route('/')
def home():
    return jsonify({
        "message": "Pexels API Wrapper",
        "endpoints": {
            "/search/photos": "Search for photos (GET)",
            "/search/videos": "Search for videos (GET)",
            "/photo/<id>": "Get specific photo by ID (GET)",
            "/curated": "Get curated photos (GET)"
        }
    })


@app.route('/search/photos', methods=['GET'])
def search_photos():
    """Search for photos on Pexels"""
    query = request.args.get('query')
    page = request.args.get('page', 1)
    per_page = request.args.get('per_page', 15)
    
    if not query:
        return jsonify({"error": "Query parameter is required"}), 400
    
    headers = {
        "Authorization": PEXELS_API_KEY
    }
    
    params = {
        "query": query,
        "page": page,
        "per_page": per_page
    }
    
    try:
        response = requests.get(
            f"{PEXELS_BASE_URL}/search",
            headers=headers,
            params=params
        )
        response.raise_for_status()
        return jsonify(response.json())
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500


@app.route('/search/videos', methods=['GET'])
def search_videos():
    """Search for videos on Pexels"""
    query = request.args.get('query')
    page = request.args.get('page', 1)
    per_page = request.args.get('per_page', 15)
    
    if not query:
        return jsonify({"error": "Query parameter is required"}), 400
    
    headers = {
        "Authorization": PEXELS_API_KEY
    }
    
    params = {
        "query": query,
        "page": page,
        "per_page": per_page
    }
    
    try:
        response = requests.get(
            f"{PEXELS_VIDEOS_URL}/search",
            headers=headers,
            params=params
        )
        response.raise_for_status()
        return jsonify(response.json())
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500


@app.route('/photo/<int:photo_id>', methods=['GET'])
def get_photo(photo_id):
    """Get a specific photo by ID"""
    headers = {
        "Authorization": PEXELS_API_KEY
    }
    
    try:
        response = requests.get(
            f"{PEXELS_BASE_URL}/photos/{photo_id}",
            headers=headers
        )
        response.raise_for_status()
        return jsonify(response.json())
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500


@app.route('/curated', methods=['GET'])
def get_curated():
    """Get curated photos"""
    page = request.args.get('page', 1)
    per_page = request.args.get('per_page', 15)
    
    headers = {
        "Authorization": PEXELS_API_KEY
    }
    
    params = {
        "page": page,
        "per_page": per_page
    }
    
    try:
        response = requests.get(
            f"{PEXELS_BASE_URL}/curated",
            headers=headers,
            params=params
        )
        response.raise_for_status()
        return jsonify(response.json())
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True,  port=5000)
