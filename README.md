# Application-Resources-Verification-Classifier

Application-Resources-Verification-Classifier is a Flask web application that helps users identify trusted and untrusted URLs associated with a specific app. The application allows users to input the name of an app, and it will search for the app in the Play Store, App Store, and Microsoft Store. The URLs from these trusted sources will be displayed, while untrusted URLs from potentially harmful sources will be filtered out.

## Table of Contents
- [Introduction](#introduction)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)

## Introduction
App URL Verifier aims to help users ensure the safety and security of the apps they are interested in downloading. By verifying trusted URLs from official app stores and filtering out potentially harmful URLs, the application helps users make informed decisions about app downloads.

## Requirements
- Python 3.x
- Flask
- Googlesearch-Python

## Installation
1. Clone the repository to your local machine.
2. Install the required Python packages using pip:
```python
pip install flask googlesearch-python
```

## Usage
1. Run the Flask web application using the `app.py` script:
```python
python app.py
```


2. Open your web browser and access the application at `http://localhost:5000`.

3. In the search box, enter the name of the app you want to verify.

4. Click the "Search" button to initiate the verification process.

5. The application will display trusted URLs from official app stores and filter out potentially harmful URLs from untrusted sources.

## Contributing
Contributions to the App URL Verifier project are welcome! If you encounter any issues or have suggestions for improvements, feel free to create a pull request or open an issue in the GitHub repository.
