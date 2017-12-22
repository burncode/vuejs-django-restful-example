import { View } from '../../mixins'
import { Mold as api, JlType, Management, Asset } from '../../xhr/'
import moment from 'moment'

const useStatusOptions = [
  {value: 'lh', label: '良好'},
  {value: 'jc', label: '较差'},
  {value: 'gz', label: '故障'},
  {value: 'jx', label: '检修'},
]

const fields = {
  // user implement
  qrcode: {
    label: '二维码',
    type: String,
    length: 100,
    width: 260,
    rules: [{ required: true, message: '此项不能为空' },]
  },
  code: {
    label: '模具编号',
    type: String,
    length: 50,
    width: 220,
    rules: [{ required: true, message: '此项不能为空' }]
  },
  arrival_date: {
    label: '入厂时间',
    type: 'date',
    rules: [{ required: true, message: '此项不能为空' }]
  },
  
  specs: {
    label: '规格',
    length: 100,
    type: String
  },
  hole_count: {
    label: '穴数',
    type: String,
    length: 50
  },
  duty_officer: {
    label: '财产权',
    type: String,
    length: 50
  },
  management_man: {
    label: '管理单位',
    type: String,
    length: 100
  },
  asset_class: {
    label: '资产类别',
    type: String,
    options: [],
    length: 25
  },
  jl_type: {
    label: '胶料类型',
    type: String,
    options: [],
    length: 25
  },
  jl_dosage: {
    label: '胶料用量',
    type: String,
    length: 15
  },
  location: {
    label: '位置',
    type: String,
    length: 50
  },
  use_status: {
    label: '使用状态',
    type: String,
    options: useStatusOptions,
    length: 15
  },
  price: {
    label: '参考单价',
    type: Number,
    length: 7
  },
  remark: {
    label: '备注',
    type: 'text',
    length: 140
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
          'qrcode': '二维码',
          'code': '设备编号'
        }
      }
    }
  },

  computed: {
    table() {
      let table = {}
      for(let item in this.fields) {
        if (Object.keys(table).length >= 5) break

        table[item] = this.fields[item].label
      }
      table['use_status'] = '使用状态'
      return table
    }
  },

  created() {
    this.loadData()
    this.loadOptions()
  },

  methods: {
    loadOptions() {
      Management.list().then(({data}) => {
        this.fields.management_man.options = data.map(item => ({ value: item.id, label: item.name }))
      })
      Asset.list().then(({data}) => {
        this.fields.asset_class.options = data.map(item => ({ label: item.value, value: item.id }))
      })
      JlType.list().then(({data}) => {
        this.fields.jl_type.options = data.map(item => ({ label: item.value, value: item.id }))
      })
    },

    // element-ui date v-model value changed to date string.
    beforeCreate() {
      this.form.arrival_date = moment(this.form.arrival_date).format('YYYY-MM-DD')
    }
  }
}
