import { Column, Entity, OneToMany, PrimaryGeneratedColumn } from 'typeorm';
import { City } from '../../../city/entities/city/city';

@Entity('provinces')
export class Province {
    @PrimaryGeneratedColumn()
    id: number;

    @Column({ type: 'varchar', nullable: false, length: 100 })
    name: string;

    @OneToMany(() => City, (city) => city.province, { cascade: true })
    cities: City[];
}
