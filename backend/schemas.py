from pydantic import BaseModel


class FirePredictionInput(BaseModel):
    Temperature: float
    RH: float
    Ws: float
    Rain: float
    FFMC: float
    DMC: float
    ISI: float
    Classes: float
    Region: float
