<template>
  <div class="h-full overflow-hidden">
    <n-card title="模型实验" class="h-full rounded-8px shadow-sm">
      <n-space :vertical="true">
        <n-space>
          <n-button @click="getDataSource">有数据</n-button>
          <n-button @click="getEmptyDataSource">空数据</n-button>
        </n-space>
        <loading-empty-wrapper class="h-620px" :loading="loading" :empty="empty">
          <n-data-table
            :columns="columns"
            :data="dataSource"
            :flex-height="true"
            class="h-620px"
            :pagination="paginationReactive"
          />
        </loading-empty-wrapper>
      </n-space>
    </n-card>
  </div>
</template>

<script setup lang="tsx">
import { onMounted, ref, reactive } from 'vue';
import { NSpace, NButton, NPopconfirm } from 'naive-ui';
import type { DataTableColumn } from 'naive-ui';
import { useLoadingEmpty } from '@/hooks';
import { getRandomInteger } from '@/utils';
import { useExperimentContext } from '@/context';
const { useProvide } = useExperimentContext();
const { infos, setInfo } = useProvide();

onMounted(() => {
  getDataSource();
});
</script>

<style scoped></style>
