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
@Controller('auth')
export class AuthController {
  constructor(private readonly authService: AuthService) {}
  @UseGuards(AuthGuard('jwt'))
  @Post('/logout')
  @HttpCode(HttpStatus.OK)
  async logout(@Req() req) {
    const userId = req.user.sub;
    await this.authService.invalidateRefreshToken(userId);
    return { message: 'El usuario se desconectó con éxito' };
  }
  @Post('signin')
  @HttpCode(HttpStatus.OK)
  signIn(@Body() dto: AuthDto) {
    return this.authService.signIn(dto);
  }
}
