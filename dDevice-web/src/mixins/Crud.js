import { Simple } from 'vue-element-crud'
import Pagination from './Pagination'

export default {
  mixins: [Simple, Pagination],
  data() {
    return {
      api: {},

      loading: false
    }
  },

  methods: {
    loadData() {
      let kw = { ...this.searcher.kw }
      
      this.api.list({ ...this._pagination, ...kw }).then(({status, data}) => {
        if (status === 200) {
          this.data = data.results
          this.setPagination(data.count, data.results.length)
        }
      })
    },

    // element-ui date v-model value changed to date string.
    beforeCreate() {},

    handleSubmit(status, closeDialog) {
      const submitSuccess = (data) => {
        this.loadData()
        closeDialog()
      }

      this.loading = true

      if (status === 0) {
        this.beforeCreate()
        this.api.create(this.form).then(({status, data}) => {
          this.loading = false

          if (status === 201) {
            this.$message.success('新增成功！');
            submitSuccess()
          }
        })
      } else {
        this.api.update(this.form).then(({status, data}) => {
          this.loading = false

          if (status === 200) {
            this.$message.success('修改成功！');
            submitSuccess()
          }
        })
      }
    },

    handleDestroy(row) {
      this.api.destroy(row.id).then(({status, data}) => {
        if (status === 204) {
          this.$message.success('删除成功！');
          this.loadData()
        }
      })
    }
  }
}
