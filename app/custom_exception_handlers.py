from custom_decorators import role_required, permission_required
from custom_decorators.status_constants import HttpStatusCode
from custom_decorators.response import Response
from exceptions import PermissionDenied
from custom_exceptions import UserAlreadyExist


def register_error_handlers(api):

    @api.errorhandler(PermissionDenied)
    def handle_permission_denied_exception(error):
        return Response.error(
            {"exception": str(error)},
            HttpStatusCode.FORBIDDEN,
            business_error=None,
            message=str(error)
        )

    @api.errorhandler(UserAlreadyExist)
    def handle_user_already_exist_exception(error):
        return Response.error(
            {"exception": str(error)},
            HttpStatusCode.BAD_REQUEST,
            message=str(error)
        )
