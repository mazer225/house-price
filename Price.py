from pydantic import BaseModel


class Cost(BaseModel):
    area: int
    bedrooms: int
    bathrooms: int
    stories: int
    parking: int
    furnishingstatus: str
