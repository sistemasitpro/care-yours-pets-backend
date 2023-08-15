import {
    Column,
    Entity,
    JoinColumn,
    ManyToOne,
    OneToMany,
    PrimaryGeneratedColumn,
} from 'typeorm';
import { Province } from '../../../province/entities/province/province';
import { User } from '../../../user/entities/user/user';

@Entity('cities')
export class City {
    @PrimaryGeneratedColumn()
    id: number;

    @ManyToOne(() => Province, (province) => province.cities)
    @JoinColumn({ name: 'province_id' })
    province: Province;

    @Column({ type: 'varchar', length: 100, nullable: false })
    name: string;

    //Relation one to many with entity User.
    @OneToMany(() => User, (user) => user.city, { cascade: true })
    users: User[];

}
