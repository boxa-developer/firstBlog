from rest_framework.decorators import api_view,authentication_classes,permission_classes
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Post, Author, Tag
from .serialzers import AuthorSerializer, PostSerializer, TagSerializer
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated


# General Info About API
@api_view(['GET'])
@csrf_exempt
def api_info(request):
    content = {
        'start_text': 'FIRST BLOG API Reference',
    }
    return JsonResponse(content)


# Post API views
@api_view(['GET'])
@csrf_exempt
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def all_posts(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return JsonResponse({'posts': serializer.data}, safe=False, status=status.HTTP_200_OK)


# Authors API view
@api_view(['GET'])
@csrf_exempt
def authors(request):
    auths = Author.objects.all()
    serializer = AuthorSerializer(auths, many=True)
    return JsonResponse({'posts': serializer.data}, safe=False, status=status.HTTP_200_OK)


@api_view(['POST'])
@csrf_exempt
def add_auth(request):
    data = request.data
    try:
        auth = Author()
        auth.author_firstname = data['fname']
        auth.author_lastname = data['lname']
        serializer = AuthorSerializer(auth)
        auth.save()
        return JsonResponse({'Author': serializer.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'err': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'err': 'status 500'},
                            safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR
                            )


# Tags API views
@api_view(['GET'])
@csrf_exempt
def get_tags(request):
    all_tags = Tag.objects.all()
    serializer = TagSerializer(all_tags, many=True)
    return JsonResponse({'tags': serializer.data}, safe=False, status=status.HTTP_200_OK)


@api_view(['GET'])
@csrf_exempt
def get_tag(request, tag_id):
    tag = Tag.objects.get(id=tag_id)
    content = {
        'id': tag_id,
        'tag': tag.tag_title
    }
    return JsonResponse(content, safe=False, status=status.HTTP_200_OK)


@api_view(['POST'])
@csrf_exempt
def add_tag(request):
    data = request.data
    try:
        tag = Tag()
        tag.tag_title = data['tag']
        tag.save()
        return JsonResponse('Success', safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'err': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'err': 'status 500'},
                            safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR
                            )


@api_view(['PUT'])
@csrf_exempt
def update_tag(request):
    data = request.data
    tag = Tag.objects.get(id=data['id']).update(tag_title=data['tag'])
    return JsonResponse('Successfully Updated!', safe=False, status=status.HTTP_200_OK)


@api_view(['DELETE'])
@csrf_exempt
def delete_tag(request):
    data = request.data
    tag = Tag.objects.get(id=data['id'])
    tag.delete()
    return JsonResponse('Successfully Deleted!', safe=False, status=status.HTTP_204_NO_CONTENT)


