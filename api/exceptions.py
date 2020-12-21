from fastapi import HTTPException, status


class APIException(HTTPException):
    """Light wrapper around HTTPException that allows specifying defaults via class property"""

    status_code = status.HTTP_400_BAD_REQUEST
    detail = None
    headers = None

    def __init__(self, *args, **kwargs):
        if "status_code" not in kwargs:
            kwargs["status_code"] = self.status_code
        if "detail" not in kwargs:
            kwargs["detail"] = self.detail
        if "headers" not in kwargs:
            kwargs["headers"] = self.headers
        super().__init__(*args, **kwargs)


class CredentialsException(APIException):
    """Default exception to throw when user is not authorized"""

    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Invalid credentials. Please log in again."
    headers = {"WWW-Authenticate": "Bearer"}


class BannedUserException(APIException):
    """Default exception when a banned user tries to access something"""

    status_code = status.HTTP_403_FORBIDDEN
    detail = (
        "Your account has been banned. Please contact an admin if you wish to appeal."
    )


class NoUserAccessException(APIException):
    """Default exception when a user tries to access something they do not have permission for"""

    status_code = status.HTTP_403_FORBIDDEN
    detail = "You do not have access to this resource."


class NotFoundException(APIException):
    """Standard "item not found" exception."""

    status_code = status.HTTP_404_NOT_FOUND
    detail = "Item not found."
