## Chat application using django channels

Channels allows you to use WebSockets and other non-HTTP protocols in your Django site.

Channels is a project that takes Django and extends its abilities beyond HTTP - to handle WebSockets, chat protocols, IoT protocols, and more. It’s built on a Python specification called ASGI.

### *Installation*
```
pip install channels==2.4.0
```

### *Once that’s done, you should add channels to your INSTALLED_APPS setting:*
```
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    ...
    'channels',
)
```

### *And set your ASGI_APPLICATION setting to point to that routing object as your root application:*
```
ASGI_APPLICATION = "myproject.asgi.application"
```

### *Then you can start writing routers for consuming consumers*
