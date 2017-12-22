<template lang="pug">
  .profile-modify(style="width:600px; margin:0 auto; transform:translateY(50%); background:#EFF2F7; padding:16px;")
    h5(style="font-size:20px; text-align:center; color:#666; font-weight:normal; margin:16px;") 用户密码修改
  
    el-form(ref="form" :rules="rules" :model="model" @keyup.13.native="changePasswd").clearfix
      el-form-item(label="原密码" :label-width="lw" prop="passwd0")
        el-input(type="password" v-model="passwd0" placeholder="请输入新密码")      
      el-form-item(label="新密码" :label-width="lw" prop="passwd1")
        el-input(type="password" v-model="passwd1" placeholder="请输入新密码")
      el-form-item(label="新密码" :label-width="lw" prop="passwd")
        el-input(type="password" v-model="passwd" placeholder="请再次输入新密码")
      .fr
        el-button(@click="empty") 清 空
        el-button(type="primary" @click="changePasswd") 修 改
</template>

<script>
import { User } from '../xhr'

export default {
  data() {
    const different = (rules, value, callback) => {
      if (this.passwd1 !== this.passwd) {
        callback(new Error('两次输入的密码不一致'))
      } else {
        callback()
      }
    }

    return {
      lw: '80px',
      passwd0: null,
      passwd1: null,
      passwd: null,

      rules: {
        passwd0: [{ required: true, message: '此项不能为空', trigger: 'change' }],
        passwd1: [{ required: true, message: '此项不能为空', trigger: 'change' },
          { pattern: /.{2}.*/, message: '密码长度必须不小于2位' }],
        passwd: [{ validator: different, trigger: 'change' }, { required: true, message: '此项不能为空', trigger: 'change' }],
      }
    }
  },
  computed: {
    model() {
      let { passwd0, passwd1, passwd } = this
      return {
        passwd0,
        passwd1,
        passwd
      }
    }
  },
  methods: {
    empty() {
      this.passwd0 = null
      this.passwd1 = null
      this.passwd = null

      if (this.$refs.form) {
        this.$refs.form.resetFields()
      }
    },
    checkPasswd(passwd) {
      return new Promise((resolve, reject) => {
        let valid = false
        if (passwd !== this.passwd0) {
          this.$message.error('原密码不正确，请确认后再修改')
          reject(valid)
        } else {
          valid = true
        }
        resolve(valid)
      })
    },
    changePasswd() {
      if (this.$refs.form) {
        this.$refs.form.validate(valid => {
          if (valid) {

            this.$confirm(`您确认要更改密码，并且使用新密码重新登录？`, '确认', {type: 'warning'}).then(_ => {
              let userCode = localStorage.getItem('userCode') || sessionStorage.getItem('userCode') || ''
              User.list({ userCode }).then(({data}) => {
                if (data.data.data.length) {
                  let user = data.data.data[0]
                  this.checkPasswd(user.passWord).then(ok => {
                    let _user = { ...user, passWord: this.passwd }
                    User.update({ data: JSON.stringify(_user) }).then(({data}) => {
                      this.$report(data, 'update', () => {
                        this.empty()
                        this.$router.push({ name: 'Login' })
                      })
                    })
                  }).catch(_ => { })
                }
              })
            }).catch(_ => { })



          }
        })
      }

      
    }
  }
}
</script>
