# Setiment-Analysis-Flask
KoBERT Setiment Analysis Model Serving on Flask

## Overview
![image](https://github.com/user-attachments/assets/2b124043-a378-48ae-91f9-6eb01ffc8851)


This repository contains the backend implementation for the **Sentiment Analysis Music Recommendation Service**, a personalized web service that analyzes emotional states based on user-submitted Korean diary entries and provides tailored music recommendations via Spotify. The service leverages natural language processing (NLP) techniques and Spotify's API to deliver an engaging and emotionally resonant experience.

This backend is built using Flask and integrates:
- A **Korean Multi-Emotion Classification Model** powered by BERT for emotion analysis.
- **Spotify API** for music recommendation based on detected emotions.

The frontend counterpart (https://github.com/jimniDev/Setiment-Analysis-Music), implemented in React, handles the user interface, enabling users to input diaries, view analysis results, and explore music recommendations seamlessly.

![image](https://github.com/user-attachments/assets/606edacb-c0bc-4248-95b4-07f99580d913)


---

## Features

### 1. Sentiment Analysis
- **Korean Multi-Emotion Classification Model**:
  - Analyzes emotional states from diary entries written in Korean.
  - Powered by **BERT** for robust emotion classification.
  - Provides insights into emotions such as happiness, sadness, anger, and more.

### 2. Spotify Music Recommendation
- **Spotify Integration**:
  - Uses Spotify API to recommend music based on the analyzed emotions.
  - Includes features like:
    - Music Search: Search for tracks or artists.
    - Music Recommendation: Parameters include `danceability`, `energy`, and `valence` to match music to emotions.
  - Built with the Python open-source library, **Spotipy**. (https://spotipy.readthedocs.io/en/2.24.0/#)

---

## Project Structure
```
Setiment-Analysis-Flask/
├── api/
│   └──  spotify.py            # Spotify API interaction function
├── model/
│   └── setiment_analysis_inference.py  # Emotion classification and inference logic
├── template/
│   ├── input.html          # HTML templates for test
│   └── output.html         # HTML templates for test
├── util
│   └── emotion.py          # emotion class
├── app.py                    # Flask application (Spotify authentication, API, endpoints)
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation
```

---

## Development Process

### Authentication with Spotify API

![008 5ec55b3ed5efd2c901a2](https://github.com/user-attachments/assets/724296a1-bacd-47ec-bd90-5c0fdbe54764)

- Authenticate user credentials and request access tokens using the Spotify Accounts Service.
- Automate token refreshes (every 1 hour) using **Spotipy**.
- Securely transmit authentication information to access Spotify Web API.

### Emotion-Based Music Recommendation

![009 8f43ef3d4f4f6c19f3db](https://github.com/user-attachments/assets/a04b015b-44e7-4e16-85a2-b9b91d002ddc)

- Analyze user emotions and translate them into parameters (`danceability`, `energy`, `valence`) for the Spotify Music Recommendation API.
- Filter and present music that resonates with the user's emotional state.

#### Music Search API
- GET request API with TRACK (song title) / ARTIST (artist) as parameters.

#### Music Recommendation API
- `danceability`: suitability for dancing.
  - Higher values == better danceability.

- `energy`: Reflects level of energy.
  - Higher values == faster, more vibrant, and noisier music.

- `valence`: This aspect is particularly intriguing! Brightness of musical content.
  - Higher values == happier and more joyful music.
  - Lower values == sadder, angrier, or more melancholic music.


---

## Tech Stack
### Backend
- **Flask**: Lightweight Python framework for building APIs.
- **Spotipy**: Python library for Spotify Web API integration.
- **BERT**: Pretrained model for sentiment classification in Korean.

### Frontend
- **React**: For an interactive and intuitive user interface.

---

## How It Works
1. **User Inputs**:
   - Users submit their diary entries in Korean via the frontend.
2. **Emotion Analysis**:
   - Backend processes the text using BERT and classifies emotions.
3. **Music Recommendation**:
   - Based on the classified emotions, backend fetches music recommendations from Spotify using parameters like:
     - `Danceability`: Suitability for dancing.
     - `Energy`: Vibrancy and speed of the music.
     - `Valence`: Emotional positivity of the track.
4. **Music Exploration**:
   - Users receive a curated list of tracks matching their emotional state.

---

## Prerequisites
1. **Spotify Developer Account**:
   - Register an app on the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications).
   - Retrieve `Client ID` and `Client Secret`.
2. **Python Environment**:
   - Python 3.7 or higher.

---

## API Endpoints

### 1. **Emotion Analysis**
- **Endpoint**: `/analysis`
- **Method**: `POST`
- **Description**: Accepts a diary text input and returns emotion probabilities.
- **Request Body**:
  ```json
  {
    "text": "오늘 기분이 정말 좋아요!" // Today i'm feeling so great!
  }
  ```
- **Response**:
  ```json
  {
    "joy": 0.95,
    "calm": 0.02,
    "surprise": 0.01,
    "sadness": 0.01,
    "anger": 0.00,
    "hurt": 0.01
  }
  ```

### 2. **Music Recommendation**
- **Endpoint**: `/recommendation`
- **Method**: `GET`
- **Description**: Fetches recommended tracks based on emotional parameters.
- **Query Parameters**:
  - `joy`, `calm`, `sadness`, `anger`, `surprise`, `hurt` (probability values).
- **Response**:
  ```json
  [
    {
      "track_name": "Happy Song",
      "artist": "Joyful Artist",
      "url": "https://open.spotify.com/track/example"
    },
    ...
  ]
  ```

---

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/jimniDev/Setiment-Analysis-Flask.git
   cd Setiment-Analysis-Flask
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   Create a `.env` file in the root directory and add:
   ```
   SPOTIFY_CLIENT_ID=your_client_id
   SPOTIFY_CLIENT_SECRET=your_client_secret
   SPOTIFY_REDIRECT_URI=http://localhost:5000/callback
   ```

4. Run the Flask server:
   ```bash
   python app.py
   ```

5. Access the backend at:
   ```
   http://localhost:5000
   ```

---

## Results
- **People's Choice Award**: Won the *SW-Reskilling @LG Electronics* award for innovative use of sentiment analysis and music recommendations.

---

## Future Enhancements
- Support additional languages for diary inputs.
- Enhance emotion classification using multimodal data (e.g., voice inputs).
- Implement user-specific recommendations based on listening history.

---

## Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss potential updates.

---

## License
This project is licensed under the [MIT License](LICENSE).
