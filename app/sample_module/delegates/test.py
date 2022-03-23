from app.sample_module.services.test import TestService


class TestDelegate:
    @staticmethod
    def create_user(data):
        # calling user creating service function from service package
        user = TestService.create_user(data)
        return user