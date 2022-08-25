import json
from datetime import datetime
import sys
from logging import Logger
from http import HTTPStatus


class Account:
    """ Account details"""
    def __init__(self, account_id, account_type):
        self.account_id = account_id
        self.account_type = account_type


class APIExceptionFinal(Exception):
    """Base APi Exception."""
    http_status = HTTPStatus.INTERNAL_SERVER_ERROR
    internal_err_msg = 'API exception occurred'
    user_err_msg = "We are sorry! Unexpected error occurred on our end "

    def __init__(self, *args, user_err_msg=None):
        if args:
            self.internal_err_msg = args[0]
            super().__init__(*args)
        else:
            super().__init__(self.internal_err_msg)

        if user_err_msg is not None:
            self.user_err_msg = user_err_msg

    def to_json(self):
        err_object = {'status': self.http_status, 'message': self.user_err_msg}
        return json.dumps(err_object)

    def log_exception(self):
        exception = {
            "type": type(self).__name__,
            "http_status": self.http_status,
            "message": self.args[0] if self.args else self.internal_err_msg,
            "args": self.args[1:]
        }
        print(f"Exception: {datetime.utcnow().isoformat}: {exception}")

"""
try:
    raise APIExceptionFinal()
except APIExceptionFinal as ex:
    ex.log_exception()
    print(ex.to_json())
"""


# Default Messages:
class ApplicationExceptionFinal(APIExceptionFinal):
    """ Indicates an application error (not user caused) - 5xx HTTP type Error """
    https_status = HTTPStatus.INTERNAL_SERVER_ERROR
    internal_err_msg = 'Generic server side exception'
    user_err_msg = 'We are sorry, An unexcepted error occurred on our end'


class DBExceptionFinal(ApplicationExceptionFinal):
    """ General database Exception """
    https_status = HTTPStatus.INTERNAL_SERVER_ERROR
    internal_err_msg = 'Database Exception '
    user_err_msg = 'We are sorry, An unexcepted error occurred on our end'


class DBConnectionErrorFinal(DBExceptionFinal):
    """ Indicates an error connecting to database """
    https_status = HTTPStatus.INTERNAL_SERVER_ERROR
    internal_err_msg = 'Database Connection Exception '
    user_err_msg = 'We are sorry, An unexcepted error occurred on our end'


class ClientExceptionFinal(APIExceptionFinal):
    """ Indicates exception that was caused by user, not an internal error """
    https_status = HTTPStatus.BAD_REQUEST
    internal_err_msg = 'Client submitted bad request '
    user_err_msg = 'A bad request was received'


class NotFoundErrorFinal(ClientExceptionFinal):
    """ Indicates resource was not Found """
    https_status = HTTPStatus.NOT_FOUND
    internal_err_msg = 'Resource Not Found '
    user_err_msg = 'Requested resource was not found '


class NotAuthorizedErrorFinal(ClientExceptionFinal):
    """ User is not authorized to perform request action on resource """
    https_status = HTTPStatus.UNAUTHORIZED
    internal_err_msg = 'Client not authorized to perform operation '
    user_err_msg = 'You are not authorized to perform this request '


def lookup_account_by_id_final(account_id):
    """ check the account """
    if not isinstance(account_id, int) or account_id <= 0:
        raise ClientExceptionFinal(f"Account number {account_id} is invalid ",
                              f"account_id={account_id}, ",
                              f"type error - account number not an integer")

    if account_id < 100:
        raise DBConnectionErrorFinal(f"Permanent failure connecting to Database, "
                                f"db=db01")
    elif account_id < 200:
        raise NotAuthorizedErrorFinal(f"User does not have permission to read this account"
                                 f"account_id = {account_id}")
    elif account_id < 300:
        raise NotFoundErrorFinal(f"Account not found",
                            f" account_id = {account_id}")
    else:
        return Account(account_id, 'Savings')


def get_account(account_id):
    try:
        account = lookup_account_by_id_final(account_id)
    except APIExceptionFinal as ex:
        ex.log_exception()
        return ex.to_json()
    else:
        return HTTPStatus.OK, {'id': account.account_id, "type": account.account_type}


get_account('50')
get_account('abc')
get_account('150')
get_account('250')

get_account('350')
