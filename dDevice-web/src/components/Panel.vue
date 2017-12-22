<template>
  <div class="m-panel">
    <div class="m-panel__head">字典类型</div>
    <div class="m-panel__body">
      <slot></slot>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    title: { required: true, type: String }
  }
}
</script>

<style>
.m-panel {
  border: 1px solid #eee;
  background: #fff;
}
.m-panel__head {
  font-size: 18px;
  font-weight: bold;
  text-align: center;
  background: #EFF2F7;
  color: #424242;
  height: 48px;
  line-height: 48px;
}
</style>
