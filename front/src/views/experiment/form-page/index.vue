<template>
  <div class="h-full overflow-hidden">
    <n-card title="模型实验" class="h-full rounded-8px shadow-sm">
      <n-space :vertical="true">
        <stepHeader :current="step" />
        <n-space justify="center" class="mt-100px">
          <createForm v-if="step === 1" class="w-700px"></createForm>
          <configForm v-if="step === 2" class="w-700px"></configForm>
        </n-space>
        <n-space justify="center" class="mt-100px">
          <n-button @click="handleButtonClick">下一步</n-button>
        </n-space>
      </n-space>
    </n-card>
  </div>
</template>

<script setup lang="tsx">
import { ref } from 'vue';
import { NSpace, NButton } from 'naive-ui';
import { useExperimentContext } from '@/context';
import stepHeader from './components/step-headers.vue';
import createForm from './components/create-form.vue';
import configForm from './components/config-form.vue';

const { useProvide } = useExperimentContext();
const { infos, setInfo } = useProvide();

const step = ref<number>(1);
function handleButtonClick() {
  step.value = (step.value % 4) + 1;
}

</script>

<style scoped></style>
