<script setup>
import { defineProps} from 'vue';

const props = defineProps({
    tag: Object
})
</script>

<template>

<div class="rounded-lg px-1 py-0.5 bg-blue-700 text-white text-xs w-fit">{{ props.tag.name || "Tag name" }}</div>

</template>