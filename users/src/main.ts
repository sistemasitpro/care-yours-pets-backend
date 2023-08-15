import { NestFactory } from '@nestjs/core';
import { AppModule } from './app.module';
import {BadRequestException, ValidationError, ValidationPipe} from "@nestjs/common";

async function bootstrap() {
  const app = await NestFactory.create(AppModule);
  app.useGlobalPipes(
      new ValidationPipe({
        exceptionFactory: (validationErrors: ValidationError[] = []) => {
          const result: { [property: string]: string[] } = {};
          validationErrors.forEach((error) => {
            if (!(error.property in result)) {
              result[error.property] = [];
            }
            result[error.property].push(...Object.values(error.constraints));
          });
          return new BadRequestException(result);
        },
      }),
  );
  app.setGlobalPrefix('v1');
  await app.listen(3000);
}
bootstrap();
