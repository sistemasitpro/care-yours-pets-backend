# models
from models_nestjs.models import Users


class Repository:
    
    def __init__(self) -> None:
        self.model = Users
    
    def get_by_id(self, id:str) -> Users | None:
        return self.model.objects.filter(id=id).only('id', 'name', 'email', 'is_active').first()

usr = Repository()