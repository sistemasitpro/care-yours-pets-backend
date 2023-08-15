import {
    Column,
    JoinColumn,
    Entity,
    ManyToOne,
    PrimaryGeneratedColumn,
    CreateDateColumn,
} from 'typeorm';
import { User } from '../../../user/entities/user/user';

@Entity('pets')
export class Pet {
    @PrimaryGeneratedColumn('uuid')
    uid: string;
    @ManyToOne(() => User, (user) => user.uid, { onDelete: 'CASCADE' })
    @JoinColumn({ name: 'user_uid' })
    user: User;
    @Column({ type: 'varchar', length: 200, nullable: false })
    name: string;
    @Column({ type: 'int', nullable: false })
    age: number;
    @Column({ type: 'varchar', length: 100, nullable: false })
    type_pet: string;
    @Column({ type: 'varchar', length: 100, nullable: false })
    specie: string;
    @Column({ type: 'varchar', length: 200, nullable: true })
    preexisting_conditions: string;
    @CreateDateColumn({ type: 'timestamp', default: () => 'CURRENT_TIMESTAMP' })
    at_created: Date;
}
