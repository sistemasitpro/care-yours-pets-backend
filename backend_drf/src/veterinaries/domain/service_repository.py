# model
from veterinaries.models import (
    VeterinaryService, Veterinaries, Service
)


class Repository:
    
    def __init__(self) -> None:
        self.model_vet_service=VeterinaryService
        self.model_service = Service
    
    def create_service(self, data:dict, veterinary:Veterinaries, service:Service) -> VeterinaryService:
        return self.model_vet_service.objects.create(
            veterinary_id=veterinary,
            service_id=service,
            name=data['name'],
            price=data['price'],
        )
    
    def get_veterinary_services(self, id:str) -> VeterinaryService:
        return self.model_vet_service.objects.filter(veterinary_id=id).all()
    
    def get_service_by_id(self, id:int) -> Service:
        return self.model_service.objects.filter(id=id).first()

vsr = Repository()