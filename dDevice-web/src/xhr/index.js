import axios from './configure'
export * from './basic'
export * from './device'
export * from './model'

export const login = params => axios.post('/api-auth/', params)
