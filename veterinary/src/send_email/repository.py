# models
from send_email.models import TokenDjango


class Repository:
    
    def __init__(self) -> None:
        self.models = TokenDjango

    def create(self, data:dict) -> TokenDjango:
       return self.models.objects.create(
            token=data['token'],
            at_created=data['at_created']
        )
    
    def get_datetime_created(self, token:str):
        instance = self.models.objects.filter(token=token).first()
        return instance.at_created

tkdr = Repository()