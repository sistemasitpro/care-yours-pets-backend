import {Inject, Injectable} from '@nestjs/common';
import { map, catchError } from 'rxjs/operators';
import {HttpService} from "@nestjs/axios";
@Injectable()
export class ExternalApiService {
    constructor(@Inject(HttpService) private httpService: HttpService) {
    }

    async activateUser(body: any, headers: any) {

        return this.httpService.post('https://external-api.com/endpoint', body, { headers })
            .pipe(
                map(response => response.data),
                catchError(error => {
                    console.error('There was an error!', error);
                    throw error;
                })
            )
            .toPromise();
    }
}
