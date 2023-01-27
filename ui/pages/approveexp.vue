<template>
    <v-app approve>
        <v-app-bar appro>

        </v-app-bar>
        <v-main>
            <v-container>
                <v-text-field label="Employee ID" v-model="empid"></v-text-field>
                <v-btn @click="fetchexp()"> Check </v-btn>
            </v-container>
        </v-main>
        
    </v-app>
</template>
<script>     
export default {
    name: "Approve Experience",
    data:() => ({
        
    }),
}
</script>