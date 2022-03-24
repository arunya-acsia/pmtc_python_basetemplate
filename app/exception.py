from werkzeug.exceptions import HTTPException
from custom_decorators.response import Response
from custom_decorators.status_constants import HttpStatusCode


def register_error_handlers(api):
    @api.errorhandler(Exception)
    def handle_error(error):
        code = 500
        if isinstance(error, HTTPException):
            code = error.code
        return Response.error(
            {"exception": str(error)},
            code,
            message=str(error))

    @api.errorhandler(Exception)
    def handle_error_exception(error):
        return Response.error(
            {"exception": str(error)},
            HttpStatusCode.BAD_REQUEST,
            message=str(error))
