
# how to add react js in django

1. add .babelrc
2. create a js file (task_list.js) to create React element
3. render bundle on template (task_list.html)
4. change webpack.config.js, handle jsx file


# how to add redis to store cache

1. add redis service in docker-compose.yml, add REDIS_HOST variable
2. add caches setting in settings.py
3. redis command,

MGET :1:product
KEYS *
the value stored in redis is hashed.


django-redis reference:
https://code.tutsplus.com/tutorials/how-to-cache-using-redis-in-django-applications--cms-30178
https://realpython.com/caching-in-django-with-redis/
