<script>
import MyHeader from './MyHeader/'
import MyFooter from './MyFooter'
import SideNav from './SideNav/'

export default {
  components: { MyHeader, MyFooter, SideNav },
  render (h) {
    return (
      <div>
        <my-header/>
        <div class="flex">
          <side-nav/>
          <div class="app-main">
            <router-view/>
            <my-footer/>
          </div>
        </div>
      </div>
    )
  }
}
</script>

<style scoped>
  .flex {
    display: flex;
  }
  .app-main {
    flex: 1;
    flex-shrink: 0;
    overflow-x: hidden; 
    position: relative;
    padding: 0 0 40px 0;
    box-sizing: border-box;
  }
</style>
