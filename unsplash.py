import os

UNSPLASH_ACCESS_KEY='-t_MrYB3fgtLStQQikmfYFqXr2sJTrTBO5bPikYu7Tw'

from pyunsplash import PyUnsplash

# instantiate PyUnsplash object
pu = PyUnsplash(api_key=UNSPLASH_ACCESS_KEY)

photos = pu.photos(type_='random', count=1, featured=True, query="niagra falls")
[photo] = photos.entries
print(photo.link_download)