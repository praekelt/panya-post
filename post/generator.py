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
                "state": "published",
                "image": random.sample(IMAGES, 1)[0],
                "sites": {
                    "model": "sites.Site",
                    "fields": { 
                        "name": "example.com"
                    }
                },
            },
        })

    # gen post photo sizes
    objects.append({
        "model": "photologue.PhotoSize",
        "fields": {
            "name": "gallery_small",
            "width": "188",
            "height": "104",
            "crop": True,
        },
    })
    
    load_json(objects)
