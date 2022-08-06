
from fastapi import FastAPI, HTTPException
import twophase.solver  as sv

app = FastAPI()


@app.get("/{face_string}")
def root(face_string: str):
    result = sv.solve(face_string)
    output = ""

    if("Error: " in result):
        raise HTTPException(status_code=404, detail = result)
    
    temp = result.split()

    for i in temp:
        if('3' in i):
            i=i[0]+"'"
        output+=i+" "    

    return output