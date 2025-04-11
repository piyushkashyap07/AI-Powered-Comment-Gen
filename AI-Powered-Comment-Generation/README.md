# AI-Powered Comment Generator

A Chrome extension that uses AI to automatically generate meaningful code comments based on the code you're viewing.

## Features

- Generate comprehensive comments for code with a single click
- Works with multiple programming languages
- Supports GitHub, GitLab, and other code-viewing websites
- Customizable comment styles and formats
- Powered by Google's Gemini API

## Demo Screenshots

![Comment Generation Demo](Backend/images/image%20(2).png)
![Comment Generation Result](Backend/images/image%20(4).png)
![Extension in Action](Backend/images/image%20(6).png)
![Sample Output](Backend/images/image%20(7).png)
![Comment Integration](Backend/images/image%20(8).png)

## Project Setup Guide

This guide will walk you through the steps to set up and run the project locally. Follow each step carefully to ensure everything is properly configured.

### 1. Clone the Repository

Clone the repository to your local machine:
```bash
git clone https://github.com/piyushkashyap07/AI-Powered-Comment-Gen.git
cd AI-Powered-Comment-Generation
```

### 2. Obtain Your Gemini API Key

To access the Gemini API, follow these steps:
1. Visit the [Gemini API Key page](https://aistudio.google.com/app/apikey)
2. Generate your API key
3. Copy the generated API key

### 3. Configure the Backend

Once you've obtained your Gemini API key, insert it into the backend configuration:
1. Navigate to the `Backend` folder:
   ```bash
   cd Backend
   ```
2. Create a `.env` file (if it doesn't already exist) and add the following line:
   ```plaintext
   GOOGLE_API_KEY=<Your_Gemini_API_Key>
   ```

### 4. Set Up Python Environment

1. **Create a Python virtual environment** (if you haven't already):
   ```bash
   python -m venv venv
   ```
2. **Activate the virtual environment**:
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
   - On Windows:
     ```bash
     .\venv\Scripts\activate
     ```
3. **Install project dependencies**:
   Navigate to the `Backend` directory (if you're not already there), and run the following command:
   ```bash
   pip install -r requirements.txt
   ```

### 5. Run the Backend FastAPI Server

1. After installing the dependencies, run the FastAPI server using `uvicorn`:
   ```bash
   uvicorn app:app --reload
   ```
2. The FastAPI server should now be running locally. You can access it at:
   ```plaintext
   http://127.0.0.1:8000
   ```

### 6. Set Up the Chrome Extension

To load and test the Chrome extension locally:
1. Open Chrome and go to:
   ```plaintext
   chrome://extensions/
   ```
2. Enable **Developer Mode** (toggle on in the top right)
3. Click on **Load Unpacked** and select the extension folder from your project directory

## How It Works

1. The extension identifies code blocks on the webpage
2. When activated, it sends the code to the FastAPI backend
3. The backend processes the code with Google's Gemini API to generate meaningful comments
4. Generated comments are then displayed alongside or integrated with the original code

## Use Cases

- **Developers**: Quickly understand unfamiliar codebases
- **Students**: Learn programming concepts through AI-generated explanations
- **Code Reviewers**: Get immediate insights into code functionality
- **Documentation**: Generate starter documentation for your projects

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License. You are free to use, modify, and distribute this project under the terms of the MIT License.

## Conclusion

You have now successfully set up the AI-Powered Comment Generator. If you encounter any issues, please raise an issue in the repository.
