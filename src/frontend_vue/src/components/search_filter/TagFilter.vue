
<template>
    <div class="container" @mouseleave="closeDropdown">
        <p class="font-semibold block mb-1 text-sm  text-gray-900" >Select {{ filterName }}</p>
        <div  class="dropdown-wrapper  max-w-52 min-w-40">
            <div  @click="toggleDropdown"  class=" bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dropdown-selected-option">
                {{ getSelectedValue}}
            </div>
            <div v-if="visibleDropdown" class="options-dropdown overflow-auto max-h-56 max-w-full z-50">
                <div class="max-w-full bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 option" 
                    v-for="(option, index) in props.options" 
                    :key="index"
                    @click="toggleSelection(option)">
                    {{ option.name || option }}
                </div>
            </div>
        </div>
    </div>
    
</template>

<script setup>
    import { computed, ref, defineEmits, onMounted} from 'vue';
 
    const emit = defineEmits(['changeTagLists'])
    const props = defineProps({
        options: Array,
        filterName: String, 
        isMultiple: Boolean,
        hasValue: String,
    })
    const selectedOption = ref([])
    const selectedOptionDisplay = ref([])
    const visibleDropdown = ref(false)
    
    const toggleSelection = (option) =>{
        if (props.isMultiple){
            const index = selectedOption.value.indexOf((option.id || option.query))
            if (index > -1){
                selectedOption.value.splice(index, 1)
                selectedOptionDisplay.value.splice(index, 1); 
            }
            else {
                selectedOptionDisplay.value.push((option.name)); 
                selectedOption.value.push((option.id || option.query)); 
            }
        }
        else{
            const index = selectedOption.value.indexOf((option.id || option.query))
            if (index > -1){
                selectedOption.value.splice(index, 1)
                selectedOptionDisplay.value.splice(index, 1); 

            }
            else {if (selectedOption.value.length > 0){
                selectedOption.value.splice(0, 1)
                selectedOptionDisplay.value.splice(0, 1); 
                
                }
                selectedOptionDisplay.value.push((option.name)); 
                selectedOption.value.push((option.id || option.query)); 
            }
            
        }
        emit('changeTagLists', selectedOption.value)

        
    }

    const isNotSensitive = (option) => {
        if (props.filterName.toUpperCase() === "TAG"){
            console.log("Hello")
        }
        return true
    }
    const getSelectedValue = computed(() =>{
        if (selectedOptionDisplay.value.length > 0 || !props.hasValue)
            return (selectedOptionDisplay.value?.name || selectedOptionDisplay.value || 'Select sth' )
        else   
            return props.hasValue
    })

    const toggleDropdown = () => {
        visibleDropdown.value = !visibleDropdown.value
    }
    
    const closeDropdown = () =>{
        visibleDropdown.value = false
    }
</script>
