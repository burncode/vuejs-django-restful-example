<template>
<m-page :title="title">
  <m-searcher v-bind="searcher" @search="loadData">
    <template slot="actions">
      <el-button type="primary" icon="plus" size="small"
        @click="() => { if ($refs.crud) { $refs.crud.create(); } }">新增</el-button>
    </template>
  </m-searcher>

  <crud :data="data" :form="form" :fields="fields" label-width="80px"
    :loading="loading" :actions="['update', 'destroy']" ref="crud"
    @create="handleCreate" @update="handleUpdate" @destroy="handleDestroy" @submit="handleSubmit">
    <template slot="index">
      <template>
        <el-table-column type="index" label="序号" width="80px">
          <template slot-scope="scope">{{ computeRowIndex(scope.$index) }}</template>
        </el-table-column>
      </template>
    </template>
  </crud>

  <el-pagination
    v-if="pagination.total > 0"
    v-bind="pagination"
    @size-change="handleSizeChange"
    @current-change="handleCurrentChange"
    style="margin-top:8px; float:right;">
  </el-pagination>
  <div style="clear:both;"></div>
</m-page>
</template>

<script src="./script.js"></script>
