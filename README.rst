Django Post:
============
**Django blog / news post app.**


Dependancies:
=============
django-content
    git@github.com:praekelt/django-content.git
django-ckeditor
    #TODO: add git url


Models:
=======

Post:
-----
class models.Post
    
Post model extends content.models.ModelBase. Add a news / blog post to the CMS.

API Reference:
~~~~~~~~~~~~~~

FIELDS
******
content
    Richtext field to add content to a post.
extends django-content fields
    See django-content README

METHODS
*******
None

MANAGERS
********
None


Tag Reference
=============

Inclusion Tags
--------------
None

Template Tags
-------------
None
