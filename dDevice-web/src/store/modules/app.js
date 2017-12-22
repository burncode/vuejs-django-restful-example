import menus from '../../components/Layout/SideNav/menus'

export default {
  state: {
    currentCategory: null,
    currentMenu: null,
    menus
  },
  mutations: {
    SET_CURRENT_CATEGORY (state, payload) {
      state.currentCategory = payload.view
    },
    SET_CURRENT_MENU (state, payload) {
      state.currentMenu = payload.menu
    }
  }
}