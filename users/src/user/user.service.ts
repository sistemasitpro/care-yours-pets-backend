import {ConflictException, Injectable, InternalServerErrorException} from '@nestjs/common';
import {UserDto} from "./dto/user.dto/user.dto";
import {InjectRepository} from "@nestjs/typeorm";
import {User} from "./entities/user/user";
import {City} from "../city/entities/city/city";
import {Repository} from "typeorm";
import * as bcrypt from 'bcrypt';
import {ES_I18N_MESSAGES} from "./es_i18n_message";
import {UpdateUserDto} from "./dto/udpate-user.dto/udpate-user.dto";
import {ExternalApiService} from "../external-api/external-api.service";

@Injectable()
export class UserService {
    constructor(
        private externalApiService: ExternalApiService,
        @InjectRepository(User) private usersRepository: Repository<User>,
        @InjectRepository(City) private cityRepository: Repository<City>
    ) {}
    async update(userUid: string, updateUserDto: UpdateUserDto): Promise<User> {
        try {
            const user = await this.usersRepository.findOne({
                where: { id: userUid },
            });
            const updatedUser = { ...user, ...updateUserDto };
            const savedUser = await this.usersRepository.save(updatedUser);
            return savedUser;
        } catch (error) {
            return error;
        }
    }
    async findOneByEmail(email: string): Promise<User> {
        return this.usersRepository.findOne({
            relations: ['city'],
            where: {
                email: email,
            },
        });
    }
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
            //this.externalApiService.activateUser({},{})
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
