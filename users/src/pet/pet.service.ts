import { Injectable } from '@nestjs/common';
import { InjectRepository } from '@nestjs/typeorm';
import { Repository } from 'typeorm';
import { Pet } from './entities/pet/pet';
import { PetDto } from './dto/pet.dto/pet.dto';
import { User } from '../user/entities/user/user';

@Injectable()
export class PetService {
  constructor(
    @InjectRepository(Pet) private petRepository: Repository<Pet>,
    @InjectRepository(User) private userRepository: Repository<User>,
  ) {}
  async insert(petDto: PetDto) {
    //FIND USER
    const user = await this.userRepository.findOne({
      where: { id: petDto.user_uid },
    });
    //CREATE PET
    const pet = this.petRepository.create({ ...petDto, user: user });

    try {
      await this.petRepository.save(pet);
      return {
        message: 'Mascota creada y asociada correctamente ' + user.name,
      };
    } catch (error) {
      console.log(error);
    }
  }
}
