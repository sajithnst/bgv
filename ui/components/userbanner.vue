<template>
    <v-container style="width: 50%;">
        <v-avatar size="100px"><v-icon  color="indigo" size="100px">mdi-account</v-icon></v-avatar>
        <h3 class="text-h5">{{ name }}</h3>
        <h3 class="text-subtitle-1">{{ email }}</h3>
    </v-container>
</template>
<script>
export default {
    name:"",
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