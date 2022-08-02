import sys
sys.path.append('..')
from typing import Any
from ariadne import ObjectType
from graphql import GraphQLResolveInfo
from data.data import Blog, BlogPayload
from data.DataManipulator import DataManipulator as DM

from schema.types import mutation, query

BLOG_TYPEDEF = """
    type Blog {
        id: ID!
        title: String!
        content: String!
        author: Author!
    }

    input BlogPayload {
        title: String
        content: String
    }

    type Mutation {
        update_blog(id: ID!, payload: BlogPayload!): Blog!
    }
"""

dm = DM()
blog_query = ObjectType("Blog")


@query.field("blogs")
def resolve_blogs(_, info: GraphQLResolveInfo) -> list[Blog]:
    return dm.all_blogs()


@query.field("blog")
def resolve_blog(_, info: GraphQLResolveInfo, id: str) -> Blog:
    return dm.get_blog(int(id))


@mutation.field("update_blog")
def resolve_update_blog(
    _, info: GraphQLResolveInfo, id: str, payload: BlogPayload
) -> Blog:
    return dm.update_blog(int(id), payload)


@blog_query.field("author")
def resolve_blog_author(blog: dict[str, Any], info: GraphQLResolveInfo):
    print(blog)
    return dm.get_author(blog["author_id"])
