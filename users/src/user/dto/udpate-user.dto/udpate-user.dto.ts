import { PartialType } from '@nestjs/mapped-types';
import { UserDto } from '../user.dto/user.dto';

export class UpdateUserDto extends PartialType(UserDto) {
  refreshToken: string;
}
