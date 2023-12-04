<template>
  <n-form
    ref="formRef"
    :model="model"
    :rules="rules"
    label-placement="left"
    require-mark-placement="right-hanging"
    size="large"
    round
    :style="{
      maxWidth: '640px'
    }"
  >
    <n-form-item label="实验名称" path="title">
      <n-input v-model:value="model.title" placeholder="请输入" />
    </n-form-item>
    <n-form-item label="基础模型" path="basic_model">
      <n-select v-model:value="model.basic_model" placeholder="Select" :options="[]" />
    </n-form-item>
    <n-form-item label="训练方法" path="training_way">
      <n-select v-model:value="model.training_way" placeholder="Select" :options="[]" multiple />
    </n-form-item>
    <n-form-item label="训练设备" path="devices">
      <n-select v-model:value="model.devices" placeholder="Select" :options="[]" multiple />
    </n-form-item>
  </n-form>

  <!-- <pre
      >{{ JSON.stringify(model, null, 2) }}
    </pre> -->
</template>

<script setup lang="ts">
import { ref } from 'vue';
import type { FormInst, FormItemRule } from 'naive-ui';
import { useMessage } from 'naive-ui';

const formRef = ref<FormInst | null>(null);
const message = useMessage();
const model = ref({
  title: null,
  basic_model: null,
  training_way: null,
  devices: null
});
const rules = {
  title: {
    required: true,
    trigger: ['blur', 'input'],
    message: '请填写实验名称'
  },
  basic_model: {
    required: true,
    trigger: ['blur', 'change'],
    message: '请选择基底模型'
  },
  training_way: {
    required: true,
    trigger: ['blur', 'change'],
    message: '请选择训练方法'
  },
  devices: {
    type: 'array',
    required: true,
    trigger: ['blur', 'change'],
    message: '请选择训练设备'
  }
};

function handleValidateButtonClick(e: MouseEvent) {
  e.preventDefault();
  formRef.value?.validate(errors => {
    if (!errors) {
      message.success('验证成功');
    } else {
      console.log(errors);
      message.error('验证失败');
    }
  });
}
</script>
