from fastapi import FastAPI , Query
from pydantic import BaseModel
from typing import List

class Student(BaseModel):
    name: str
    marks: int


app = FastAPI()

arr=[{"name":"oJt5K","marks":38},{"name":"HTMz0YGSvt","marks":98},{"name":"TspR1","marks":77},{"name":"AGfzj3tM","marks":61},{"name":"xKY","marks":48},{"name":"Z5xN","marks":91},{"name":"j3E3dEcF","marks":35},{"name":"BC5WtmRu","marks":50},{"name":"r1BB","marks":27},{"name":"NTrzn0Gm4","marks":53},{"name":"r0","marks":13},{"name":"1qGMiadv","marks":60},{"name":"PzBDOpN","marks":35},{"name":"hr","marks":60},{"name":"oq5fD","marks":31},{"name":"FP3nqIb","marks":32},{"name":"SLjq","marks":26},{"name":"Ioue5SKs","marks":77},{"name":"PUwPA","marks":53},{"name":"LlDe3FxNg","marks":97},{"name":"Qu5lV","marks":1},{"name":"lcVA","marks":71},{"name":"N0RoxtfY6","marks":75},{"name":"Ub","marks":29},{"name":"SzL1K7sIq","marks":83},{"name":"YiI","marks":38},{"name":"z86uD","marks":5},{"name":"qlaBAtcMGl","marks":55},{"name":"R","marks":97},{"name":"9","marks":74},{"name":"cvKt2IcxT","marks":56},{"name":"BH8r","marks":5},{"name":"ulJ","marks":72},{"name":"T","marks":15},{"name":"S","marks":94},{"name":"uhQegJcmi","marks":5},{"name":"F","marks":40},{"name":"b8sYf","marks":10},{"name":"e","marks":42},{"name":"5kKm","marks":76},{"name":"b59IZGw1D","marks":80},{"name":"1WME","marks":99},{"name":"n6yxPD","marks":32},{"name":"H","marks":95},{"name":"r","marks":69},{"name":"yEXZ3m5UI","marks":94},{"name":"KizcMLM","marks":91},{"name":"M","marks":57},{"name":"71RLKetx","marks":18},{"name":"hKj3VPClG","marks":78},{"name":"yQQ6jQwc","marks":34},{"name":"EP","marks":56},{"name":"DuZw","marks":91},{"name":"15Q1W","marks":70},{"name":"zN","marks":17},{"name":"4HOa","marks":71},{"name":"ZVomIfIQL","marks":17},{"name":"PU419EXWD","marks":44},{"name":"gE8v9Ed","marks":72},{"name":"Lxf1Kj","marks":42},{"name":"upm2E","marks":98},{"name":"X6wqo4ZdN","marks":74},{"name":"oUNr","marks":82},{"name":"DB","marks":27},{"name":"bqOIZbHvf","marks":37},{"name":"btX","marks":36},{"name":"wbhpybZSc","marks":10},{"name":"N2yDY4","marks":39},{"name":"yOG1s","marks":11},{"name":"3","marks":85},{"name":"RvN1","marks":99},{"name":"r72t","marks":22},{"name":"2B6V","marks":12},{"name":"AX","marks":2},{"name":"hQQfA","marks":65},{"name":"wi0EPgG","marks":97},{"name":"UrI5jx","marks":4},{"name":"6oGQEP","marks":54},{"name":"JFFvw","marks":69},{"name":"PR2luh","marks":6},{"name":"y6","marks":57},{"name":"wPV9CelJo","marks":55},{"name":"j7V","marks":84},{"name":"VnMmB4F9M7","marks":16},{"name":"BzFPDWUhzR","marks":42},{"name":"M4FwU2HiMF","marks":66},{"name":"kno","marks":82},{"name":"QlAgx0UBA9","marks":60},{"name":"lEN","marks":29},{"name":"ig","marks":71},{"name":"kF","marks":9},{"name":"tonAra","marks":70},{"name":"59dJPlqe","marks":70},{"name":"b4Axlv","marks":72},{"name":"2c60","marks":92},{"name":"rqt","marks":95},{"name":"QE53","marks":55},{"name":"Mbdu","marks":6},{"name":"p","marks":56},{"name":"A6i9R","marks":39}]

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI on Vercel!"}


@app.get("/api")
def read_marks(name: List[str] = Query(...)):
    nameX=name[0]
    nameY=name[1]

    marks=[]

    for i in arr:
        if i["name"]==nameX:
            marks.append(i["marks"])

    for i in arr:
        if i["name"]==nameY:
            marks.append(i["marks"])
    print(marks)
    return {"Marks":marks}
   

        


