<script setup>
import { defineProps,defineEmits} from 'vue';
import { useRoute, useRouter, RouterLink} from 'vue-router';
import router from '@/router';
const props = defineProps({
    _start: Number,
    _limit: Number
})

const _route = useRoute()
const _router = useRouter()
console.log(_route.path)

const start = props._start - 2 > 0 ? props._start - 2 : 1
const end =  (props._start - 2 > 0 ? props._start - 2 : 1) + props._limit - 1

const calcEnd = () =>{
    return _limit + _start - 1 
}
const arrayRange = (start1, stop1, step1) =>
    Array.from(
    { length: (stop1 - start1) / step1 + 1 },
    (value, index) => start1 + index * step1
);

const emit = defineEmits(['changePage'])

const toPage = (event) => {
    console.log(event)
    emit('changePage', event)
}
</script>


<template>
    <div class="bar-wrapper">
        <span><i class="pi pi-angle-double-left  text-blue-500 hover:text-blue-100 hover:bg-blue-500"></i></span>
        <span @click="toPage(value)" v-for="(value, index) in arrayRange(start, end, 1)" :key="index" class=" text-blue-500 hover:text-blue-100 hover:bg-blue-500 hover:cursor-pointer"> {{ value }}</span>
        <span><i class="pi pi-angle-double-right text-blue-500 hover:text-blue-100 hover:bg-blue-500"></i></span>
    </div>
</template>