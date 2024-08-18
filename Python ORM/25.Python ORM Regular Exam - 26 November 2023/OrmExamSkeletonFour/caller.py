import os
import django


# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from django.db.models import Count, Q, Avg
from main_app.models import Author, Article


def get_authors(search_name=None, search_email=None):
    authors = None
    if search_name is None and search_email is None:
        return ""

    if search_name is not None and search_email is not None:
        # query = Q(full_name__icontains=search_name) and Q(email__icontains=search_email)
        authors = Author.objects.filter(full_name__icontains=search_name, email__icontains=search_email).order_by('-full_name')
    elif search_name is not None:
        # query = Q(full_name__icontains=search_name)
        authors = Author.objects.filter(full_name__icontains=search_name).order_by('-full_name')
    elif search_email is not None:
        # query = Q(email__icontains=search_email)
        authors = Author.objects.filter(email__icontains=search_email).order_by('-full_name')
    # authors = Author.objects.filter(query).order_by('-full_name')
    # if not authors:
    #     return ""

    result = []
    [result.append(f'Author: {a.full_name}, email: {a.email}, status: {"Banned" if a.is_banned else "Not Banned"}')
        for a in authors if a]

    return '\n'.join(result) if result else ""


# print(get_authors("o", "@"))


def get_top_publisher():
    author = Author.objects.annotate(article_count=Count('articles')).order_by('-article_count', 'email').first()

    if author is None or author.article_count == 0:
        return ""
    return f"Top Author: {author.full_name} with {author.article_count} published articles."


# print(get_top_publisher())

def get_top_reviewer():
    author = Author.objects.prefetch_related('reviews').annotate(
        reviews_count=Count('reviews'),
    ).order_by('-reviews_count', 'email').first()
    if not author or not author.reviews_count:
        return ''
    # author = Author.objects.annotate(reviews_count=Count("reviews")).order_by('-reviews_count', 'email').first()
    # if author is None or author.reviews_count == 0:
    #     return ""
    return f"Top Reviewer: {author.full_name} with {author.reviews_count} published reviews."


def get_latest_article():
    article = Article.objects.prefetch_related('authors', 'reviews').annotate(
        average_rating=Avg('reviews__rating')).order_by('-published_on').first()
    if article is None:
        return ""
    number_reviews = article.reviews.count()
    avg_rating = article.average_rating if article.average_rating else 0.0
    return (f"The latest article is: {article.title}. "
            f"Authors: {', '.join(a.full_name for a in article.authors.all().order_by('full_name'))}."
            f" Reviewed: {number_reviews if number_reviews else 0} times. Average Rating: {avg_rating:.2f}.")


# print(get_latest_article())

def get_top_rated_article():
    top_article = (
        Article.objects
        .annotate(avg_rating=Avg('reviews__rating'), num_reviews=Count('reviews'))
        .filter(num_reviews__gt=0)
        .order_by('-avg_rating', 'title')
        .first()
    )

    if top_article:
        return (
            f"The top-rated article is: {top_article.title}, "
            f"with an average rating of {top_article.avg_rating:.2f}, "
            f"reviewed {top_article.num_reviews} times."
        )
    else:
        return ""


def ban_author(email=None):
    if email is None:
        return "No authors banned."

    try:
        author = Author.objects.get(email=email)
    except Author.DoesNotExist:
        return "No authors banned."

    num_reviews = author.reviews.count()
    author.reviews.all().delete()

    author.is_banned = True
    author.save()

    return f"Author: {author.full_name} is banned! {num_reviews} reviews deleted."

