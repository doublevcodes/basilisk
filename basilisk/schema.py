import strawberry
from strawberry import Schema

from basilisk import __version__


@strawberry.type
class Query:
    pass


@strawberry.type
class Mutation:
    pass


class BasiliskSchema(Schema):
    """A schema for the Basilisk GraphQL API."""

    version = __version__

    def __init__(self) -> None:
        super().__init__(
            query=Query,
            mutation=Mutation,
        )
