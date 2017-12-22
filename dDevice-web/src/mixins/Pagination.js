export default {
  data() {
    return {
      pagination: {
        total: null,        
        currentPage: 1,
        pageSizes: [1, 5, 10, 20, 50],
        pageSize: 10,
        layout: 'sizes, prev, pager, next'
      }
    }
  },

  computed: {
    _pagination() {
      return {
        page_size: this.pagination.pageSize,
        page: this.pagination.currentPage
      }
    }
  },

  methods: {
    loadData() {},

    handleSizeChange(val) {
      this.pagination.pageSize = val
      this.loadData()
    },

    handleCurrentChange(val) {
      this.pagination.currentPage = val
      this.loadData()
    },

    computeRowIndex(index) {
      return (this.pagination.currentPage - 1) * this.pagination.pageSize + index + 1
    },

    setPagination(count, length) {
      this.pagination.total = count

      // stupid search pagination
      if (!length && this.pagination.currentPage > 1) {
        this.pagination.currentPage = 1
        return this.loadData()
      }
    }
  }
}
