def test_app_homepage(page):
    page.goto("http://127.0.0.1:8000/")
    assert "FastAPI Calculator is running" in page.text_content("body")