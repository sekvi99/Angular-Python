export interface UserDto {
    username: string,
    email: string,
    password: string,
    connectedMail?: string | null
}