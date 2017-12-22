import axios from 'axios'
import { Message } from 'element-ui'
import settings from 'settings'
import qs from 'qs'

export const baseUrl = `http://${settings.SERVER_HOST}:${settings.SERVER_PORT}/`

export const TOKEN_KEY = 'imodel-token'

const transformRequest = (data={}, headers) => {
  if (typeof data === 'string') return data
  
  let Authorization = localStorage.getItem(TOKEN_KEY) || sessionStorage.getItem(TOKEN_KEY) || null
  if (Authorization) {
    headers.Authorization = 'Token ' + Authorization
    // data.oauth = Authorization
  }

  return qs.stringify(data)
}

let _axios = axios.create({
  baseURL: baseUrl,
  headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
  transformRequest: [transformRequest],
  timeout: 8000
})

_axios.interceptors.response.use(response => response, error => {
  let { response } = error
  let { data } = response
  let errorMsg = ''
  for (let k in data) {
    errorMsg += data[k] instanceof Array ? data[k].join(' ') : data[k]
  }
  Message.error(errorMsg)
  return response
})

export default _axios
