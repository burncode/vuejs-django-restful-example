// side-nav menus
const basic = [
  { path: "/basic/supplier", text: '供应商管理' },
  { path: "/basic/organization", text: '工厂管理' }
];

const model = [
  { path: "/model/model", text: '模具管理' }
]

const device = [
  { path: "/device/device", text: '设备管理' },
]

// 菜单栏
export default  [
  { icon: 'fa fa-database', path: 'basic', text: '基础信息', children: basic },
  { icon: 'fa fa-cube', path: 'model', text: '模具资料库', children: model },
  { icon: 'fa fa-cubes', path: 'device', text: '设备资料库', children: device }
]
