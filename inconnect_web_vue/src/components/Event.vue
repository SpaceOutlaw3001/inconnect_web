<template>
    <label>
        {{ event.id }}
    </label>
</template>

<script>
import axios from 'axios'

export default {
    props: {
        event: Object
    },

    /* data() {
        return {
            body: '',
            is_private: false,
            url: null,
        }
    }, */

    methods: {
        
    }
}
</script>