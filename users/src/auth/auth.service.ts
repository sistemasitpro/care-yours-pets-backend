import {BadRequestException, Inject, Injectable} from '@nestjs/common';
import { UserService } from '../user/user.service';
import { JwtService } from '@nestjs/jwt';
import * as bcrypt from 'bcrypt';
import {ConfigService, ConfigType} from '@nestjs/config';
import { AuthDto } from './dto/auth.dto/auth.dto';
import config from "../config";

@Injectable()
export class AuthService {
  constructor(
    private usersService: UserService,
    private jwtService: JwtService,
    @Inject(config.KEY) private configService: ConfigType<typeof config>
  ) {}

  async signIn(data: AuthDto) {
    const user = await this.usersService.findOneByEmail(data.email);
    if (!user) throw new BadRequestException('El usuario no existe');

    //MATCH PASSWORD
    const isMatch = await bcrypt.compare(data.password, user?.password);
    if (!isMatch) {
      throw new BadRequestException('Contraseña incorrecta');
    }

    const tokens = await this.getTokens(user.id, user.email);
    await this.updateRefreshToken(user.id, tokens.refreshToken);

    return {
      ...tokens,
      name: user.name,
      uuid: user.id,
    };
  }
  hashData(data: string) {
    return bcrypt.hash(data, 10);
  }
  async updateRefreshToken(userUid: string, refreshToken: string) {
    const hashedRefreshToken = await this.hashData(refreshToken);
    await this.usersService.update(userUid, {
      refreshToken: hashedRefreshToken,
    });
  }

  async invalidateRefreshToken(userId: string): Promise<void> {
    await this.usersService.update(userId, { refreshToken: null });
  }

  async getTokens(userId: string, email: string) {
    const [accessToken, refreshToken] = await Promise.all([
      this.jwtService.signAsync(
        {
          sub: userId,
          email,
        },
        {
          secret: this.configService.JWT_ACCESS_SECRET,
          expiresIn: this.configService.JWT_ACCESS_SECRET_EXPIRY,
        },
      ),
      this.jwtService.signAsync(
        {
          sub: userId,
          email,
        },
        {
          secret: this.configService.JWT_REFRESH_SECRET,
          expiresIn: this.configService.JWT_REFRESH_SECRET_EXPIRY,
        },
      ),
    ]);

    return {
      accessToken,
      refreshToken,
    };
  }
}
