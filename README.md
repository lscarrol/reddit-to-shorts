# Reddit to YouTube Shorts Automation

## Overview
This project automates the process of identifying popular Reddit posts containing videos and images, downloading them, generating autogenrated commentary, and posting them on YouTube Shorts. The entire workflow is orchestrated using serverless GCP services including Cloud Functions, Cloud Run, and Pub/Sub.

## Features
- Identifies popular Reddit posts with videos and images.
- Downloads the identified videos and images.
- Analyzes the downloaded media using ImageAI and OpenCV.
- Generates autogenrated commentary for the downloaded media.
- Adds subtitles and commentary to the videos using MoviePy and OpenCV.
- Posts the videos with commentary on YouTube Shorts.

## Components
1. **Reddit Media Identification**
 - Scrapes Reddit for popular posts containing videos and images using Selenium.

2. **Media Download**
 - Transfers the fetched media to a designated GCP bucket for further processing.

3. **Media Analysis**
 - Utilizes ImageAI and OpenCV to analyze the downloaded media.

4. **Commentary Generation**
 - Utilizes NLP techniques to generate autogenrated commentary for the downloaded media.

5. **Subtitles and Commentary Addition**
 - Utilizes MoviePy and OpenCV to add subtitles and commentary to the videos.

6. **YouTube Shorts Posting**
 - Uses Google Cloud Vision API to post the videos with commentary on YouTube Shorts.

## Technologies Used
- **Python**: The primary programming language used for scripting and automation.
- **Selenium**: Web scraping tool for interacting with Reddit's dynamic website elements.
- **Google Cloud Platform (GCP) Services**:
 - Cloud Functions: Orchestrating the workflow.
 - Cloud Run: Running serverless containers for specific tasks.
 - Pub/Sub: Messaging service for communication between components.
 - Cloud Storage: Storing media in GCP buckets.
 - Cloud Vision API: Posting videos on YouTube Shorts.
 - ImageAI: Analyzing media.
 - OpenCV: Analyzing and editing media.
 - MoviePy: Editing videos.
 - NLP Libraries: Generating commentary for the media.

## Usage
- Configure the system to scrape Reddit for popular posts periodically.
- Access the YouTube Shorts to view the posted videos with autogenrated commentary.

## Contributors
- Your Name

## License
Distributed under the MIT License. See `LICENSE` for more information.
