# Likes & Notifications API

## Like a Post
**Endpoint:** `/posts/<int:pk>/like/`  
**Method:** POST  
**Auth:** Required  
**Request:** None (just login and post)  
**Response:**  
```json
{
  "detail": "Post liked."
}
```
**Error:**  
```json
{
  "detail": "You have already liked this post."
}
```

## Unlike a Post
**Endpoint:** `/posts/<int:pk>/unlike/`  
**Method:** POST  
**Auth:** Required  
**Response:**  
```json
{
  "detail": "Post unliked."
}
```
**Error:**  
```json
{
  "detail": "You have not liked this post."
}
```

## View Notifications
**Endpoint:** `/notifications/`  
**Method:** GET  
**Auth:** Required  
**Response Example:**  
```json
[
  {
    "id": 1,
    "recipient": 2,
    "actor_username": "user1",
    "verb": "liked your post",
    "target_repr": "Post object (1)",
    "timestamp": "2025-08-24T10:01:23Z",
    "read": false
  }
]
```

## Supported Notification Types
- New followers
- Likes on posts
- Comments on posts

**How It Works:**  
- Users can like or unlike posts.  
- Post owners receive a notification when someone else likes their post.  
- Notifications are displayed via `/notifications/` endpoint, with unread ones shown first.

## Benefits
- Drives engagement and interaction
- Users stay informed about what’s happening around their content

## Testing
- Use Django's test client or Postman to send requests to the endpoints.
- Automated tests cover liking, unliking, and notification creation.
