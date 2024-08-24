
<template>
    <div class="container" @mouseleave="closeDropdown">
        <p>Select {{ filterName }}</p>
        <div  class="dropdown-wrapper  max-w-52 min-w-40">
            <div  @click="toggleDropdown"   class=" bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 dropdown-selected-option">
                {{ getSelectedValue}}
            </div>
            <div v-if="visibleDropdown" class="options-dropdown overflow-auto max-h-56 max-w-full">
                <div class="max-w-full bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 option" 
                    v-for="(option, index) in options" 
                    :key="index"
                    @click="toggleSelection(option)">
                    {{ option.name || option }}
                </div>
            </div>
        </div>
    </div>
    
</template>

<script setup>
    import { computed, ref } from 'vue';
    import { onMounted } from 'vue';
    const emit = defineEmits(['changeTagLists'])
    const props = defineProps({
        options: Array,
        filterName: String
    })
    const selectedOption = ref(null)
    const visibleDropdown = ref(false)
    const toggleSelection = (option) =>{
        selectedOption.value = option.name; 
    }

    const getSelectedValue = computed(() =>{
        return (selectedOption.value?.name || selectedOption.value || 'Select sth' )
    })

    const toggleDropdown = () => {
        visibleDropdown.value = !visibleDropdown.value
    }
    
    const closeDropdown = () =>{
        visibleDropdown.value = false
    }
</script>
