# HNG-Stage-1-Backend--Number-Classification-API
# HNG Stage 1 Task - Number Classification API

This is a simple API that classifies a number and returns its mathematical properties along with a fun fact.

## Features
- **Number Classification**: Determines if a number is prime, perfect, odd/even, or an Armstrong number.
- **Digit Sum**: Calculates the sum of the digits of the number.
- **Fun Fact**: Fetches a fun fact about the number from the [Numbers API](http://numbersapi.com/).

## API Endpoint
- **URL**: `https://your-app.onrender.com/api/classify-number?number=<number>`
- **Method**: `GET`
- **Query Parameter**:
  - `number`: The number to classify (must be an integer).

### Example Request