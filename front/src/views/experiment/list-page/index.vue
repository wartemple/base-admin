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

interface DataSource {
  name: string;
  age: number;
  address: string;
}

const { loading, startLoading, endLoading, empty, setEmpty } = useLoadingEmpty();

const columns: DataTableColumn<DataSource>[] = [
  {
    title: '实验名称',
    key: 'title',
    align: 'center'
  },
  {
    title: '使用显卡',
    key: 'device',
    align: 'center'
  },
  {
    title: '基础模型',
    key: 'model',
    align: 'center'
  },
  {
    title: '训练方法',
    key: 'trainWay',
    align: 'center'
  },
  {
    title: '状态',
    key: 'status',
    align: 'center'
  },
  {
    key: 'action',
    title: '操作',
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
        model: `Name${index}`,
        title: getRandomInteger(30, 20),
        device: '1,2,3,4',
        trainWay: 'lora',
        status: 1
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

const paginationReactive = reactive({
  page: 2,
  pageSize: 10,
  showSizePicker: true,
  pageSizes: [10, 15, 20],
  onChange: (page: number) => {
    paginationReactive.page = page;
  },
  onUpdatePageSize: (pageSize: number) => {
    paginationReactive.pageSize = pageSize;
    paginationReactive.page = 1;
  }
});
onMounted(() => {
  getDataSource();
});
</script>

<style scoped></style>
