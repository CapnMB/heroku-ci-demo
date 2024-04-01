from fastapi import FastAPI, HTTPException
from is_prime import is_prime

app = FastAPI()

# Route to check if a number is a prime number
@app.get("/prime/{number}")
def check_if_prime(number: int):
    return is_prime(number)
    raise HTTPException(status_code=400, detail="Input invalid")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
