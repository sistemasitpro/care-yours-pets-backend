import {
  Body,
  Controller,
  HttpCode,
  HttpStatus,
  Post,
  UseGuards,
} from '@nestjs/common';
import { PetService } from './pet.service';
import { PetDto } from './dto/pet.dto/pet.dto';
import { AuthGuard } from '@nestjs/passport';

@Controller('pet')
export class PetController {
  constructor(private readonly petService: PetService) {}
  @Post()
  @UseGuards(AuthGuard('jwt'))
  @HttpCode(HttpStatus.OK)
  create(@Body() petDto: PetDto) {
    return this.petService.insert(petDto);
  }
}
