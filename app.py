from recommender import predict

from fastapi import FastAPI
import uvicorn

app = FastAPI()

def func1():
    return [0, 516, 5, 200, 323, 720]

@app.get("/")
def root():
    return func1()

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

results = predict(input_string, in_dataset = True)

##show to user



