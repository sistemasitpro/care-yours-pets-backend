import { Module } from '@nestjs/common';
import { TypeOrmModule } from '@nestjs/typeorm';
import {ConfigModule} from "@nestjs/config";
import {User} from "./user/entities/user/user";
import {Pet} from "./pet/entities/pet/pet";
import {Province} from "./province/entities/province/province";
import {City} from "./city/entities/city/city";
import {JwtBlacklistNestjs} from "./jwt-blacklist-nestjs/entities/jwt-blacklist-nestjs/jwt-blacklist-nestjs";
import { UserModule } from './user/user.module';
import {AuthModule} from "./auth/auth.module";
import {PetModule} from "./pet/pet.module";
import { ExternalApiService } from './external-api/external-api.service';
import {HttpModule} from "@nestjs/axios";
@Module({
  imports: [
    HttpModule,
      UserModule,
    AuthModule,
      PetModule,
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
    })
  ],
  controllers: [],
  providers: [ExternalApiService],
})
export class AppModule {}
