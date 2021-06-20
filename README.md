
# DreamCTF

A quick-and-easy CTF framework for people who love ASCII and minimalism.

Also known as "PokeCTF 2", [this is the original one](https://www.github.com/cyanpencil/PokeCTF)

Here's a screenshot:

![cool ascii](https://user-images.githubusercontent.com/3428362/122681530-fd7d3a00-d1f4-11eb-8b8b-40f0763ba0e3.png)

You can try a live version [here](http://www.cyanpencil.xyz:5000).

Refresh the page to randomize the colorscheme. 

No javascript required.

## Instructions:

for basic usage, (no challenges will be up)

`sudo docker-compose up main db`

then, enter into container `pokectf2_main`

and go to /usr/src/app/

and run `python manage.py create_db`
and then `python manage.py update_chals`

and you're good to go! (on port 8000 of localhost)

# Credits

Colorscheme randomization, and "grimes" wall art are directly ~copied~ inspired 
from sixeyes' [dreamwiki](https://dreamwiki.sixey.es)

Pokemon sprites from: https://www.kaggle.com/kvpratama/pokemon-images-dataset

Blurry text hack from: http://www.briankhuu.com/blog/self/2015/01/14/css-style-for-ascii-art.html
