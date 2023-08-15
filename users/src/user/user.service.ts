import {ConflictException, Injectable, InternalServerErrorException} from '@nestjs/common';
import {UserDto} from "./dto/user.dto/user.dto";
import {InjectRepository} from "@nestjs/typeorm";
import {User} from "./entities/user/user";
import {City} from "../city/entities/city/city";
import {Repository} from "typeorm";
import * as bcrypt from 'bcrypt';
import {ES_I18N_MESSAGES} from "./es_i18n_message";

@Injectable()
export class UserService {
    constructor(
        @InjectRepository(User) private usersRepository: Repository<User>,
        @InjectRepository(City) private cityRepository: Repository<City>,
    ) {}
    async insert(body: UserDto): Promise<any> {
        //GENERATE PASSWORD
        body.password = await bcrypt.hash(body.password, 10);

        //FIND CITY
        const city_user = await this.cityRepository.findOne({
            where: {id: body.city_id},
        });

        //CREATE USER WITH CITY
        const user = this.usersRepository.create({...body, city: city_user});

        //VERIFY EMAIL AND PHONE EXIST
        try {
            await this.usersRepository.save(user);
            return {
                message:
                    'Usuario creado correctamente, y se envió un enlace de activación a su correo: ' +
                    user.email,
            };
        } catch (error) {
            if (error.code === '23505') {
                switch (error.constraint) {
                    case 'UQ_97672ac88f789774dd47f7c8be3':
                        throw new ConflictException({
                            email: ES_I18N_MESSAGES['existEmail'],
                        });
                        break;
                    case 'UQ_17d1817f241f10a3dbafb169fd2':
                        throw new ConflictException({
                            phone: ES_I18N_MESSAGES['existPhone'],
                        });
                        break;
                }
            }
            throw new InternalServerErrorException();
        }
    }
}
