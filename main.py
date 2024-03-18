from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Union

app = FastAPI()

class RequestData(BaseModel):
    data: List[Union[int, str]]

class ResponseData(BaseModel):
    is_success: bool
    user_id: str
    email: str
    roll_number: str
    odd_numbers: List[int]
    even_numbers: List[int]
    alphabets: List[str]

@app.post("/bfhl", response_model=ResponseData)
async def process_data(request: RequestData):
    user_id = "john_doe_17091999"  # Replace with your user ID
    email = "john@xyz.com"  # Replace with your email
    roll_number = "ABCD123"  # Replace with your roll number

    odd_numbers = []
    even_numbers = []
    alphabets = []

    for item in request.data:
        if isinstance(item, int):
            if item % 2 == 0:
                even_numbers.append(item)
            else:
                odd_numbers.append(item)
        elif isinstance(item, str) and item.isalpha():
            alphabets.append(item.upper())

    return ResponseData(
        is_success=True,
        user_id=user_id,
        email=email,
        roll_number=roll_number,
        odd_numbers=odd_numbers,
        even_numbers=even_numbers,
        alphabets=alphabets
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)