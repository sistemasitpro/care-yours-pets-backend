import {Body, Controller, HttpCode, HttpStatus, Post} from '@nestjs/common';
import {UserService} from "./user.service";
import {UserDto} from "./dto/user.dto/user.dto";
import {
    ApiBody, ApiOperation,
    ApiProperty,
    ApiResponse,
    ApiTags
} from "@nestjs/swagger";

class UserResponseDTO {
    @ApiProperty(
        { example: 'Usuario creado correctamente' })
    message: string;
}

@ApiTags('users')
@Controller('user')
export class UserController {
    constructor(private readonly userService: UserService) {}
    @Post()
    @HttpCode(HttpStatus.OK)
    @ApiOperation({ summary: 'Endpoint to create a new user' })
    @ApiBody({
        type: UserDto,
        description: 'Data user',
    })
    @ApiResponse({
        status: 200,
        description: 'Successful create user',
        type: UserResponseDTO,
    })
    @ApiResponse({
        status: 409,
        description: 'Conflict email or telefone number',
    })
    create(@Body() userDto: UserDto) {
        return this.userService.insert(userDto);
    }
}
