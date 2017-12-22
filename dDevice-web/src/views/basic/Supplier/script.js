import { View } from '../../../mixins'
import { Supplier as api } from '../../../xhr/'

const fields = {
  // user implement
  code: {
    label: '编码',
    type: String,
    length: 20,
    rules: [{ required: true, message: '此项不能为空' }]
  },
  name: {
    label: '名称',
    type: String,
    length: 20,
    rules: [{ required: true, message: '此项不能为空' }]
  },
  phone: {
    label: '联系电话',
    type: String,
    length: 20
  },
  address: {
    label: '所在地',
    type: String,
    length: 50
  },
  remark: {
    label: '责任人',
    type: 'text',
    length: 200
  }
}

export default {
  mixins: [View],
  data() {
    return {
      api,

      fields,

      searcher: {
        placeholders: {
          code: '编码',
          name: '名称'
        },
      }
    }
  },

  created() {
    this.loadData()
  }
}
