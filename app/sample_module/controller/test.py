from flask_restx import Namespace, Resource, fields
from custom_decorators import role_required, permission_required
from custom_decorators.status_constants import HttpStatusCode
from custom_decorators.response import Response
from app.sample_module.delegates.test import TestDelegate
from flask import request

api = Namespace("Test", description="Namespace for Test API")

user_create_doc = api.model("User",{
    "name": fields.String,
    "password": fields.String
})


@api.route("/test")
class Test(Resource):
    # @api.doc(params={"paylod":{'name':'','password': ''}})
    @api.expect(user_create_doc)
    def post(self):
        try:
            """
                    API for sample API creation
                    :return: success
                    """
            payload = request.json
            data = TestDelegate.create_user(payload)

            return Response.success(response_data=data, status_code=HttpStatusCode.OK,
                                    message="User successfully created")
        # except ValidationError as err:
        #         return Response.error(err.messages, HttpStatusCode.BAD_REQUEST)

        except Exception as err:
            print(err)
            return Response.error(str(err), HttpStatusCode.BAD_REQUEST, message="Error")
