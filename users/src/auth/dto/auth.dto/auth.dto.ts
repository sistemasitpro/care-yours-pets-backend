import { IsEmail, IsNotEmpty, IsString } from 'class-validator';
import { ES_I18N_MESSAGES } from '../../es_i18n_message';

export class AuthDto {
  @IsNotEmpty({ message: ES_I18N_MESSAGES['emailRequired'] })
  @IsEmail({}, { message: ES_I18N_MESSAGES['emailFormat'] })
  email: string;

  @IsNotEmpty({ message: ES_I18N_MESSAGES['passwordRequired'] })
  @IsString()
  password: string;
}
