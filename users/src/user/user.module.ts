import { Module } from '@nestjs/common';
import {TypeOrmModule} from "@nestjs/typeorm";
import {User} from "./entities/user/user";
import {City} from "../city/entities/city/city";
import {UserController} from "./user.controller";
import {UserService} from "./user.service";
import {ExternalApiService} from "../external-api/external-api.service";
import {HttpModule} from "@nestjs/axios";

@Module({
    imports: [HttpModule,TypeOrmModule.forFeature([User, City])],
    controllers: [UserController],
    providers: [UserService, ExternalApiService],
    exports: [TypeOrmModule, UserService,ExternalApiService],
})
export class UserModule {

}
