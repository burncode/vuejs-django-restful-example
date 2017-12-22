export const Supplier = () => import(/* webpackChunkName: "basic" */ './Supplier/')
export const Organization = () => import(/* webpackChunkName: "basic" */ './Organization/')

export const components = ['Supplier', 'Organization']

export const baseUrl = '/basic/'
