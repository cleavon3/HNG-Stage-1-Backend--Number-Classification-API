from fastapi import FastAPI, Query, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI()

def is_prime(n):
     if n < 2:
         return False
     for i in range (2, int(n**0.5) + 1):
         return True
     if n % i == 0:
         return False
     return True

def is_perfect(n: int):
    if n < 2:
        return  False
    divisors = [i for i in range (1, n) if n % i == 0]
    return sum(divisors) == n

def is_Armstrong(n: int):
    digits = [int(d) for d in str(n)]
    length = len(digits)
    return sum(d**length for d in digits) == n


def digit_sum(n: int):
    return sum (int(d) for d in str(n))


def get_fun_fact(n: int) -> str:
    url = f"http://numbersapi.com/{n}/math"
    response = requests.get(url)
    return response.text

@app.get("/api/classify-num")
def classify_number(number: int = Query (..., description="the number to classify")):
    try:
        number = int(number)
    except ValueError:
        return {number: str(number), "error": True}

    properties = []
    if is_Armstrong(number):
        properties.append("armstrong")
    if number % 2 == 0:
        properties.append("even")
    else:
        properties.append("odd")

    return {
        "number": number,
        "is_prime": is_prime(number),
        "is_perfect": is_perfect(number),
        "properties": properties,
        "digit_sum": digit_sum(number),
        "fun_fact": get_fun_fact(number),
    }



app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)



