<template>
    <v-app hse>
    <v-container class="hseform">
        <v-form v-model="isFormValid"></v-form>
        <v-alert v-model="fail" type="error"> Data insertion Failed</v-alert>
        <h1 class="form-title text-center"> HSE Details </h1><br/>
        <v-divider></v-divider><br/>
            <v-col>
                <v-row>
                    <v-text-field label="Registration Number" v-model="regno" :rules="[rules.required]"></v-text-field>
                </v-row>
                <v-row>
                    <v-text-field label="Marks" v-model="marks" :rules="[rules.required]"></v-text-field>
                </v-row>
                <v-row>
                    <v-text-field label="School" v-model="school" :rules="[rules.required]"></v-text-field>
                </v-row>
                <v-row>
                    <v-text-field label="Year of Completion" v-model="passout" :rules="[rules.required]"></v-text-field>
                </v-row>
                <v-row>
                    <v-text-field label="Board" v--model="board" :rules="[rules.required]"></v-text-field>
                </v-row>
                <v-row>
                    <v-file-input @change="fileselect"  label = "Upload HSE Certificate as PDF" :rules="[rules.required]">
                    </v-file-input>
                </v-row>
                <v-row>
                    <v-btn large block color="teal" @click="save()" :disabled="!isFormValid">Save HSE Details</v-btn>
                </v-row>
            </v-col>
    </v-container>
</v-app>
</template>
<script>
export default{
    name: "hsedata",
    async mounted(){
        this.email= await this.$storage.getUniversal('Email');
        let url ='http://127.0.0.1:8000/user'
        await this.$axios.get(url,{params:{email : this.email}}).then(res=>{
            this.name = res.data.name
        }).catch(error => console.log(error));

    },
    data:()=>({
        isFormValid:null,
        email:'',
        name : '',
        regno: '',
        file:null,
        fail : null,
        marks:0,
        school: '',
        passout: '',
        board: '',
        rules:{
            required:(v) => !!v || "Required",
           


        }

    }),
    methods:{
        async fileselect(event){
            this.file=event
        },
        async save(){
                let hdata= {
                    regno : this.regno,
                    email: this.email,
                    name : this.name,
                    marks : this.marks,
                    school : this.school,
                    passout : this.passout,
                    board : this.board, 
                }
                let url = "http://127.0.0.1:8000/hse"
                await this.$axios.post(url, hdata).then( res => {
                    if (res.data == true){
                        this.$router.push('/ug');
                    }else{
                        this.fail= true;
                    }
                }).catch(error => console.log(error));

                let formdata= new FormData()
                formdata.append('email',this.email)
                formdata.append('regno',this.regno)
                formdata.append('file',this.file)
                let furl="http://127.0.0.1:8000/uploadhsepdf"
                await this.$axios.post(furl,formdata,{ headers : {'Content-Type': 'application/json',}}).then(res => { 
                    if (res.data == false){
                        this.fail = true
                    }
                }
                ).catch( err => { console.log(err)})
        },
    }


}
</script>
<style>
.hseform{
    width: 40%;
    margin:5% auto ;
}
</style>