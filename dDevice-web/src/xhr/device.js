import axios from './configure'
import qs from 'qs'

export const Device = {
  list: (query) => axios.get(`/device-api/devices?${qs.stringify(query)}`),
  create: (form) => axios.post('/device-api/devices', form),
  update: (form) => axios.put(`/device-api/devices/${form.id}`, form),
  destroy: (id) => axios.delete(`/device-api/devices/${id}`),
}

export const Management = {
  list: () => axios.get('/device-api/managements')
}

export const Asset = {
  list: () => axios.get('/device-api/assets')
}
