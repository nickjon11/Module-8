# Module 8 - FastAPI Calculator Program

## Overview

This project is a simple calculator web test built using FastAPI. Unlike the previous calculator programs, this usies a basic arithmetic operations and currently no user input. 

## Important Exclaimer:

In order to properly run pytest, use 2 WSL terminal windows: One for the webAPI to run and the other to run pytest

## Features

- FastAPI web application
- Addition
- Subtraction
- Multiplication
- Division
- Error handling for division by zero
- Unit testing with Pytest
- Integration testing using FastAPI TestClient
- End-to-end testing with Playwright
- Logging for operations and errors
- GitHub Actions CI workflow

## Installation

Clone the repository:

```bash
git clone https://github.com/nickjon11/module-8.git
cd module-8
```

Create a Virtual environemnt:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt 
```

Install Playwright browsers:

```bash
playwright install
```

## Running the Application

Start the FastAPI server:

```bash
uvicorn app.main:app --reload
```

Open your browser and navigate to:

```
http://127.0.0.1:8000
```

Example API request:

```
http://127.0.0.1:8000/add?a=2&b=3
```

Response:

```json
{
    "result": 5.0
}
```

## Running Tests

Run all tests:

```bash
PYTHONPATH=. pytest
```

Run only the unit tests:

```bash
pytest tests/test_operations.py
```

Run only the integration tests:

```bash
pytest tests/test_main.py
```

Run only the Playwright end-to-end tests (make sure the FastAPI server is running):

```bash
pytest tests/test_e2e.py
```
