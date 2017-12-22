import axios from './configure'
import qs from 'qs'

export const Supplier = {
  list: (query) => axios.get(`/basic-api/suppliers?${qs.stringify(query)}`),
  create: (form) => axios.post('/basic-api/suppliers', form),
  update: (form) => axios.put(`/basic-api/suppliers/${form.id}`, form),
  destroy: (id) => axios.delete(`/basic-api/suppliers/${id}`),
}

export const Organization = {
  list: (query) => axios.get(`/basic-api/organizations?${qs.stringify(query)}`),
  create: (form) => axios.post('/basic-api/organizations', form),
  update: (form) => axios.put(`/basic-api/organizations/${form.id}`, form),
  destroy: (id) => axios.delete(`/basic-api/organizations/${id}`),
}
