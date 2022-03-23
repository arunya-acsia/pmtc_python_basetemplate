def register_module_routes(api, app, root="api"):
    from .test import api as test_api
    api.add_namespace(test_api, path=f"/v1")