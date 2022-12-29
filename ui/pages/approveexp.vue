<template>
    <v-app approve>
        <v-container>
            <v-text-field label="" v-model="empid"></v-text-field>
            <v-btn @click="fetchexp()"> Search </v-btn>
        </v-container>
    </v-app>
</template>
<script>     
export default {
    name: "Approve Experience",
    data:() => ({
        
    }),
}
</script>