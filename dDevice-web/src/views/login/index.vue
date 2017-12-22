<template lang="pug">
.viewport(style="background-color: #B3E5FC;")
  el-form(:model="loginForm" ref="loginForm" :rules="rules" @keyup.enter.native="handleLogin").login-container
    .company
      h3.company__title CloudDisk模具
      .company__subtitle iModel 设备管理系统
    //- img(v-if="!loginForm.username" src="../../../static/images/fg/taiji.jpg").avatar
    m-avatar(:username="loginForm.username" :size="64").avatar

    el-form-item(prop='username')
      el-input(type='text', v-model='loginForm.username', autofocus placeholder='账号')
        template(slot='prepend')
          i.fa.fa-user-o(style='width:14px;')
    el-form-item(prop='password')
      el-input(type='password', v-model='loginForm.password', auto-complete='off', placeholder='密码')
        template(slot='prepend')
          i.fa.fa-key(style='width:14px;')

    el-checkbox.remember(v-model='isRemember') 记住密码
    el-form-item(style='width:100%;')
      el-button(type='primary', style='width:100%;', @click='handleLogin', :loading='logining') 登录

    .copyright
      span © 版权所有 <a href="http://xtits.cn/" target="_blank">杭州 CloudDev 科技有限公司</a> iModel v1.0
</template>

<script>
import { login } from '../../xhr/index';
import { TOKEN_KEY } from '../../xhr/configure'
import Avatar from './Avatar'
export default {
  components: { 'm-avatar': Avatar },
  data() {
    return {
      logining: false,
      loginForm: {
        username: '',
        password: ''
      },
      rules: {
        username: [
          { required: true, message: '请输入账号！', trigger: 'blur' },
        ],
        password: [
          { required: true, message: '请输入密码！', trigger: 'blur' },
        ]
      },
      isRemember: false
    };
  },
  methods: {
    handleLogin() {
      // 验证表单
      this.$refs.loginForm.validate(valid => {
        if (valid) {
          login(this.loginForm).then(({ data, status }) => {
            if (status === 200) {
              this.saveUsername(this.loginForm.username);
              this.saveToken(data.token);
              this.redirect();
            }
          });
        }
      });
    },
    saveToken(token) {
      if (this.isRemember) {
        localStorage.setItem(TOKEN_KEY, token);
      } else {
        sessionStorage.setItem(TOKEN_KEY, token);
      }
    },
    redirect() {
      let redirect = this.$route.query.redirect;
      redirect = redirect ? redirect : '/';
      this.$router.push({ path: redirect });
    },
    saveUsername(username) {
      if (this.isRemember) {
        localStorage.setItem('username', username);
      } else {
        sessionStorage.setItem('username', username);
      }
    }
  }
}
</script>

<style lang="scss">
.login-container {
  border-radius: 5px;
  background-clip: padding-box;
  position: absolute;
  top: 0;
  left: 0;
  bottom: 0;
  right: 0;
  margin: auto;
  width: 20%;
  height: 40%;
  min-height: 400px;
  min-width: 336px;
  padding: 24px 16px 8px 16px;
  background: #fff;
  border: 1px solid #eaeaea;
  box-shadow: 0 0 25px #cac6c6;
  .avatar {
    margin: 16px auto 20px auto;
    display: block;
    max-width: 64px;
    max-height: 64px;
    border-radius: 50%;
  }
  .remember {
    margin: 8px 0px 24px 0px;
  }
}

.company {

  .company__title {
    color: #26A69A;
    font-size: 1.72em;
    font-size: 600;
    text-align: center;
    margin-top: 20px;
    margin-bottom: 4px;
    letter-spacing: 2px;
  }
  .company__subtitle {
    text-align: center;
    font-size: 1.1em;
    font-family: Arial, Helvetica;
    color: #26A69A;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  }
}

.copyright {
  position: fixed;
  width: 100%;
  text-align: center;
  left: 0;
  bottom: 10px;
  font-size: 14px;
  // color: #898989;
  color: #fbdcdc;

  a {
    color: inherit;
    text-decoration: none;
    &:hover {
      text-decoration: underline;
    }
  }
}

// IE login form style compatibility
.login-container .el-form-item__content {
  line-height: normal;
}
</style>
