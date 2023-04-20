
<template>
    <v-container class="text-center">
        <v-icon size="150px">mdi-account</v-icon>
        <v-container class="text-center">
            {{ name }}<br/>
            {{ email }}
        </v-container>
    </v-container>
</template>
<script>
export default {
    name:"userbanner",
    async mounted(){
        this.email = this.$storage.getUniversal('user_email')
        let url = "http://127.0.0.1:8000/user"
        let res = await this.$axios.get(url,{params:{ email :this.email}});
        this.name=res.data.name
    },
    data:()=>({
        name:"",
        email:"",

    }),
}
</script>
