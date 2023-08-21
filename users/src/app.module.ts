import {Module} from '@nestjs/common';
import {TypeOrmModule} from '@nestjs/typeorm';
import {ConfigModule,ConfigService} from "@nestjs/config";
import {User} from "./user/entities/user/user";
import {Pet} from "./pet/entities/pet/pet";
import {Province} from "./province/entities/province/province";
import {City} from "./city/entities/city/city";
import {JwtBlacklistNestjs} from "./jwt-blacklist-nestjs/entities/jwt-blacklist-nestjs/jwt-blacklist-nestjs";
import {UserModule} from './user/user.module';
import {AuthModule} from "./auth/auth.module";
import {PetModule} from "./pet/pet.module";
import {ExternalApiService} from './external-api/external-api.service';
import {HttpModule} from "@nestjs/axios";
import {environments} from "./environments";
import * as process from "process";
import config from "./config";
import * as Joi from 'joi';

@Module({
    imports: [
        HttpModule,
        UserModule,
        AuthModule,
        PetModule,
        ConfigModule.forRoot({
            envFilePath:  environments[process.env.NODE_ENV] || '.env',
            load: [config],
            isGlobal: true,
            validationSchema: Joi.object({
                JWT_REFRESH_SECRET:Joi.string().required(),
                JWT_ACCESS_SECRET:Joi.string().required(),
                JWT_REFRESH_SECRET_EXPIRY:Joi.string().required(),
                JWT_ACCESS_SECRET_EXPIRY:Joi.string().required(),
                DATABASE_HOST:Joi.string().required(),
                DATABASE_USERNAME:Joi.string().required(),
                DATABASE_PASSWORD:Joi.string().required(),
                DATABASE_PORT:Joi.number().required(),
                DATABASE_NAME:Joi.string().required(),
            }),
        }),
        TypeOrmModule.forRootAsync({
            imports: [ConfigModule],
            inject: [ConfigService],
            useFactory: async (configService: ConfigService) => ({
                type: 'postgres',
                host: configService.get<string>('DATABASE_HOST'),
                port: parseInt(configService.get<string>('DATABASE_PORT')),
                username: configService.get<string>('DATABASE_USERNAME'),
                password: configService.get<string>('DATABASE_PASSWORD'),
                database: configService.get<string>('DATABASE_NAME'),
                //autoLoadEntities: true,
                entities: [User, Pet, City, Province, JwtBlacklistNestjs],
                synchronize: true,
            })
        })
    ],
    controllers: [],
    providers: [ExternalApiService],
})
export class AppModule {
}
