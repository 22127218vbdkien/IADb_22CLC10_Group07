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
    <div>
        <RouterLink :to="`/characters/${character.id}/`">
            <div>
            <img :src="props.character.img_med" alt="character Image"/>
            <div>{{ props.character.name }}</div>
            </div>
        </RouterLink>
        
    </div>
</template>