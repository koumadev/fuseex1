# FastAPI URL Validator

This project is a FastAPI-based web application that validates and fetches information about a given URL.

## Features
- Accepts a URL as input.
- Validates the URL's accessibility.
- Extracts the title of the webpage.

## Requirements
- Python 3.10+
- FastAPI
- httpx
- BeautifulSoup4

## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```bash
   cd fuseex1
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Start the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```
2. Open Postman or a browser and test the endpoint:
   - **Endpoint**: `POST /validate-url/`
   - **Request Body**:
     ```json
     {
       "url": "https://example.com"
     }
     ```

## Example Response
```json
{
  "url": "https://example.com",
  "status_code": 200,
  "title": "Example Domain"
}
```

## License
This project is licensed under the MIT License.
