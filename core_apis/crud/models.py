# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.validators import RegexValidator
from django.db import models
from core_apis import settings
import uuid
# Create your models here.

class Member(models.Model):
    """
    Member table to store member parameters.
    """

    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")

    first_name = models.CharField(max_length=40, default=None, null=True, blank=True, verbose_name="Member's first name.")
    last_name = models.CharField(max_length=40, default=None, null=True, blank=True, verbose_name="Member's last name.")
    email = models.EmailField(unique=True, verbose_name="Member's email id.")
    password = models.CharField(max_length=32, default=None, null=True, blank=True, verbose_name="To store the encrypted password.")
    phone = models.CharField(max_length=32, verbose_name="Telephone number", validators=[phone_regex])
    is_active = models.BooleanField(default=True, verbose_name="Member active status")
    is_deleted = models.BooleanField(default=False, verbose_name="Member deletion status")
    joined_on = models.DateTimeField(auto_now_add=True, verbose_name="Member joining date")
    modified_on = models.DateTimeField(auto_now=True,verbose_name="Member details modified date")
    member_type = models.CharField(max_length=1, default='A', verbose_name="Member type. Admin/User")
    expires_on = models.DateField(verbose_name="Membership expiry date.")
    misc_details = models.CharField(max_length=1024, default=None, null=True, blank=True, verbose_name="Membership miscellaneous details.")

    def __str__(self):
        """ String representation of the Model."""
        return '{"Member Name": "%s", "Email": "%s", "Expired on: "%s"}' % (self.first_name, self.email, self.expires_on)


class Author(models.Model):
    """ Table to store author details. """
    first_name = models.CharField(max_length=40, default=None, null=True, blank=True, verbose_name="Author's first name.")
    last_name = models.CharField(max_length=40, default=None, null=True, blank=True, verbose_name="Author's last name.")
    email = models.EmailField(unique=True, verbose_name="Author's email id.")

    def __str__(self):
        """ String representation of the Model."""
        return '{"Author Name": "%s %s"}' % (self.first_name, self.last_name)

class BookManager(models.Manager):
    """ To fetch count of books by title. """
    def title_count(self, keyword):
        return self.filter(title__icontains=keyword).count()

class Book_master(models.Model):
    """ Stores book details. """
    author = models.ForeignKey('Author', on_delete=models.PROTECT, verbose_name="Unique id of the book author.")
    isbn = models.CharField(max_length=13, unique=True, verbose_name="ISBN of the book.")
    title = models.CharField(max_length=100, default=None, null=True, blank=True, verbose_name="Title of the book.")
    no_of_copies = models.IntegerField(default=1, verbose_name="Total number of copies available.")
    is_deleted = models.BooleanField(default=False, verbose_name="Book deletion status")
    added_on = models.DateTimeField(auto_now_add=True, verbose_name="Book addition date")
    modified_on = models.DateTimeField(auto_now=True,verbose_name="Book details modified date")
    misc_details = models.CharField(max_length=1024, default=None, null=True, blank=True, verbose_name="Extra details of book.")
    objects = BookManager()

    def __str__(self):
        """ String representation of the Model."""
        return '{"Book Name": "%s", "ISBN": "%s"}' % (self.title,self.isbn)


class Book(models.Model):
    """ Stores particular book's copy details. """
    book_master = models.ForeignKey('Book_master', on_delete=models.CASCADE, verbose_name="Id of the parent book.")
    last_borrowed_date = models.DateTimeField(auto_now_add=True, verbose_name="Most reccent borrow date for this copy.")
    book_id = models.UUIDField(default=uuid.uuid4, editable=False)
    available = models.BooleanField(default=True, verbose_name="Book availability.") 

    def __str__(self):
        """ String representation of the Model."""
        return '{"Book master id": "%s"}' % (self.book_master_id)

class BookAction(models.Model):
    """ Table that stores borrow/return data. """
    member = models.ManyToManyField(Member, verbose_name="Member id of the user.")
    copy = models.ForeignKey('Book', on_delete=models.PROTECT, verbose_name="Id of the book copy issued.")
    borrowed_date = models.DateTimeField(default = None, null=True, blank=True, verbose_name="Borrowed date.")
    due_date = models.DateTimeField(verbose_name="Borrowed date.")
    is_returned = models.BooleanField(default=False, verbose_name="Book return status.")
    fine_collected = models.DecimalField(default=0.00, max_digits=6, decimal_places=2, verbose_name="Fine collected.")

    def __str__(self):
        """ String representation of the Model."""
        return '{"Book action. Member": "%s", "Copy: " "%s"}' % (self.member,self.copy)