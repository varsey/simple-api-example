
from typing import TypedDict


class Blog(TypedDict):
    id: int
    title: str
    content: str
    author_id: int


class BlogPayload(TypedDict, total=False):
    title: str
    content: str


class Author(TypedDict):
    id: int
    name: str


BLOGS: dict[int, Blog] = {
    1: {"id": 1, "title": "Blog 1", "author_id": 1, "content": "Content 1"},
    2: {"id": 2, "title": "Blog 2", "author_id": 2, "content": "Content 2"},
    3: {"id": 3, "title": "Blog 3", "author_id": 3, "content": "Content 3"},
}

AUTHORS: dict[int, Author] = {
    1: {"id": 1, "name": "Author 1"},
    2: {"id": 2, "name": "Author 2"},
    3: {"id": 3, "name": "Author 3"},
}
