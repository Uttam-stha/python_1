from fastapi import Depends

def common_parameters(q: str = None,limit: int = 10 ):
    return {"q": q, "limit": limit}

@app.get("/search/")
def search(params: dict = Depends(common_parameters)):
    return {"params": params}