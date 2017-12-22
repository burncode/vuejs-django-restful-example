import axios from './configure'
import qs from 'qs'

export const Mold = {
  list: (query) => axios.get(`/device-api/molds?${qs.stringify(query)}`),
  create: (form) => axios.post('/device-api/molds', form),
  update: (form) => axios.put(`/device-api/molds/${form.id}`, form),
  destroy: (id) => axios.delete(`/device-api/molds/${id}`),
}

export const JlType = {
  list: (query) => axios.get(`/device-api/jl-types?${qs.stringify(query)}`),
  create: (form) => axios.post('/device-api/jl-types', form),
  update: (form) => axios.put(`/device-api/jl-types/${form.id}`, form),
  destroy: (id) => axios.delete(`/device-api/jl-types/${id}`),
}
