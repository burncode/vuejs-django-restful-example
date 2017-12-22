import { kebabCase } from 'lodash'
import Page from './Page'
import Searcher from './Searcher'
import RowInput from './RowInput'

export const comps = {
  Page,
  Searcher,
  RowInput
}

export default function install(Vue, opt={prefix: 'm'}) {
  for (let k in comps) {
    Vue.component(opt.prefix + '-' + kebabCase(k), comps[k])
  }
}
