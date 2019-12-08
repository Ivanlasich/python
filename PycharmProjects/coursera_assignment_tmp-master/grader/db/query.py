from datetime import datetime
from django.utils import timezone
from django.db.models import Q, Count, Avg
from pytz import UTC
import os
import sys


#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "grader.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            import django
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise
    execute_from_command_line(sys.argv)










from db.models import User, Blog, Topic


def create():
    a = User(first_name='u1', last_name='u1')
    a.save()
    b = User(first_name='u2', last_name='u2')
    b.save()
    c = User(first_name='u3', last_name='u3')
    c.save()
    d = Blog(title = 'blog1', author = a)
    d.save()
    e = Blog(title = 'blog2', author = a)
    e.save()
    d.subscribers.add(a, b)
    d.save()
    e.subscribers.add(b)
    e.save()
    f = Topic(title = "topic1", blog = d, author = a)
    f.save()
    g = Topic(title = "topic2_content", blog = d, author = c, created = "2017-01-01")
    g.save()
    f.likes.add(a, b, c)
    f.save()

def edit_all():
    a = User.objects.all()
    for i in a:
        i.first_name = "uu1"
        i.save()


def edit_u1_u2():
    a = User.objects.all()
    for i in a:
        if((i.first_name == "u1")|(i.first_name == "u2")):
            i.first_name = "uu1"
            i.save()


def delete_u1():
    a = User.objects.all()
    for i in a:
        if (i.first_name == "u1"):
            i.delete()


def unsubscribe_u2_from_blogs():
    c = User.objects.all().get(first_name='u2')
    b = Blog.objects.all()
    for i in b:
        a = i.subscribers
        a.remove(c)


def get_topic_created_grated():

    return Topic.objects.filter(created__gt="2018-01-01")


def get_topic_title_ended():
    return Topic.objects.filter(title__endswith="content")


def get_user_with_limit():
    return User.objects.order_by('-id')[:2]

def get_topic_count():
    b = Blog.objects.all()
    for i in b:
        ro = Blog.objects.annotate(topic_count=Count("topic__blog"))

    for i in range(len(b)):
        ro[0].topic_count = Blog.objects.filter(topic__blog=b[i]).count()
    a = ro.order_by('topic__blog')
    return a


def get_avg_topic_count():
    a = Blog.objects.all().annotate(topic_count=Count('topic')).aggregate(Avg('topic_count'))['topic_count__avg']
    d = {'avg': a}
    return d


def get_blog_that_have_more_than_one_topic():
    return Blog.objects.all().annotate(topic_count=Count('topic')).filter(topic_count__gt = 1)


def get_topic_by_u1():
    return Topic.objects.all().filter(author__first_name="u1")


def get_user_that_dont_have_blog():
    return User.objects.all().filter(blog__isnull=True).order_by('pk')


def get_topic_that_like_all_users():
    return Topic.objects.filter(likes=User.objects.all())


def get_topic_that_dont_have_like():
    return Topic.objects.filter(likes__isnull=True)

def start():
    a = User.objects.all()
    b = a[0]
    b.first_name = "u1"
    b.save()
    b = a[1]
    b.first_name = "u2"
    b.save()
    b = a[2]
    b.first_name = "u3"
    b.save()
    for i in a:
        print(i.first_name)

def deli():
    User.objects.all().delete()
    Blog.objects.all().delete()
    Topic.objects.all().delete()
#print(Topic.objects.get(title = "topic1").likes.get(first_name='U3').first_name)
