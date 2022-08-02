import sys
sys.path.append('..')
from data.data import Author
from graphql.type.definition import GraphQLResolveInfo
from data.DataManipulator import DataManipulator as DM

from schema.types import query

AUTHOR_TYPEDEF = """
    type Author {
        id: ID!
        name: String!
    }
"""

dm = DM()

@query.field("authors")
def resolve_authors(_, info: GraphQLResolveInfo) -> list[Author]:
    return dm.all_authors()


@query.field("author")
def resolve_author(_, info: GraphQLResolveInfo, id: str) -> Author:
    return dm.get_author(int(id))
