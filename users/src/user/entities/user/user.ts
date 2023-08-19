import {
    Column,
    Entity,
    JoinColumn,
    ManyToOne,
    OneToMany,
    CreateDateColumn,
    PrimaryGeneratedColumn,
} from 'typeorm';
import { City } from '../../../city/entities/city/city';
import { Pet } from '../../../pet/entities/pet/pet';

@Entity('users')
export class User {
    @PrimaryGeneratedColumn('uuid')
    id: string;

    @Column({ type: 'varchar', length: 200, nullable: false })
    name: string;

    @Column({ type: 'varchar', length: 100, unique: true, nullable: false })
    email: string;

    @Column({ type: 'varchar', length: 16, unique: true, nullable: false })
    phone_number: string;

    //relation many to one with entity City
    @ManyToOne(() => City, (city) => city.users)
    @JoinColumn({ name: 'city_id' })
    city: City;

    @Column({ type: 'varchar', length: 300, nullable: false })
    address: string;

    @Column({ type: 'varchar', length: 128, nullable: false })
    password: string;

    @Column({ type: 'boolean', default: false, nullable: false })
    is_active: boolean;

    @Column({ type: 'boolean', nullable: false, default: false })
    is_superuser: boolean;

    @CreateDateColumn({
        type: 'timestamp',
        select: false,
        default: () => 'CURRENT_TIMESTAMP',
    })
    at_created: Date;

    @CreateDateColumn({
        type: 'timestamp',
        default: () => 'CURRENT_TIMESTAMP',
        nullable: true,
    })
    last_login: Date;

    @OneToMany(() => Pet, (pet) => pet.user)
    pets: Pet[];

    @Column({ type: 'varchar', nullable: true })
    refreshToken: string;
}
