# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

#Django rest framework imports
# from rest_framework import generics
from rest_framework.response import Response
# from rest_framework.reverse import reverse
from rest_framework.views import APIView
from rest_framework import status
from core_apis import settings

#Model imports
from models import Member, Book_master, Author, Book

# Import serializers here
from serializers import MemberSerializer, BookSerializer

#Import custom validations here.
from validations import DataValidation
validation = DataValidation()

import json
from django.http import JsonResponse

model_list = {"Member":Member, "Book_master":Book_master}
serializer_list = {"Member":MemberSerializer,"Book_master":BookSerializer}
# Making use of class based views here

class GenericHandler(object):
    """ """
    def validate(self, model_name, method, request):
        # val_fn_tobe_called = eval(model_name.lower()+"_validate")
        if model_name == "Member":
            self.response = validation.member_validate(method,request)
        elif model_name == "Book_master":
            self.response = validation.book_master_validate(method,request)
        return self.response

    def read(self, model_name, request, query_param):
        print 'in read'
        kwargs = {}
        query_param_value = request.query_params.get(query_param)
        kwargs[query_param] = query_param_value
        try:
          model_data = model_list[model_name].objects.filter( **kwargs)
          print 'model_data'
          print model_data
          if not model_data:
              message = {"message":"No "+model_name+" found for: "+query_param_value, "status":status.HTTP_200_OK}
              return message

          serializer = serializer_list[model_name](model_data, many=True)
          message = {"message":serializer.data, "status":status.HTTP_200_OK}
          return message
          
        except Exception as e:
            print 'error'
            print e
            message = {"message":str(e), "status":status.HTTP_400_BAD_REQUEST}
            return message

    def update(self, model_name, request, query_param):
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
        kwargs = {}
        data=request.data
        query_param_value = request.query_params.get(query_param)
        kwargs[query_param] = query_param_value
        try:
            model_deleted = model_list[model_name].objects.filter( **kwargs).update(is_deleted=True)
            print model_deleted
            if not model_deleted:
                message = {"message":"No "+model_name+" found with this "+query_param+". Did not delete.", "status":status.HTTP_200_OK}
                return message
            message = {"message":model_name+" entry deleted successfully.","status":status.HTTP_200_OK}
            return message
        except Exception as e:
            print 'error2'
            print e
            message = {"message":str(e), "status":status.HTTP_400_BAD_REQUEST}
            return message

class MemberOperations(APIView, GenericHandler):
    """
    Class which handles Member actions.
    Inherited from APIView class.
    """

    # Over-ride the allowed http method names
    http_method_names = [u'get', u'post', u'put', u'delete']

    def get(self, request, format=None):
        """ To fetch member details. """
        is_valid = self.validate("Member", "get", request)
        if not is_valid.get('success'):
            return Response(is_valid.get('message'),is_valid.get('status'))
        print 'goin to call read'
        response = self.read("Member",request,"email")
        return Response(response.get('message'),response.get('status'))    

    def post(self, request, format=None):
        """ """
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

        new_member = Member(first_name=first_name, last_name=last_name,email=email,phone=phone,member_type=member_type,expires_on=expires_on)
        try:
            new_member.save()
            message = "New member added successfully."
            return Response(message, status=status.HTTP_201_CREATED)
        except Exception as e:
            print e
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, format=None):
        """ """
        is_valid = self.validate("Member", "delete", request)
        if not is_valid.get('success'):
            return Response(is_valid.get('message'),is_valid.get('status'))
        response = self.remove("Member",request,"email")
        return Response(response.get('message'),response.get('status'))

    def put(self, request, format=None):
        """ """
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
        is_valid = self.validate("Book_master", "get", request)
        if not is_valid.get('success'):
            return Response(is_valid.get('message'),is_valid.get('status'))
        print 'after'
        response = self.read("Book_master",request,"isbn")
        return Response(response.get('message'),response.get('status'))

    def delete(self, request, format=None):
        """ """
        is_valid = self.validate("Book_master", "delete", request)
        if not is_valid.get('success'):
            return Response(is_valid.get('message'),is_valid.get('status'))
        response = self.remove("Book_master",request,"isbn")
        return Response(response.get('message'),response.get('status'))

    def put(self, request, format=None):
        """ """
        is_valid = self.validate("Book_master", "put", request)
        if not is_valid.get('success'):
            return Response(is_valid.get('message'),is_valid.get('status'))
        response = self.update("Book_master",request,"isbn")
        return Response(response.get('message'),response.get('status'))

    def post(self, request, format = None):
        """ """
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
            print author
            new_book_master = Book_master(author=author,isbn=isbn, title=title, no_of_copies=no_of_copies)
            new_book_master.save()
            # create book copies and save them in Book table
            for i in xrange(no_of_copies):
                Book.objects.create(book_master=new_book_master)
            message = "New book added successfully."
            return Response(message, status=status.HTTP_201_CREATED)
        except Exception as e:
            print e
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)



class BookActions(APIView, GenericHandler):
    pass