from rest_framework.exceptions import APIException

class InvalidRequest(APIException):
    status_code = 400
    default_detail = 'Invalid request'

class DatabaseError(APIException):
    status_code = 500
    default_detail = 'Database error'
