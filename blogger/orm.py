# orm_operations.py

import os
import django

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
django.setup()

from blog.models import Post
from CommentAppp.models import Comment

# Create at least 3 posts with different titles, categories, and content.
def create_posts():
    Post.objects.create(title='Post 1', category='Category 1', content='Content 1')
    Post.objects.create(title='Post 2', category='Category 2', content='Content 2')
    Post.objects.create(title='Post 3', category='Category 3', content='Content 3')

# Query and display all posts in a specific category.
def get_posts_by_category(category):
    posts = Post.objects.filter(category=category)
    for post in posts:
        print(f'Title: {post.title}, Category: {post.category}, Content: {post.content}')

# Update the content of one of the posts.
def update_post_content(post_id, new_content):
    post = Post.objects.get(id=post_id)
    post.content = new_content
    post.save()

# Delete a post.
def delete_post(post_id):
    Post.objects.filter(id=post_id).delete()

# Create at least 3 comments related to different blog posts.
def create_comments():
    Comment.objects.create(post_id=1, content='Comment 1')
    Comment.objects.create(post_id=2, content='Comment 2')
    Comment.objects.create(post_id=3, content='Comment 3')

# Query and display all comments related to a specific post.
def get_comments_by_post(post_id):
    comments = Comment.objects.filter(post_id=post_id)
    for comment in comments:
        print(f'Post ID: {comment.post_id}, Content: {comment.content}')

# Update the content of one of the comments.
def update_comment_content(comment_id, new_content):
    comment = Comment.objects.get(id=comment_id)
    comment.content = new_content
    comment.save()

# Delete a comment.
def delete_comment(comment_id):
    Comment.objects.filter(id=comment_id).delete()

def main():
    # Perform the required ORM operations here
    create_posts()
    get_posts_by_category('Category 1')
    update_post_content(1, 'New content')
    delete_post(2)
    create_comments()
    get_comments_by_post(1)
    update_comment_content(1, 'Updated comment content')
    delete_comment(2)

if __name__ == '__main__':
    main()