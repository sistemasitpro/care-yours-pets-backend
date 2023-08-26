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
import {ApiProperty} from "@nestjs/swagger";
export class PetDto {
  @ApiProperty()
  @IsString({ message: ES_I18N_MESSAGES['required'] })
  @MaxLength(100, { message: ES_I18N_MESSAGES['maxCharacters'] })
  @Matches(/^[a-zA-ZáéíóúÁÉÍÓÚ\s]*$/, {
    message: ES_I18N_MESSAGES['noSpecialChars'],
  })
  @ApiProperty()
  @MinLength(4, { message: ES_I18N_MESSAGES['nameMin'] })
  name: string;
  @ApiProperty()
  @IsInt({ message: ES_I18N_MESSAGES['ageInteger'] })
  @Min(0, { message: ES_I18N_MESSAGES['ageMin'] })
  @Max(99, { message: ES_I18N_MESSAGES['ageMax'] })
  age: number;
  @ApiProperty()
  @IsString({ message: ES_I18N_MESSAGES['required'] })
  @Matches(/^[a-zA-ZáéíóúÁÉÍÓÚ\s]*$/, {
    message: ES_I18N_MESSAGES['noSpecialChars'],
  })
  @ApiProperty()
  @MaxLength(100, { message: ES_I18N_MESSAGES['maxCharacters'] })
  type_pet: string;
  @IsString({ message: ES_I18N_MESSAGES['required'] })
  @Matches(/^[a-zA-ZáéíóúÁÉÍÓÚ\s]*$/, {
    message: ES_I18N_MESSAGES['noSpecialChars'],
  })
  @ApiProperty()
  @MaxLength(100, { message: ES_I18N_MESSAGES['maxCharacters'] })
  specie: string;
  @ApiProperty()
  @IsOptional()
  @IsString({ message: ES_I18N_MESSAGES['required'] })
  @MaxLength(200, { message: ES_I18N_MESSAGES['maxCharactersPreexistingCor'] })
  @Matches(/^[a-zA-ZáéíóúÁÉÍÓÚ\s]*$/, {
    message: ES_I18N_MESSAGES['noSpecialChars'],
  })
  preexisting_cor: string;
  @ApiProperty()
  @IsUUID(4, { message: ES_I18N_MESSAGES['formatUuid'] })
  user_uid: string;
}
