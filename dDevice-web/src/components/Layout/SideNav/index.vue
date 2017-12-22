<template>
  <div class="el-menu-wrap">
    <el-menu theme="light" unique-opened :collapse="isCollapse" :class="[{'side-nav--collapse': isCollapse}, 'side-nav']" :router="true">
      <div class="current-menu"><i :class="icon"></i><span class="current-menu__title">{{ name }}</span></div>
      <el-submenu :key="index" v-for="(menu, index) in menus" :index="menu.path" align="left">
        <template slot="title">
          <i :class="menu.icon" style="width:20px; text-align:center;"></i>
          <span slot="title">{{ menu.text }}</span>
        </template>
        <el-menu-item :key="index" v-for="(o, index) in menu.children" :index="o.path" @click="handleClick(o)">{{ o.text }}</el-menu-item>
      </el-submenu>
    </el-menu>
  </div>
</template>

<script>
import menus from './menus'

export default {
  data() {
    return {
      isCollapse: false,
      menus: menus,
    }
  },
  computed: {
    name() {
      return (this.$store.state.app.currentCategory || '').name || '首页'
    },
    icon() {
      return ((this.$store.state.app.currentCategory || '').meta || '').icon || 'fa fa-home fa-lg'
    }
  },
  methods: {
    handleClick(menu) {
      this.$store.commit({ type: 'SET_CURRENT_MENU', menu })
    }
  }
}
</script>

<style lang="scss" scoped>
.el-menu-wrap {
  min-height: calc(100vh - 48px);
  overflow-y: scroll;
  &::-webkit-scrollbar {
    display: none
  }
}

.side-nav {
  border-right: 1.1px solid #d3d3d3;
  width: 170px;
  box-sizing: border-box;
  overflow: hidden;
  min-height: 100%;
  flex: 170px;
  flex-shrink: 0;
}

.side-nav.side-nav--collapse {
  width: auto;
}

.current-menu {
  border-bottom: 1.1px solid #d3d3d3;
  max-height: 65.1px;
  height: 64px;
  display: flex;
  align-items: center;
  padding: 0 8px 0 16px;
  .side-logo {
    width: 40px;
    height: 40px;
  }
}
.current-menu__title {
  margin-left: 16px;
  margin-right: 16px;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  font-weight: 400;
  letter-spacing: .005em;
  font-size: 18px;
  line-height: 20px;
}
</style>
