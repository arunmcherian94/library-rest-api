from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
 
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
       'MemberCRUD': reverse('crud:member_route', request=request, format=format),
       'BookCRUD': reverse('crud:book_route', request=request, format=format),
       'BookBorrowReturn': reverse('crud:book_action_route', request=request, format=format),
    })