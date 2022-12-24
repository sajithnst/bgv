<template>
<v-container class="sm-auto">
    <h2>Outgoing Requests</h2><br/>
        <v-list
            style="max-height:500px"
            class="overflow-y-auto">
            <v-list-item-group>
                <v-list-item v-for="exp in exps" :key="exp.empid">
                    <v-list-item-content>
                        <v-list-item-title v-text="exp.name"></v-list-item-title>
                        <v-list-item-title v-text="exp.company"></v-list-item-title>
                    </v-list-item-content>
                    <v-btn icon @click="sendverifymail(exp.empid)"><v-icon >mdi-email</v-icon></v-btn>
                </v-list-item>
            </v-list-item-group>
        </v-list>
</v-container>
</template>
<script>
export default {
    name : "outgoing",
    async mounted(){
        let eurl = "http://127.0.0.1:8000/pendingexp";
        let eres = await this.$axios.get(eurl)
        this.exps = eres.data
    },
    data : () =>({
        exps:[],
    }),
    methods:{
        async sendverifymail(empid){
            console.log(empid)
            let url = "http://127.0.0.1:8000/verifydatamail";
            let mail = {
                empid : empid
            }
            let res = await this.$axios.post(url, mail)
            console.log(res.data)
            window.location.reload()
        }
    }
}
</script>