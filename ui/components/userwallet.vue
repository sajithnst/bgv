<template>
    <v-container>
        <h1 class="text-center">INR  {{ wallet }}</h1>
        <v-container class="text-center">
            <v-btn text outlined @click="sync()">Sync</v-btn>
        </v-container>
    </v-container>
</template>
<script>
export default{
    name: "userwallet",
    async mounted(){
       this.email= this.$storage.getUniversal('Email')
       let res = await this.$axios.get("http://127.0.0.1:8000/user",{params:{email : this.email}});
       this.wallet = res.data.wallet;
    },
    data:() =>({
        wallet: 0,
        email:"",
    }),
    methods: {
        async sync(){
            let res = await this.$axios.get("http://127.0.0.1:8000/user",{params:{email : this.email}});
            this.wallet = res.data.wallet;
        }
    }
}
</script>