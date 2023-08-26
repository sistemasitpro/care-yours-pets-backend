import { IsEmail, IsNotEmpty, IsString } from 'class-validator';
import { ES_I18N_MESSAGES } from '../../es_i18n_message';
import {ApiProperty} from "@nestjs/swagger";

export class AuthDto {
  @ApiProperty()
  @IsNotEmpty({ message: ES_I18N_MESSAGES['emailRequired'] })
  @IsEmail({}, { message: ES_I18N_MESSAGES['emailFormat'] })
  email: string;

  @ApiProperty()
  @IsNotEmpty({ message: ES_I18N_MESSAGES['passwordRequired'] })
  @IsString()
  password: string;
}
