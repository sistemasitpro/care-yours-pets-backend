import { Column, Entity, CreateDateColumn, PrimaryGeneratedColumn } from 'typeorm';

@Entity('jwt_blacklist_user')
export class JwtBlacklistNestjs {
    @PrimaryGeneratedColumn('uuid')
    uid: string;
    @Column({ type: 'varchar', nullable: false, unique: true })
    token: string;
    @Column({ type: 'varchar', nullable: false, unique: true })
    jti: string;
    @Column({ type: 'varchar', length: 30, nullable: false })
    type_token: string;
    @CreateDateColumn({ type: 'timestamp', default: () => 'CURRENT_TIMESTAMP' })
    expires_at: string;
    @CreateDateColumn({ type: 'timestamp', default: () => 'CURRENT_TIMESTAMP' })
    at_created: string;
}
