import {
  Body,
  Controller,
  HttpCode,
  HttpStatus,
  Post,
  Req,
  UseGuards,
} from '@nestjs/common';
import { AuthService } from './auth.service';
import { AuthDto } from './dto/auth.dto/auth.dto';
import {AuthGuard} from "@nestjs/passport";
import {ApiBody, ApiHeader, ApiOkResponse, ApiOperation, ApiProperty, ApiResponse, ApiTags} from "@nestjs/swagger";

class LogoutResponseDTO {
  @ApiProperty(
      { example: 'El usuario se desconectó con éxito' })
  message: string;
}

export class SignInResponseDTO {
  @ApiProperty({ example: 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...' })
  accessToken: string;

  @ApiProperty({ example: 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...' })
  refreshToken: string;

  @ApiProperty({ example: 'Juanito' })
  name: string;

  @ApiProperty({ example: '2c4275e9-40cf-47c8-81b9-12476213d410' })
  uuid: string;
}

@Controller('auth')
@ApiTags('auth')
export class AuthController {
  constructor(private readonly authService: AuthService) {}
  @UseGuards(AuthGuard('jwt'))
  @Post('/logout')
  @HttpCode(HttpStatus.OK)
  @ApiResponse({ status: 200, type: LogoutResponseDTO })
  @ApiResponse({ status: 401, description: 'Unauthorized' })
  @ApiOperation({ summary: 'Sign off' })
  @ApiHeader({
    name: 'Authorization',
    description: 'Authorization token in bearer format',
    required: true,
  })
  async logout(@Req() req) {
    const userId = req.user.sub;
    await this.authService.invalidateRefreshToken(userId);
    return { message: 'El usuario se desconectó con éxito' };
  }

  @Post('signin')
  @HttpCode(HttpStatus.OK)
  @ApiOperation({ summary: 'Signin' })
  @ApiBody({ type: AuthDto })
  @ApiResponse({ status: 200, type: SignInResponseDTO })
  @ApiResponse({ status: 400, description: 'Request Failed' })
  signIn(@Body() dto: AuthDto) {
    return this.authService.signIn(dto);
  }
}
