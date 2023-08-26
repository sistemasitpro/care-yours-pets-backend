import {
    IsEmail,
    IsNotEmpty,
    IsNumber,
    IsPhoneNumber,
    IsString,
    IsStrongPassword,
    Matches,
    MaxLength,
    MinLength,
} from 'class-validator';
import { ES_I18N_MESSAGES } from '../../es_i18n_message';
import {ApiProperty} from "@nestjs/swagger";

export class UserDto {
    // VERIFY NAME
    @ApiProperty()
    @IsString({ message: ES_I18N_MESSAGES['nameRequired'] })
    @Matches(/^[a-zA-ZáéíóúÁÉÍÓÚ\s]*$/, { message: ES_I18N_MESSAGES['nameNoSpecialChars'] })
    @MaxLength(180, { message: ES_I18N_MESSAGES['nameMaxLength'] })
    @MinLength(4, { message: ES_I18N_MESSAGES['nameMinLength'] })
    name: string;

    // VERIFY EMAIL
    @ApiProperty()
    @IsEmail({}, { message: ES_I18N_MESSAGES['emailRequired'] })
    @MaxLength(90, { message: ES_I18N_MESSAGES['emailMaxLength'] })
    email: string;

    // VERIFY PHONE
    @ApiProperty()
    @IsPhoneNumber(undefined, { message: ES_I18N_MESSAGES['phoneRequired'] })
    @Matches(/^\(\+\d{2,3}\)\d+$/, { message: ES_I18N_MESSAGES['mobilePhoneValid']})
    @MaxLength(15, { message: ES_I18N_MESSAGES['phoneMaxLength'] })
    phone_number: string;

    // VERIFY ADDRESS
    @ApiProperty()
    @IsNotEmpty({ message: ES_I18N_MESSAGES['addressRequired'] })
    @IsString({ message: ES_I18N_MESSAGES['addressRequired'] })
    @MaxLength(255, { message: ES_I18N_MESSAGES['addressMaxLength'] })
    address: string;

    // VERIFY CITY
    @ApiProperty()
    @IsNumber({}, { message: ES_I18N_MESSAGES['cityRequired'] })
    city_id: number;

    // VERIFY PASSWORD
    @ApiProperty()
    @IsStrongPassword({}, { message: ES_I18N_MESSAGES['passwordStrong'] })
    @MaxLength(20, { message: ES_I18N_MESSAGES['passwordMaxLength'] })
    password: string;
}
