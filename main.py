import requests
from PIL import Image
import pytesseract
from io import BytesIO

# Function to solve captcha

def solve_captcha(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    text = pytesseract.image_to_string(img)
    return {'captcha_text': text}

# Default URL
url = 'https://example.com/sample_captcha.png'
result = solve_captcha(url)
print(result)