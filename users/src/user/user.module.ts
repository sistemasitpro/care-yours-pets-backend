import { Module } from '@nestjs/common';
import {TypeOrmModule} from "@nestjs/typeorm";
import {User} from "./entities/user/user";
import {City} from "../city/entities/city/city";
import {UserController} from "./user.controller";
import {UserService} from "./user.service";

@Module({
    imports: [TypeOrmModule.forFeature([User, City])],
    controllers: [UserController],
    providers: [UserService],
    exports: [TypeOrmModule, UserService],
})
export class UserModule {

}
