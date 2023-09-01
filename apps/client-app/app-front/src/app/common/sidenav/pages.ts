import { INavigationData } from "src/app/interfaces/nav-interface";

export const pages: INavigationData[] = [
    {
        routeLink: 'home',
        icon: 'fa fa-home',
        labelPl: 'Strona Główna',
        labelEng: 'Main Page'
    },
    {
        routeLink: 'about',
        icon: 'fa fa-address-card',
        labelPl: 'O Projekcie',
        labelEng: 'About Project'
    },
    {
        routeLink: 'register',
        icon: 'fa fa-user-plus',
        labelPl: 'Zarejestruj Się',
        labelEng: 'Register'
    },
    {
        routeLink: 'login',
        icon: 'fa fa-sign-in',
        labelPl: 'Zaloguj Się',
        labelEng: 'Sign In'
    },
    {
        routeLink: 'logout',
        icon: 'fa fa-sign-out',
        labelPl: 'Wyloguj Się',
        labelEng: 'Logout'
    }
]