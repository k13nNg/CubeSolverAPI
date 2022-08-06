
from fastapi import FastAPI, HTTPException
import twophase.solver  as sv

app = FastAPI()

# def solver(inputStr):
#     return sv.solve(inputStr)

@app.get("/{face_string}")
def root(face_string: str):
    result = sv.solve(face_string)

    if("Error: " in result):
        raise HTTPException(status_code=404, detail = result)
    
    return result