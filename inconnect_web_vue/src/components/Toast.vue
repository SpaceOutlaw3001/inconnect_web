<script setup>
import { useToastStore } from '@/stores/toast'

const store = useToastStore()

</script>

<template>
    <div
        v-if="store.isVisible"
        :class="store.classes"
    >
        {{ store.message }}
    </div>
</template>