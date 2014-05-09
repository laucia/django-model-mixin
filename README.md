django-model-mixin
==================

A set of useful and common mixin to avoid code duplication when making django models

## Setup
Install with pip
```
pip install git+git://github.com/laucia/django-model-mixin.git
```
Add ``modelmixin`` to your ``settings.py`` ``INSTALLED_APPS``
```
INSTALLED_APPS = (
    ...
    'modelmixin',
)
```

## Usage

```
from modelmixin.models import Mixin1, Mixin2

class CoolModel(Mixin1,Mixin2):
    mycoolField = models.CoolField()
    ...
```


## Available Mixins

### OrderedMixin
A mixin with a field that represents a relative order.

adds an ``ordering` field for this purpose.

One should make the ``Meta`` class inherit of ``OrderedMixin.Meta`` to benefit 
from the ordering effect when getting request

```
from modelmixin.models import OrderedMixin

class CoolModel(OrderedMixin):
    mycoolField = models.CoolField()
    ...
    class Meta(OrderedMixin.Meta)
        verbose_name ...
```

### DescriptiveMixin

A mixin that adds a ``name`` and an optional ``description`` text.

Also override ``__unicode__`` to return the ``name`` field by default.

### ModTrackingMixin

A mixin to track the object edition and creation

Adds a ``created`` and a ``created`` ``DateTimeField`` for this purpose
