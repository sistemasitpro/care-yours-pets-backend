import {registerAs} from '@nestjs/config';
import * as process from "process";

export default registerAs('config', () => {
    return {
        JWT_REFRESH_SECRET: process.env.JWT_REFRESH_SECRET,
        JWT_REFRESH_SECRET_EXPIRY: process.env.JWT_REFRESH_SECRET_EXPIRY,
        JWT_ACCESS_SECRET: process.env.JWT_ACCESS_SECRET,
        JWT_ACCESS_SECRET_EXPIRY: process.env.JWT_ACCESS_SECRET_EXPIRY,
        DATABASE_HOST: process.env.DATABASE_HOST,
        DATABASE_USERNAME: process.env.DATABASE_USERNAME,
        DATABASE_PASSWORD: process.env.DATABASE_PASSWORD,
        DATABASE_PORT: process.env.DATABASE_PORT,
        DATABASE_NAME: process.env.DATABASE_NAME,
    };
});