export default {
  computed: {
    title() {
      let { fullPath } = this.$route
      let { menus } = this.$store.state.app
      let find;
      menus.find(menu => {
        find = menu.children.find(m => m.path === fullPath)
        return find
      })
      return find.text
    }
  }
}
