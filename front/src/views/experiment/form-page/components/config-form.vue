<template>
  <n-button @click="handleButtonClick">添加配置项</n-button>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { useMessage, useDialog } from 'naive-ui';
import CreateConfigForm from './create-config-form.vue';
const formItemTypeOptions = [
  { label: '字符串', value: 'input' },
  { label: '单选', value: 'radio' },
  { label: '多选', value: 'multiSelect' },
  { label: '开关', value: 'switch' },
  { label: '数字', value: 'number' },
  { label: '浮点数', value: 'float' }
];
const message = useMessage();
const dialog = useDialog();
function handleButtonClick() {
  dialog.success({
    title: '关闭',
    content: () => render(),
    positiveText: '保存',
    negativeText: '取消'
  });
}
// const groups = [{
//     name: "xxxx",
//     items: [{
//         id: ""
//         name: "" -> label
//         key: ""
//         default: "" -> value
//         category: ""
//         meta: {
//             options
//             placeholder
//         }
//     }]
//    }]
const customValue = ref([{ key: null, label: null, category: 'input', value: null }]);
const defaultValue = { key: null, label: null, category: 'input', value: null };
function onCreate() {
  return defaultValue;
}
</script>
