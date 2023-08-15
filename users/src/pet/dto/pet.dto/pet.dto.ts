import {
  IsInt,
  IsNotEmpty,
  IsOptional,
  IsString,
  IsUUID,
  Matches,
  Max,
  MaxLength,
  Min,
  MinLength,
} from 'class-validator';
import { ES_I18N_MESSAGES } from '../../es_i18n_message';
export class PetDto {
  @IsString({ message: ES_I18N_MESSAGES['required'] })
  @MaxLength(100, { message: ES_I18N_MESSAGES['maxCharacters'] })
  @Matches(/^[a-zA-ZáéíóúÁÉÍÓÚ\s]*$/, {
    message: ES_I18N_MESSAGES['noSpecialChars'],
  })
  @MinLength(4, { message: ES_I18N_MESSAGES['nameMin'] })
  name: string;
  @IsInt({ message: ES_I18N_MESSAGES['ageInteger'] })
  @Min(0, { message: ES_I18N_MESSAGES['ageMin'] })
  @Max(99, { message: ES_I18N_MESSAGES['ageMax'] })
  age: number;
  @IsString({ message: ES_I18N_MESSAGES['required'] })
  @Matches(/^[a-zA-ZáéíóúÁÉÍÓÚ\s]*$/, {
    message: ES_I18N_MESSAGES['noSpecialChars'],
  })
  @MaxLength(100, { message: ES_I18N_MESSAGES['maxCharacters'] })
  type_pet: string;
  @IsString({ message: ES_I18N_MESSAGES['required'] })
  @Matches(/^[a-zA-ZáéíóúÁÉÍÓÚ\s]*$/, {
    message: ES_I18N_MESSAGES['noSpecialChars'],
  })
  @MaxLength(100, { message: ES_I18N_MESSAGES['maxCharacters'] })
  specie: string;
  @IsOptional()
  @IsString({ message: ES_I18N_MESSAGES['required'] })
  @MaxLength(200, { message: ES_I18N_MESSAGES['maxCharactersPreexistingCor'] })
  @Matches(/^[a-zA-ZáéíóúÁÉÍÓÚ\s]*$/, {
    message: ES_I18N_MESSAGES['noSpecialChars'],
  })
  preexisting_cor: string;
  @IsUUID(4, { message: ES_I18N_MESSAGES['formatUuid'] })
  user_uid: string;
}
