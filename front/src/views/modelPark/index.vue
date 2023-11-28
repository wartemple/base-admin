<template>
  <div class="h-full overflow-hidden">
    <n-card title="模型广场"  class="h-full rounded-8px shadow-sm">
      <n-space :vertical="true" class="h-650px border-separate" >
        <loading-empty-wrapper class="h-650px" :loading="loading" :empty="empty">
          <n-layout :native-scrollbar="false">
            <n-grid class="h-650px" cols="s:1 m:2 l:4" responsive="screen" :x-gap="16" :y-gap="16" >
              <n-grid-item v-for="item in data" :key="item.id" >
                <modelCard class="h-full rounded-8px shadow-sm b-1"/>
              </n-grid-item>
            </n-grid>
          </n-layout>
        </loading-empty-wrapper>
        <n-space justify="center" class="mt-20px">
          <n-pagination
            v-model:page="page"
            v-model:page-size="pageSize"
            :page-count="100"
            show-size-picker
          />
        </n-space>
       
      </n-space>
    </n-card>
  </div>
</template>

<script setup lang="tsx">
import { onMounted, ref } from 'vue';
import { NSpace, NButton, NPopconfirm } from 'naive-ui';
import type { DataTableColumn } from 'naive-ui';
import { useLoadingEmpty } from '@/hooks';
import { getRandomInteger } from '@/utils';
import modelCard from './components/modelCard.vue'

const page = 1
const pageSize = 12

interface DataSource {
  name: string;
  age: number;
  address: string;
}

const { loading, startLoading, endLoading, empty, setEmpty } = useLoadingEmpty();
const data = [
  {id: 2},
  {id: 1},
  {id: 3},
  {id: 4},
  {id: 5},
  {id: 6},
  {id: 7},
  {id: 8},
  {id: 9},
  {id: 10},
  {id: 11},
  {id: 12},
]

const columns: DataTableColumn<DataSource>[] = [
  {
    title: 'Name',
    key: 'name',
    align: 'center'
  },
  {
    title: 'Age',
    key: 'age',
    align: 'center'
  },
  {
    title: 'Address',
    key: 'address',
    align: 'center'
  },
  {
    key: 'action',
    title: 'Action',
    align: 'center',
    render: row => {
      return (
        <NSpace justify={'center'}>
          <NButton
            size={'small'}
            onClick={() => {
              handleEdit(row.name);
            }}
          >
            编辑
          </NButton>
          <NPopconfirm
            onPositiveClick={() => {
              handleDelete(row.name);
            }}
          >
            {{
              default: () => '确认删除',
              trigger: () => <NButton size={'small'}>删除</NButton>
            }}
          </NPopconfirm>
        </NSpace>
      );
    }
  }
];

const dataSource = ref<DataSource[]>([]);

function createDataSource(): DataSource[] {
  return Array(100)
    .fill(1)
    .map((_item, index) => {
      return {
        name: `Name${index}`,
        age: getRandomInteger(30, 20),
        address: '中国'
      };
    });
}

function getDataSource() {
  startLoading();
  setTimeout(() => {
    dataSource.value = createDataSource();
    endLoading();
    setEmpty(!dataSource.value.length);
  }, 1000);
}

function getEmptyDataSource() {
  startLoading();
  setTimeout(() => {
    dataSource.value = [];
    endLoading();
    setEmpty(!dataSource.value.length);
  }, 1000);
}

function handleEdit(_name: string) {
  //
}

function handleDelete(_name: string) {
  //
}

onMounted(() => {
  getDataSource();
});
</script>

<style scoped></style>
