import { Module } from '@nestjs/common';
import { TypeOrmModule } from '@nestjs/typeorm';
import {ConfigModule} from "@nestjs/config";
import {User} from "./user/entities/user/user";
import {Pet} from "./pet/entities/pet/pet";
import {Province} from "./province/entities/province/province";
import {City} from "./city/entities/city/city";
import {JwtBlacklistNestjs} from "./jwt-blacklist-nestjs/entities/jwt-blacklist-nestjs/jwt-blacklist-nestjs";
import { UserController } from './user/user.controller';
import { UserService } from './user/user.service';
import { UserModule } from './user/user.module';
@Module({
  imports: [UserModule,
    ConfigModule.forRoot({
      isGlobal: true,
    }),
    TypeOrmModule.forRoot({
      type: 'postgres',
      host: process.env.DATABASE_HOST,
      port: parseInt(process.env.DATABASE_PORT),
      username: process.env.DATABASE_USERNAME,
      password: process.env.DATABASE_PASSWORD,
      database: process.env.DATABASE_NAME,
      //autoLoadEntities: true,
      entities: [User, Pet, City, Province, JwtBlacklistNestjs],
      synchronize: false,
    }),
    UserModule,
  ],
  controllers: [],
  providers: [],
})
export class AppModule {}
