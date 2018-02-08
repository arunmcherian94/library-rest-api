# Library Management REST api's #

Provides REST api's for managing a library.
The features supported are:

* Member operations
    * Add a member
    * Fetch a particular member details or fetch all members
    * Update member details
    * Remove a member (soft delete only)
* Book operations
    * Add a new book
    * Fetch a particular book details or fetch all books
    * Update book details
    * Remove a book (soft delete)

### Tools Employed ####

REST api Framework is built with these tools:

* Python 2.7.6 and Django 1.11.10
* MySQL - Server version: Ver 14.14 Distrib 5.6.37
* Django rest framework - 3.7.7

### How do I get set up? ###

* Database configuration
    * `create database librarydb
    * configure database settings in <repo>/core_apis/settings.py
    * `mysql -u <user> -p < <repo>/core_apis/librarydb_dump.sql

* Summary of set up
    * Assuming you have installed all the above mentioned tools, required for this application, please go ahead and check out this repository.
    * `create a virtualenv and activate
    * `pip install -r requirements.txt`
    * `cd <repo>/core_apis
    * `python manage.py makemigrations
    * `python manage.py migrate
    * `python manage.py runserver

* Dependencies

* Usage instructions
    * visit http://localhost:8000/ in your browser
    * Has three options, BookBorrowReturn, BookCRUD, MemberCRUD
    * MemberCRUD usage:
        * GET -> to get member details
            * http://localhost:8000/core/member/?email=arun.cherian@gmail.com : returns particular member details
            * http://localhost:8000/core/member/ : will return all members
        * POST -> to create new member
            * first_name, phone, email (unique), expires_on (YYYY-MM-DD) are mandatory params
        * PUT -> to update member details
            * email is mandatory in query string
            * field_name to be updated should be given
        * DELETE -> to remove a member. (updates is_deleted=True)
            * email is mandatory in query string
           
    * BookCRUD usage:
        * GET -> to get book details
            * http://localhost:8000/core/book/?isbn=12345 : returns particular book details
            * http://localhost:8000/core/book/ : will return all books
        * POST -> to create new book
            * title, isbn(unique), author_email (an author with this email should be existing) are mandatory params.
                * Note: Author create is not handled.
        * PUT -> to update book details
            * field_names to be updated should be given
        * DELETE -> to remove a book. (updates is_deleted=True)
            * isbn is mandatory in query string
            
    * BookBorrowReturn usage:
        * POST -> to borrow a book
            * book_id (the unique copy id) and email (registered member email) are mandatory params.
        * DELETE -> to return a book
            * book_id (unique copy id) should be present in query string

### ToDos ###

* Logging. Left this out for simplicity
* Validation of data using django rest serializers
* Table to store plan details for each member
* AuthorCRUD functionalities

