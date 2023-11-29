import { ref } from 'vue';
import type { Ref } from 'vue';
import { useContext } from '@/hooks';

interface ExperimentContext {
  infos: Ref<object>;
  setInfo: (info: object) => void;
}

const { useProvide: useExperimentProvide, useInject: useExperimentInject } = useContext<ExperimentContext>();

export function useExperimentContext() {
  const infos = ref({});

  function setInfo(info: object) {
    infos.value = info;
  }

  const experimentContext: ExperimentContext = {
    infos,
    setInfo
  };

  function useProvide() {
    return useExperimentProvide(experimentContext);
  }

  return {
    useProvide,
    useInject: useExperimentInject
  };
}

// 示例用法: A.vue为父组件， B.vue为子孙组件 C.vue为子孙组件
// A.vue
// import { useDemoContext } from '@/context';
// const { useProvide } = useDemoContext();
// const { counts, setCounts } = useProvide();

// B.vue 和 C.vue : 共享状态 counts
// import { useDemoContext } from '@/context';
// const { useInject } = useDemoContext();
// const { counts, setCounts } = useInject();
