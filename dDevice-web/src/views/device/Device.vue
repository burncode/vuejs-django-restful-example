<template>
<m-page :title="title" id="model-list">
  
  <m-searcher v-bind="searcher" @search="loadData">
    <template slot="actions">
      <el-button type="primary" icon="plus" size="small"
        @click="() => { if ($refs.crud) { $refs.crud.create(); } }">新增</el-button>
    </template>
  </m-searcher>
  
  <crud :data="data" :form="form" :table="table" :fields="fields" inline label-width="100px"
    highlight-current-row :loading="loading" :actions="['update', 'destroy']" ref="crud"
    @create="handleCreate" @update="handleUpdate" @destroy="handleDestroy" @submit="handleSubmit">
    <template slot="expand">
      <el-table-column type="expand">
        <template slot-scope="scope">
          
        </template>
      </el-table-column>
    </template>
    <template slot="index">
      <el-table-column type="index" label="序号" width="80px">
        <template slot-scope="scope">{{ computeRowIndex(scope.$index) }}</template>
      </el-table-column>
    </template>
    <el-table-column label="状态">
      <template slot-scope="scope">
        <!-- 1:正常.2:转移中 -->
        <span v-if="scope.row.status === 1">正常</span>
        <el-badge v-else is-dot>转移中</el-badge>
      </template>
    </el-table-column>
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

<style lang="scss">
#model-list {
  .el-table__expanded-cell {
    padding: 10px 20px;
  }
}
</style>
