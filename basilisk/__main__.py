import uvicorn

from basilisk import Basilisk, BasiliskSchema


if __name__ == "__main__":
    schema = BasiliskSchema()
    basilisk = Basilisk(schema)

    uvicorn.run(
        basilisk,
        port=8000,
    )
