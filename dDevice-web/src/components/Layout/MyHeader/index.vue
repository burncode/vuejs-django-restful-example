<script>
import Avatar from './Avatar'
export default {
  render (h) {
    return (
      <header class="header">
        <h1 class="header__title">CloudDisk模具设备管理系统</h1>
        <div class="header__meta user-info">
          <span class="user-info__username">欢迎，</span>
          <router-link to="/profile">
            <Avatar username={ localStorage.getItem('username') || sessionStorage.getItem('username') || 'Administration' } size={ 40 } style="display:inline-block;"/>
          </router-link>
          <router-link to="/login" class="user-info__logout">注销</router-link>
        </div>
      </header>
    )
  }
}
</script>

<style scoped>
  .header{
    width: 100%;
    height: 48px;
    line-height: 48px;
    position: relative;
    top: 0;
    left: 0;
    z-index: 20;
    background-color: #2196F3;
    color: #666666;
    padding: 0 24px;
    box-sizing: border-box;
  }
  .header:after{
    content: '';
    clear: both;
    display: table;
  }
  .header__title{
    font-size: 18px;
    font-weight: normal;
    color: white;
    margin: 0;
    float: left;
  }
  .header__meta{
    float: right;
    color: white;
    font-size: 14px;
    padding-right: 24px;
  }
  .user-info__logout{
    color: #F7BA2A;
    text-decoration: none;
    margin-left: 8px;
  }
</style>
