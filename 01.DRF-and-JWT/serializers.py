from collections import OrderedDict
from datetime import datetime


class SerializerField:
    def to_representation(self, value):
        return value


class DateTimeField(SerializerField):
    def to_representation(self, value):
        return value.isoformat()


class EmailField(SerializerField):
    pass


class CharField(SerializerField):
    pass


class MetaSerializer(type):
    def __new__(cls, name, bases, attrs):
        fields = [(attr_name, attrs.pop(attr_name))
                  for attr_name, attr in list(attrs.items())
                  if isinstance(attr, SerializerField)]

        attrs['_fields'] = OrderedDict(fields)

        return super().__new__(cls, name, bases, attrs)


class Serializer(metaclass=MetaSerializer):
    def __init__(self, instance):
        self._instance = instance
        self.serialize_instance()

    def serialize_instance(self):
        result = {}

        for field_name, field in self._fields.items():
            result[field_name] = field.to_representation(getattr(self._instance, field_name))

        self.data = result


class Comment(object):
    def __init__(self, email, content, created_at=None):
        self.email = email
        self.content = content

        if created_at is None:
            created_at = datetime.now()

        self.created_at = created_at


class CommentSerializer(Serializer):
    email = EmailField()
    content = CharField()
    created_at = DateTimeField()


comment = Comment(email='radorado@hakbulgaria.com', content='wie naistina li hakvate?')
serializer = CommentSerializer(comment)
print(serializer._fields)
print(serializer.data)
