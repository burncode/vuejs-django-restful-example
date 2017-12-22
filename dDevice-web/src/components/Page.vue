<script>
export default {
  props: {
    title: { required: true, type: String },
  },
  render(h) {
    return (
      <div class="m-page">
        <div class="m-page__header">
          <span class="m-page__title">{ this.title }</span>
          { this.$slots.actions &&
            <div class="m-page__action-group">
              { this.$slots.actions }
            </div>
          }
        </div>
        <div class="m-page__body">
          <router-view />
          { this.$slots.default }
        </div>
      </div>
    )
  }
}
</script>

<style scoped>
.m-page__header {
  border-bottom: 1.1px solid #d3d3d3;
  max-height: 65.1px;
  height: 64px;
  display: flex;
  align-items: center;
  padding: 0 8px 0 16px;
}
.m-page__header .m-page__title {
  font-weight: 400;
  letter-spacing: .005em;
  font-size: 18px;
  line-height: 20px;
  margin-left: 8px;
  color: #000;
}
.m-page__header .m-page__action-group {
  margin-left: 56px;
  flex: 1;
}
.m-page__body {
  padding: 8px;
}
</style>
