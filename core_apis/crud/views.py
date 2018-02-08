# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from datetime import timedelta, datetime
from django.http import JsonResponse
import json

#Django rest framework imports
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
#Settings import
from core_apis import settings

#Model imports
from models import Member, Book_master, Author, Book, BookAction

#Import serializers here
from serializers import MemberSerializer, BookSerializer, BookActionSerializer

#Import custom validations here.
from validations import DataValidation
validation = DataValidation()

# Holds the model instances against a model_name key. Used in GenericHandler class
model_list = {"Member":Member, "Book_master":Book_master, "BookAction":BookAction}
serializer_list = {"Member":MemberSerializer,"Book_master":BookSerializer, "BookAction":BookActionSerializer}

# Making use of class based views here

class GenericHandler(object):
    """ Generic logic for read/update/delete functionalities. """

    '''
    model_name : Name of the model. Passed from child classes. eg : Member
    method : The http method for which the function is called
    request : The request object which contains data, query_params
    query_param : The name of mandatory query_param if any
    '''

    def validate(self, model_name, method, request):
        """ Data validation for the requests. """
        # Validation needs to be handled by the serializer
        # Keeping it basic for simplicity now.
        if model_name == "Member":
            self.response = validation.member_validate(method,request)
        elif model_name == "Book_master":
            self.response = validation.book_master_validate(method,request)
        elif model_name == "BookAction":
            self.response = validation.book_action_validate(method,request)
        return self.response

    def read(self, model_name, request, query_param):
        """ Read operation logic. """
        kwargs = {}
        get_all = False
        query_param_value = request.query_params.get(query_param)
        if not query_param_value:
            get_all = True
        kwargs[query_param] = query_param_value
        try:
          if get_all:
              model_data = model_list[model_name].objects.all()
          else:
              model_data = model_list[model_name].objects.filter( **kwargs)
          if not model_data:
              message = {"message":"No "+model_name+" found for: "+query_param_value, "status":status.HTTP_200_OK}
              return message

          serializer = serializer_list[model_name](model_data, many=True)
          message = {"message":serializer.data, "status":status.HTTP_200_OK}
          return message
          
        except Exception as e:
            print e
            message = {"message":str(e), "status":status.HTTP_400_BAD_REQUEST}
            return message

    def update(self, model_name, request, query_param):
        """ Update operation logic. """
        kwargs = {}
        data=request.data
        query_param_value = request.query_params.get(query_param)
        kwargs[query_param] = query_param_value
        # was not able to use kwargs with .get()
        update_model_data = model_list[model_name].objects.filter( **kwargs).first()
        if not update_model_data:
            message = {"message":"Not updating. No "+model_name+" was found for: "+query_param_value, "status":status.HTTP_400_BAD_REQUEST}
            return message

        for field_name in data:
            setattr(update_model_data, field_name, data.get(field_name))
        try:
            # update() gave issue on modified_date . Hence not doing this
            # member_updated = Member.objects.filter(email=email).update(**kwargs)
            update_model_data.save()
            message = {"message":model_name+" details updated successfully.","status":status.HTTP_200_OK}
            return message
        except Exception as e:
            print e
            message = {"message":str(e), "status":status.HTTP_400_BAD_REQUEST}
            return message

    def remove(self, model_name, request, query_param):
        """ Delete logic. """
        kwargs = {}
        data=request.data
        query_param_value = request.query_params.get(query_param)
        kwargs[query_param] = query_param_value
        try:
            model_deleted = model_list[model_name].objects.filter( **kwargs).update(is_deleted=True)
            if not model_deleted:
                message = {"message":"No "+model_name+" found with this "+query_param+". Did not delete.", "status":status.HTTP_200_OK}
                return message
            message = {"message":model_name+" entry deleted successfully.","status":status.HTTP_200_OK}
            return message
        except Exception as e:
            print e
            message = {"message":str(e), "status":status.HTTP_400_BAD_REQUEST}
            return message



class MemberOperations(APIView, GenericHandler):
    """
    Class which handles Member actions.
    Inherited from APIView class.
    """

    '''
    Member CRUD operations are done here.
    Function is written for each https method that is allowed.
    Operations are written in GenericHandler class. 
    '''

    # Over-ride the allowed http method names
    http_method_names = [u'get', u'post', u'put', u'delete']

    def get(self, request, format=None):
        """ To fetch member details by email. """
        # email needs to be sent as a query string
        is_valid = self.validate("Member", "get", request)
        if not is_valid.get('success'):
            return Response(is_valid.get('message'),is_valid.get('status'))
        response = self.read("Member",request,"email")
        return Response(response.get('message'),response.get('status'))    

    def post(self, request, format=None):
        """ To create/add a new member. """

        '''
        email : email_id of the member. Must be unique
        first_name, phone, expires_on are mandatory parameters
        member_type : A (admin) or U (user) are the allowed values. A by default
        '''
        data=request.data
        response = self.validate("Member", "post", request)
        if not response.get('success'):
            return Response(response.get('message'),response.get('status'))
        email = data.get('email')
        first_name = data.get('first_name')
        last_name = data.get('last_name','')
        phone = data.get('phone')
        member_type = data.get('member_type','A')
        expires_on = data.get('expires_on')
        try:
            new_member = Member(first_name=first_name, last_name=last_name,email=email,phone=phone,member_type=member_type,expires_on=expires_on)
            new_member.save()
            message = "New member added successfully."
            return Response(message, status=status.HTTP_201_CREATED)
        except Exception as e:
            print e
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, format=None):
        """ To remove a member. Soft delete. """
        '''
        email of member to be deleted must be passed in the query params
        '''
        is_valid = self.validate("Member", "delete", request)
        if not is_valid.get('success'):
            return Response(is_valid.get('message'),is_valid.get('status'))
        response = self.remove("Member",request,"email")
        return Response(response.get('message'),response.get('status'))

    def put(self, request, format=None):
        """ To update member details. """
        '''
        email of member to be updated must be passed in the query params 
        '''
        is_valid = self.validate("Member", "put", request)
        if not is_valid.get('success'):
            return Response(is_valid.get('message'),is_valid.get('status'))
        response = self.update("Member",request,"email")
        return Response(response.get('message'),response.get('status'))



class BookOperations(APIView, GenericHandler):
    """ Class which handles book CRUD operations. """

    # Over-ride the allowed http method names
    http_method_names = [u'get', u'post', u'put', u'delete']

    def get(self, request, format=None):
        """ To fetch book details. """
        '''
        isbn : should be passed in the query string
        '''
        is_valid = self.validate("Book_master", "get", request)
        if not is_valid.get('success'):
            return Response(is_valid.get('message'),is_valid.get('status'))
        response = self.read("Book_master",request,"isbn")
        return Response(response.get('message'),response.get('status'))

    def delete(self, request, format=None):
        """ To delete a book. Soft delete. """
        '''
        isbn : mandatory in query string
        '''
        is_valid = self.validate("Book_master", "delete", request)
        if not is_valid.get('success'):
            return Response(is_valid.get('message'),is_valid.get('status'))
        response = self.remove("Book_master",request,"isbn")
        return Response(response.get('message'),response.get('status'))

    def put(self, request, format=None):
        """ To update a book detail. """
        '''
        isbn : mandatory query string param
        '''
        is_valid = self.validate("Book_master", "put", request)
        if not is_valid.get('success'):
            return Response(is_valid.get('message'),is_valid.get('status'))
        response = self.update("Book_master",request,"isbn")
        return Response(response.get('message'),response.get('status'))

    def post(self, request, format = None):
        """ To add a new book. """

        '''
        author_email : email_id of a registered author. Author needs to be added first
        isbn : book isbn (unique)
        title : book title
        no_of_copies : Total number of copies for this book.

        '''
        data=request.data
        response = self.validate("Book_master", "post", request)
        if not response.get('success'):
            return Response(response.get('message'),response.get('status'))
        author_email = data.get('author_email')
        isbn = data.get('isbn')
        title = data.get('title')
        no_of_copies = data.get('no_of_copies',1)     
        try:
            # To fetch multiple authors if mentioned
            # Expects an author to be already created
            # not handling get_or_create for now.
            author = Author.objects.get(email=author_email)
            new_book_master = Book_master(author=author,isbn=isbn, title=title, no_of_copies=no_of_copies)
            new_book_master.save()
            # create book copies and save them in Book table
            for i in xrange(no_of_copies):
                Book.objects.create(book_master=new_book_master)
            message = "New book added successfully."
            return Response(message, status=status.HTTP_201_CREATED)

        except Author.DoesNotExist:
            print "Author not registered."
            message = "Author is not registered. Please add the author."
            return Response(message, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            print e
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)



class BookActions(APIView, GenericHandler):
    """
    Class which handles Book borrow/return actions.
    """

    '''
    Supports get/post/put methods.
    '''

    # Over-ride the allowed http method names
    http_method_names = [u'get', u'post', u'delete']

    '''
    def get(self, request, format = None):
        """ To fetch list of borrowed books for given user. """
        email = request.query_params.get('email')
        if not email:
            return Response("Provide email parameter in query string.",status=status.HTTP_400_BAD_REQUEST)
        try:
          # member = Member.objects.get(email=email)
          # print member
          model_data = BookAction.objects.filter(is_returned=False)
          if not model_data:
              return Response("No borrowed books found for: "+email,status=status.HTTP_200_OK)
          serializer = BookActionSerializer(model_data, many=True)
          message = serializer.data
          return Response(message,status=status.HTTP_200_OK)
          
        except Member.DoesNotExist:
            print "Member not registered."
            message = "Member is not registered. Please add the member."
            return Response(message, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            print e
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST) 
    '''
    def post(self, request, format=None):
        """ To borrow a book. """
        '''
        book_id : Mandatory. The unique copy_id of the book. (uuid)
        email : Mandatory. Email id of the member borrowing the book.
        '''
        data=request.data
        response = self.validate("BookAction", "post", request)
        if not response.get('success'):
            return Response(response.get('message'),response.get('status'))

        book_id = data.get('book_id')
        email = data.get('email')
        try:
            # Issue the book only if it is not deleted from the inventory.
            requesting_member = Member.objects.get(email=email,is_deleted=False)
            book = Book.objects.get(book_id=book_id, available=True, book_master__is_deleted=False)
            borrowed_book = BookAction(copy =book, borrowed_date=datetime.now(), due_date=datetime.now()+timedelta(settings.DAYS_TO_RETURN))
            #Create a new book
            borrowed_book.save()
            # update the ManyToMany field member
            borrow = borrowed_book.member.add(requesting_member)
            #  set this copy to not available
            book.available = False
            book.save()
            message = "Borrowed successfully."
            return Response(message, status=status.HTTP_200_OK)
        
        except Member.DoesNotExist:
            print "Member not registered/active/is deleted."
            message = "Member not registered/active/is deleted."
            return Response(message, status=status.HTTP_400_BAD_REQUEST)
        
        except Book.DoesNotExist:
            print "Book not added."
            message = "Invalid book_id / book deleted / book not available."
            return Response(message, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            print e
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST) 

    def delete(self, request, format=None):
        """ To return a book. """
        '''
        book_id : unique copy id of the book. Mandatory.
        '''
        response = self.validate("BookAction", "delete", request)
        if not response.get('success'):
            return Response(response.get('message'),response.get('status'))

        book_id = request.query_params.get('book_id')
        try:
            returning_book = BookAction.objects.get(copy__book_id=book_id, is_returned=False)
            returned_date = datetime.now()
            # To do: calculate the fine collected and save in db
            returning_book.is_returned = True
            # Set is_returned True for this entry
            returning_book.save()
            # Update this copy to available
            Book.objects.filter(book_id=book_id).update(available=True)
            message = "Book returned successfully."
            return Response(message, status=status.HTTP_200_OK)
        except Exception as e:
            print e
            return Response(str(e), status=status.HTTP_200_OK)