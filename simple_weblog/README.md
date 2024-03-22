```markdown
# Django Blog

This is a simple Django project for creating a blog with basic endpoints to manage articles and comments.

## Requirements

- Python (3.6, 3.7, 3.8, 3.9)
- Django (3.0+)

## Installation

1. Clone the repository:

```bash
git clone <repository_url>
cd django-blog
```

2.  Install the dependencies:

```bash
pip install -r requirements.txt
```

3. Apply migrations:

```bash
python manage.py migrate
```

4. Run the development server:

```bash
python manage.py runserver
```

The development server will start at `http://127.0.0.1:8000/`.

## Endpoints

### Get Article List

```
GET /articles/
```

Returns a list of all articles.

### Get Article Details

```
GET /articles/<article_id>/
```

Return details of a specific article.

### Filter Articles by Topic

```
GET /articles/filter/<topic>/
```

Returns a list of articles filtered by topic.

### Post Comment

```
POST /articles/<article_id>/comment/
```

Posts a comment on a specific article.

## Models

### Article

- `id`: IntegerField (auto-generated)
- `title`: CharField (max_length=100)
- `content`: TextField
- `topic`: CharField (max_length=50)

### Comment

- `id`: IntegerField (auto-generated)
- `article`: ForeignKey to Article model (related_name='comments')
- `text`: TextField
- `author`: CharField (max_length=50)

## Contributing

Contributions are welcome! Please feel free to submit a pull request.
