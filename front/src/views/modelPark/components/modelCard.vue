<template>
    <n-thing class="p-6" >
        <template #avatar><n-avatar><n-icon><svg-icon local-icon="Affiliate" /></n-icon></n-avatar>
        </template>
        <template  #header  > 货币 </template>
        <template #header-extra >
            <n-space>
                <n-button size="tiny">
                    <template #icon><n-icon><svg-icon local-icon="EditRegular" /> </n-icon>
                    </template>
                    编辑
                </n-button>
                <n-button size="tiny">
                    <template #icon><n-icon><svg-icon local-icon="ControlFilled" /> </n-icon>
                    </template>
                    精调模型
                </n-button>
            </n-space>
        </template>
        <template #description> <n-space>
                <n-tag type="info" size="tiny">
                    哪里都是你
                </n-tag>
            </n-space> </template>
        货币是为了提高交易效率而用于交换的中介商品。货币有多种形式，如贝壳粮食等自然物、金属纸张等加工品、银行卡信用卡等磁条卡、移动支付加密货币等APP。
    </n-thing>
</template>

<script lang="ts">
import { defineComponent, ref } from "vue";

export default defineComponent({
    components: {},
    setup() {
        return {
            avatar: ref(true),
            header: ref(true),
            headerExtra: ref(true),
            description: ref(true),
            footer: ref(true),
            action: ref(true),
        };
    },
});
</script>
