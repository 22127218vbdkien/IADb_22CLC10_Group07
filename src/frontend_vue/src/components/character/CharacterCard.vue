<script setup>
    import { defineProps, ref } from 'vue';
    import { RouterLink } from 'vue-router';
    const props = defineProps({
        character:Object
    })

    const getCharacterID = (characterUrl) => {
        temp = characterUrl.split("/")
        return temp[temp.length - 2]
    }
</script>

<template>
    <div class="card-container hover:border-blue-600 hover:border-4 hover:border-dashed w-40 px-1 py-2 min-w-24 min-h-32">
        <RouterLink :to="`/characters/${character.id}/`">
            <div class="flex flex-col items-center">
            <img :src="props.character.img_large||props.character.img_med" alt="character Image"/>
            <div class="text-sm mt-1">{{ props.character.name }}</div>
            </div>
        </RouterLink>
    </div>
</template>