<!-- eslint-disable consistent-return -->
<template>
  <div class="h-full overflow-hidden">
    <n-form ref="formRef" :label-width="80" :model="formValue" :rules="rules" size="large">
      <n-form-item label="配置名称" path="name">
        <n-input v-model:value="formValue.name" placeholder="输入配置名称" />
      </n-form-item>
    </n-form>
  </div>
</template>

<script setup lang="tsx">
import { ref } from 'vue';
import { useMessage } from 'naive-ui';
import type { FormInst } from 'naive-ui';
import { createExperimentConfigTemplateApi } from '@/service/api'


window.$message = useMessage();
const formRef = ref<FormInst | null>(null);
const formValue = ref({
  name: ''
});
const message = useMessage();
const rules = {
  name: {
    required: true,
    message: '请输入配置名称',
    trigger: ['input']
  }
};

const handleValidateClick = () => {
  const res = formRef.value?.validate(errors => {
    if (!errors) {
      message.success('创建配置成功');
    } else {
      message.error('验证失败');
    }
  });
  console.log(res);
};

defineExpose({ handleValidateClick, formValue });
</script>

<style scoped></style>
