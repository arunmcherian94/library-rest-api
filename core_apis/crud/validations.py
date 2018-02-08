from core_apis import settings
from rest_framework import status

'''
This is a makeshift implementation for a very basic validation.
Code redundancy is purposely ignored. Validation to be done via serialzers ideally.
'''

 
class DataValidation(object):

    def member_validate(self, method, request_data):
        print method
        response = {"success":True,"message":""}
        if method.lower() in ['put', 'delete']:
            print 'weird'
            email = request_data.query_params.get('email')
            if not email:
                response['success'] = False
                response['message'] = "Please provide email parameter in query string."
                response['status'] = status.HTTP_400_BAD_REQUEST
                return response

        if method.lower() in ['put','post']:
            if not request_data.data:
                response['success'] = False
                response['message'] = "Please provide the fields to be updated in request body."
                response['status'] = status.HTTP_400_BAD_REQUEST
                return response

            elif request_data.data.get('member_type'):
                if request_data.data.member_type not in settings.MEMBER_TYPES:
                    response['success'] = False
                    response['message'] = "member_type should be A or U only."
                    response['status'] = status.HTTP_400_BAD_REQUEST
                    return response   

        if method.lower() in ['post']:
            data = request_data.data
            if not (data.get('email') and data.get('phone') and data.get('first_name') and data.get('expires_on')):
                response['success'] = False
                response['message'] = "Please check the email/phone/first_name/expires_on fields."
                response['status'] = status.HTTP_400_BAD_REQUEST         
                return response

        return response

    
    def book_master_validate(self, method, request_data):
        response = {"success":True,"message":""}
        if method.lower() in ['put', 'delete']:
            print 'weird'
            isbn = request_data.query_params.get('isbn')
            if not isbn:
                response['success'] = False
                response['message'] = "Please provide isbn parameter in query string."
                response['status'] = status.HTTP_400_BAD_REQUEST
                return response

        if method.lower() in ['put','post']:
            if not request_data.data:
                response['success'] = False
                response['message'] = "Please provide the fields to be updated in request body."
                response['status'] = status.HTTP_400_BAD_REQUEST
                return response

        if method.lower() in ['post']:
            data = request_data.data
            if not (data.get('author_email') and data.get('title') and data.get('isbn')):
                response['success'] = False
                response['message'] = "Please check the author_email/isbn/title fields."
                response['status'] = status.HTTP_400_BAD_REQUEST         
                return response

        return response

    def book_action_validate(self, method, request_data):

        response = {"success":True,"message":""}
        data = request_data.data
        if method.lower() in ['post']:
            if not data:
                response['success'] = False
                response['message'] = "Please provide book_id/email in request body."
                response['status'] = status.HTTP_400_BAD_REQUEST
                return response

            elif not (data.get('book_id') and data.get('email')):
                response['success'] = False
                response['message'] = "Please check the book_id/email fields."
                response['status'] = status.HTTP_400_BAD_REQUEST         
                return response
        
        elif method.lower() in ['delete']:
            book_id = request_data.query_params.get('book_id')
            if not book_id:
                response['success'] = False
                response['message'] = "Please provide book_id parameter in query string."
                response['status'] = status.HTTP_400_BAD_REQUEST
                return response

        return response