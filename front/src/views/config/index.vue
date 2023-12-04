<template>
  <div class="h-full overflow-hidden">
    <n-card title="配置管理" class="h-full rounded-8px shadow-sm">
      <n-space :vertical="true">
        <n-space>
          <n-button @click="openCreateDialog">新增配置</n-button>
          <!-- <n-button @click="">导入配置</n-button> -->
        </n-space>
      </n-space>
    </n-card>
  </div>
</template>

<script setup lang="tsx">
crud
import { onMounted, ref, reactive, h } from 'vue';
import { NSpace, NButton, NPopconfirm, useDialog } from 'naive-ui';
import type { DataTableColumn } from 'naive-ui';
import { useLoadingEmpty } from '@/hooks';
import { getRandomInteger } from '@/utils';
import createForm from './create-form.vue';

const createDialog = useDialog();
const cForm = ref<any>();
function openCreateDialog() {
  createDialog.info({
    title: '新增配置',
    positiveText: '保存',
    negativeText: '取消',
    content() {
      return h(createForm, { ref: cForm }, '');
    },
    onPositiveClick: (e: MouseEvent) => {
      const a = cForm.value.handleValidateClick(e);
      console.log(a);
    }
  });
}
</script>

<style scoped></style>
