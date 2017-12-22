<template>
  <footer class="footer">
    <el-row type="flex">
      <el-col :span="18">
        <p class="footer__copyright">© 版权所有 杭州贤二智能科技有限公司 iModel v1.0</p>
      </el-col>
    </el-row>
  </footer>
</template>

<style scoped>
  .footer{
    position: absolute;
    left: 0;
    bottom: 0;
    width: 100%;
  }
  .footer__copyright{
    font-size: 14px;
    color: #333;
    padding-left: 16px;
  }
</style>
