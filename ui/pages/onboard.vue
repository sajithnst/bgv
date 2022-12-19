<template>
    <v-app onboard>
    <v-form firstlogin>
        <v-btn icon @click="redirect()"><v-icon size="32">mdi-archive-arrow-up-outline</v-icon></v-btn>
    </v-form>
</v-app>
</template>
<script>
export default{
    name:"firstlogin",
    data:()=>({

    }),
    methods:{
        async redirect(){
            this.$router.push('/notary')
        },
    }
}
</script>