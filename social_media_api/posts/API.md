# Posts & Comments API

## Endpoints

### Posts
- `GET /posts/` — List posts (paginated, filterable by title/content)
- `POST /posts/` — Create post (auth required)
- `GET /posts/{id}/` — Retrieve post
- `PUT /posts/{id}/`, `PATCH /posts/{id}/` — Update post (owner only)
- `DELETE /posts/{id}/` — Delete post (owner only)

### Comments
- `GET /comments/` — List comments (paginated)
- `POST /comments/` — Create comment (auth required)
- `GET /comments/{id}/` — Retrieve comment
- `PUT /comments/{id}/`, `PATCH /comments/{id}/` — Update comment (owner only)
- `DELETE /comments/{id}/` — Delete comment (owner only)

## Filtering
- Filter posts by `title` or `content`: `/posts/?search=keyword`

## Examples
- Create Post:
    ```http
    POST /posts/
    {
        "title": "Hello World",
        "content": "This is a new post"
    }
    ```
- Create Comment:
    ```http
    POST /comments/
    {
        "post": 1,
        "content": "Great post!"
    }
    ```

## Authentication
- Use DRF token or session authentication.
