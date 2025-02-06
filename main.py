from fastapi import FastAPI, Query, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI()


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(abs(n) ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def is_perfect(n: int):
    if n < 2:
        return False
    divisors = [i for i in range(1, abs(n)) if n % i == 0]
    return sum(divisors) == abs(n)


def is_armstrong(n: int):
    digits = [int(d) for d in str(abs(n))]
    length = len(digits)
    return sum(d ** length for d in digits) == abs(n)


def digit_sum(n: int):
    return sum(int(d) for d in str(abs(n)))


def get_fun_fact(n: int) -> str:
    url = f"http://numbersapi.com/{n}/math"
    response = requests.get(url)
    return response.text


@app.get("/api/classify-number")
def classify_number(number: int = Query(..., description="the number to classify")):
    try:
        number_int = int(number)
    except ValueError:
        raise HTTPException(
            status_code=400,
            detail={
                "number" : number,
                "error": True,
                "message": "input must be a valid integer."

            }
        )
    if number_int < 0:
        return {
            "number": number_int,
            "is_prime": False,
            "is_perfect": False,
            "properties": ["negative"],
            "digit_sum": digit_sum(number_int),
            "fun_fact": get_fun_fact(number_int),
        }


    properties = []
    if is_armstrong(number_int):
        properties.append("armstrong")
    if number_int % 2 == 0:
        properties.append("even")
    else:
        properties.append("odd")

    return {
        "number": number_int,
        "is_prime": is_prime(number_int),
        "is_perfect": is_perfect(number_int),
        "properties": properties,
        "digit_sum": digit_sum(number_int),
        "fun_fact": get_fun_fact(number_int),
    }


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
