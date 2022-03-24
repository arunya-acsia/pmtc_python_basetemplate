from custom_decorators import role_required, permission_required
from custom_decorators.status_constants import HttpStatusCode


class UserAlreadyExist(Exception):
    def __init__(self, message="User already exists"):
        self.message = message
        super().__init__(self.message)

