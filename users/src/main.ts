import {NestFactory} from '@nestjs/core';
import {AppModule} from './app.module';
import {SwaggerModule, DocumentBuilder} from '@nestjs/swagger';
import {BadRequestException, ValidationError, ValidationPipe} from "@nestjs/common";

async function bootstrap() {

    const app = await NestFactory.create(AppModule, {
        cors: true,
    });

    app.setGlobalPrefix('v1');
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

    const config = new DocumentBuilder()
        .setTitle('CAREYOURSPETS')
        .setDescription('API NESTJS careyourspets ')
        .setVersion('1.0')
        .addTag('Pets', 'The /pets endpoint is a part of the PetStore API. It allows clients to access information about available pets')
        .addTag('users', 'Requests related to the creation of new users')
        .addTag('auth', 'Endpoint used for authentication and authorization')
        .addBearerAuth(
            {
                // I was also testing it without prefix 'Bearer ' before the JWT
                description: `[just text field] Please enter token in following format: Bearer <JWT>`,
                name: 'Authorization',
                bearerFormat: 'Bearer', // I`ve tested not to use this field, but the result was the same
                scheme: 'Bearer',
                type: 'http', // I`ve attempted type: 'apiKey' too
                in: 'Header',
            },
            'access-token', // This name here is important for matching up with @ApiBearerAuth() in your controller!
        )
        .build();
    const document = SwaggerModule.createDocument(app, config);
    SwaggerModule.setup('api', app, document);

    await app.listen(3000);
}

bootstrap();
