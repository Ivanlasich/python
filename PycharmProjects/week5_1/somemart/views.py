import json
from marshmallow.validate import Length, Range
from django import forms
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
from django.utils.decorators import method_decorator
from jsonschema import validate
from jsonschema.exceptions import ValidationError
from marshmallow import Schema, fields
import os
import sys
from marshmallow import ValidationError as MarshmallowError
if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "somemart.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)







from somemart.models import Item, Review



class ReviewSchema(Schema):
    title = fields.Str(validate=Length(min=1, max=64))
    description = fields.Str(validate=Length(min=1, max=1024))
    price = fields.Int(validate=Range(min=1, max=1000000))


class ReviewSchema_1(Schema):
    text = fields.Str(validate=Length(min=1, max=1024))
    grade = fields.Int(validate=Range(min=1, max=10))






REVIEW_SCHEMA = {
    '$schema': 'http://json-schema.org/schema#',
    'type': 'object',
    'properties': {
        'title': {
            'type': 'string',
            'minLength': 1,
            'maxLength': 64,
        },
        'description': {
            'type': 'string',
            'minLength': 1,
            'maxLength': 1024,
        },
        'price': {
            'type': 'integer',
            'minimum': 1,
            'maximum': 1000000
        }
    },
    'required': ['title', 'description', 'price'],
}

EVIEW_SCHEMA_1 = {
    '$schema': 'http://json-schema.org/schema#',
    'type': 'object',
    'properties': {
        'text': {
            'type': 'string',
            'minLength': 1,
            'maxLength': 1024,
        },
        'grade': {
            'type': 'integer',
            'minimum': 1,
            'maximum': 10
        }
    },
    'required': ['text', 'grade'],
}



@method_decorator(csrf_exempt, name='dispatch')
class AddItemView(View):

    def post(self, request):
        try:
            document = json.loads(request.body)
            validate(document, REVIEW_SCHEMA)
            ans = {}
            u = Item.objects.create(title=document['title'], description=document['description'], price=document['price'])
            u.save()
            ans['id'] = u.id

            return JsonResponse(ans, status=201)
        except json.JSONDecodeError:
            return JsonResponse({'errors': 'Invalid JSON'}, status=400)
        except ValidationError as exc:
            return JsonResponse({'errors': exc.message}, status=400)
'''
@method_decorator(csrf_exempt, name='dispatch')
class AddItemView(View):

    def post(self, request):
        try:
            document = json.loads(request.body)


            schema = ReviewSchema(strict=True)
            data = schema.load(document)
            ans = {}
            u = Item.objects.create(title=document['title'], description=document['description'], price=document['price'])
            u.save()
            ans['id'] = u.id
            return JsonResponse(ans, status=201)

        except json.JSONDecodeError:
            return JsonResponse({'errors': 'Invalid JSON'}, status=400)
        except MarshmallowError as exc:
            return JsonResponse({'errors': exc.messages}, status=400)


@method_decorator(csrf_exempt, name='dispatch')
class PostReviewView(View):

    def post(self, request, item_id):
        try:
            document = json.loads(request.body)
            schema = ReviewSchema_1(strict=True)
            data = schema.load(document)

            try:
                a = Item.objects.get(id=item_id)
                u = Review.objects.create(text=document['text'], grade=document['grade'], item = a)
                u.save()
                return JsonResponse(document, status=201)
            except:
                return JsonResponse({'errors': 'id do not exist'}, status=404)

        except json.JSONDecodeError:
            return JsonResponse({'errors': 'Invalid JSON'}, status=400)
        except MarshmallowError as exc:
            return JsonResponse({'errors': exc.messages}, status=400)

'''        

@method_decorator(csrf_exempt, name='dispatch')
class PostReviewView(View):

    def post(self, request, item_id):
        try:
            document = json.loads(request.body)
            validate(document, EVIEW_SCHEMA_1)
            try:
                ans = {}
                a = Item.objects.get(id=item_id);
                u = Review.objects.create(text=document['text'], grade=document['grade'], item = a)
                ans['id'] = u.id
                u.save()
                return JsonResponse(ans, status=201)
            except:
                return JsonResponse({'errors': 'id do not exist'}, status=404)

        except json.JSONDecodeError:
            return JsonResponse({'errors': 'Invalid JSON'}, status=400)
        except ValidationError as exc:
            return JsonResponse({'errors': exc.message}, status=400)


class GetItemView(View):

    def get(self, request, item_id):
        try:
            b = Item.objects.get(id=item_id)
            dict = model_to_dict(b)
            d = Review.objects.filter(item=b).order_by('-id')[0:5]
            list = []
            for c in d:
                p = model_to_dict(c)
                p.pop('item')
                list.append(p)
            dict["reviews"] = list

            return JsonResponse(dict, status=200)
        except Item.DoesNotExist:
            return JsonResponse(status=404, data={})
A = Item.objects.all()
print(len(A))