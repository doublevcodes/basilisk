from fastapi import FastAPI
from strawberry import Schema
from strawberry.asgi import GraphQL


class Basilisk(FastAPI):
    def __init__(self, schema: Schema) -> None:
        super().__init__()
        self.schema = schema
        self.graphql_app = GraphQL(self.schema)
        self.add_route("/graphql", self.graphql_app)
        self.add_websocket_route("/graphql", self.graphql_app)
