# models
from send_email.models import TokenDjango


class Repository:
    
    def __init__(self) -> None:
        self.model = TokenDjango

    def create(self, token:str) -> TokenDjango:
       return self.model.objects.create(
            token=token,
        )
    
    def get_datetime_created(self, token:str):
        instance = self.model.objects.filter(token=token).first()
        return instance.at_created

tkdr = Repository()