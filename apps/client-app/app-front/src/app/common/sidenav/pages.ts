import { INavigationData } from "src/app/interfaces/nav-interface";

export const pages: INavigationData[] = [
    {
        routeLink: 'home',
        icon: 'fa fa-home',
        translation: 'nav.home',
    },
    {
        routeLink: 'about',
        icon: 'fa fa-address-card',
        translation: 'nav.about',
    },
    {
        routeLink: 'register',
        icon: 'fa fa-user-plus',
        translation: 'nav.register',
    },
    {
        routeLink: 'login',
        icon: 'fa fa-sign-in',
        translation: 'nav.login',
    },
    {
        routeLink: 'logout',
        icon: 'fa fa-sign-out',
        translation: 'nav.logout',
    }
]