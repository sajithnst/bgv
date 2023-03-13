<template>
    <v-container>
            <h3 class="text-center">Wallet Balance</h3>
            <h1 class="text-center">{{ wallet }}</h1>
            <v-container class="text-center">
                <v-btn text @click="getbalance()" color="primary" outlined>Sync</v-btn>
            </v-container>
    </v-container>
</template>
<script>
export default {
    name : 'userwallet',
    async mounted(){
        this.getbalance()
    },
    data :() =>({
        wallet: 0,
    }),
    methods:{
        async getbalance(){
            let url = "http://127.0.0.1:8000/user"
        }
    }

}
</script>

<style lang="scss" scoped>

</style>