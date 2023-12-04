<template>
  <n-steps v-model:current="current">
    <n-step title="实验信息" description="这一步，你将创建一个训练实验" />
    <n-step title="实验配置" description="配置实验所需的相关参数" />
    <n-step title="数据集配置" description="完成数据集上传和对其进行预处理" />
    <n-step title="完成创建" description="你已完成实验的创建。" />
  </n-steps>
</template>

<script setup lang="ts">
import { ref } from 'vue';

const current = ref<number | undefined>(1);
</script>
