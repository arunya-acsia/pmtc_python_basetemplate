def register_routes(api, app, root="api"):
    from app.sample_module.controller import register_module_routes as attach_test
    attach_test(api, app)