from .data import Blog, BLOGS, Author, AUTHORS, BlogPayload


class NotFoundError(Exception):
    pass


class DataManipulator:

    def all_blogs(self) -> list[Blog]:
        return list(BLOGS.values())

    def get_blog(self, blog_id: int) -> Blog:
        if not BLOGS.get(blog_id):
            raise NotFoundError("Blog not found")
        return BLOGS[blog_id]

    def update_blog(self, blog_id: int, payload: BlogPayload) -> Blog:
        blog = BLOGS.get(blog_id)
        if not blog:
            raise NotFoundError("Blog not found")
        for key, value in payload.items():
            blog[key] = value
        return blog

    def all_authors(self) -> list[Author]:
        return list(AUTHORS.values())

    def get_author(self, author_id: int) -> Author:
        if not AUTHORS.get(author_id):
            raise NotFoundError("Author not found")
        return AUTHORS[author_id]
