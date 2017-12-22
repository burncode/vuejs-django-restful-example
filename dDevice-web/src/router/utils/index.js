// stupid webpack build will compile the component's name to a single letter.
// so component.name is not accessable for production.
import { kebabCase } from 'lodash'

export const compConfig = (modules, baseUrl) => modules.components.map(component => ({
  component: modules[component],
  name: component,
  path: baseUrl + kebabCase(component)
}))
