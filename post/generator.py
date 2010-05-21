import random

from generate import IMAGES
from generate.json_loader import load_json

POST_COUNT = 20

def generate():
    objects = []

    # gen post objects
    for i in range(1, POST_COUNT + 1):
        objects.append({
            "model": "post.Post",
            "fields": {
                "title": "Post %s Title" % i,
                "description": "Post %s description with some added text to verify truncates where needed." % i,
                "state": "published",
                "image": random.sample(IMAGES, 1)[0],
                "content": "<strong>strong</strong><i>italic</i>",
                "sites": {
                    "model": "sites.Site",
                    "fields": { 
                        "name": "example.com"
                    }
                },
            },
        })

    load_json(objects)
