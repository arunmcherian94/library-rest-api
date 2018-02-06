from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
 
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
       'member_operations': reverse('crud:member_route', request=request, format=format),
       'book_operations': reverse('crud:book_route', request=request, format=format),
    })