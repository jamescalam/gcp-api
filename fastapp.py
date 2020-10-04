from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

DATA = {
    'places':
        ['rome',
         'london',
         'new york city',
         'los angeles',
         'brisbane',
         'new delhi',
         'beijing',
         'paris',
         'berlin',
         'barcelona']
}


class PlacesItem(BaseModel):
    location: str

    
@app.get("/places")
async def get_places():
    # return our data
    return {'data': DATA}

@app.post("/places")
async def post_place(item: PlacesItem):
    if item.location in DATA['places']:
        # if place is already present, we don't append to DATA
        # so just return response with message saying already exists
        return {'data': DATA,
                'message': 'location already exists'}
    else:
        # if it is not present, append to places
        DATA['places'].append(item.location)
        # return response
        return {'data': DATA,
                'message': 'location added'}

@app.delete("/places")
async def delete_place(item: PlacesItem):
    if item.location in DATA['places']:
        # if place is present, delete it
        DATA['places'].remove(item.location)
        # return response confirming deletion
        return {'data': DATA,
                'message': 'location deleted'}
    else:
        # if it is not present, just return response
        return {'data': DATA,
                'message': 'location does not exist'}


#if __name__ == '__main__':
#    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
