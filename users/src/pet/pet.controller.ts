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
import {ApiBadRequestResponse, ApiBody, ApiOperation, ApiProperty, ApiResponse, ApiTags} from '@nestjs/swagger';
class PetResponseDTO {
  @ApiProperty(
      { example: 'Mascota creada y asociada correctamente ygghh' })
  message: string;
}

@ApiTags('Pets')
@Controller('pet')
export class PetController {
  constructor(private readonly petService: PetService) {}
  @Post()
  @UseGuards(AuthGuard('jwt'))
  @ApiOperation({ summary: 'Create a pet' })
  @ApiBody({ type: PetDto, description: 'This method allows customers to add a new pet to the PetStore. After receiving a successful request.' })
  @ApiResponse({ status: HttpStatus.OK, description: 'Pet created successfully', type: PetResponseDTO })
  @ApiBadRequestResponse({ description: 'Invalid data provided' })
  @HttpCode(HttpStatus.OK)
  create(@Body() petDto: PetDto) {
    return this.petService.insert(petDto);
  }

}
