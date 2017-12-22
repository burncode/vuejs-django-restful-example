import { View } from '../../mixins'
import { Device as api, Management, Asset } from '../../xhr/'
import moment from 'moment'

const fields = {
  // user implement
  qrcode: {
    label: '二维码',
    type: String,
    length: 100,
    rules: [{ required: true, message: '此项不能为空' }, /*{ validator: this.serverHasQrCode, message: '服务器中已有这个' }*/]
  },
  name: {
    label: '设备名称',
    type: String,
    length: 50,
    rules: [{ required: true, message: '此项不能为空' }]
  },
  code: {
    label: '设备编号',
    type: String,
    length: 50,
    rules: [{ required: true, message: '此项不能为空' }]
  },
  asset_no: {
    label: '资产编号',
    type: String,
    length: 20
  },
  specs: {
    label: '规格/型号',
    length: 100,
    type: String
  },
  arrival_date: {
    label: '入厂时间',
    length: 15,
    type: 'date'
  },
  
  duty_officer: {
    label: '财产权',
    type: String,
    length: 50
  },
  management_man: {
    label: '管理单位',
    type: Number,
    options: [],
    length: 100
  },
  asset_class: {
    label: '资产类别',
    type: Number,
    options: [],
    length: 25
  },
  use_status: {
    label: '设备状态',
    type: String,
    length: 20
  },
  price: {
    label: '参考单价(元)',
    type: Number,
    length: 8
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

      searcher: {
        placeholders: {
          'qrcode': '二维码',
          'name': '设备名称',
          'code': '设备编号'
        }
      },

      fields
    }
  },

  computed: {
    table() {
      let table = {}
      for(let item in this.fields) {
        if (Object.keys(table).length >= 5) break

        table[item] = this.fields[item].label
      }
      return table
    }
  },

  created() {
    this.loadData()
    this.loadOptions()
  },
  
  watch: {
    'form.price'(val, newVal) {
      if (val && val.toString().length > this.fields.price.length) {
        this.$nextTick(() => {
          this.form.price = Number(val.toString().slice(0, this.fields.price.length))
        })
      }
    }
  },

  methods: {

    loadOptions() {
      Management.list().then(({data}) => {
        this.fields.management_man.options = data.map(item => ({ value: item.id, label: item.name }))
      })
      Asset.list().then(({data}) => {
        this.fields.asset_class.options = data.map(item => ({ label: item.value, value: item.id }))
      })
    },

    // element-ui date v-model value changed to date string.
    beforeCreate() {
      this.form.arrival_date = moment(this.form.arrival_date).format('YYYY-MM-DD')
    }
  }
}
